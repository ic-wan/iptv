import urllib.request
import re

SOURCE_FILE = 'm3u_source.txt'
OUTPUT_M3U = 'ich-iptv.m3u'

# Header M3U lengkap dengan tautan otomatis EPG
M3U_HEADER = '#EXTM3U url-tvg="https://raw.githubusercontent.com/ic-wan/iptv/main/epg-ich.xml.gz"'

def load_m3u_sources(source_path):
    """Membaca daftar URL sumber M3U dari file teks (per baris)."""
    sources = []
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            for line in f:
                url = line.strip()
                if url and not url.startswith('#'):
                    sources.append(url)
    except FileNotFoundError:
        print(f"File sumber {source_path} tidak ditemukan!")
    except Exception as e:
        print(f"Gagal membaca {source_path}: {e}")
    return sources

def download_m3u_from_url(url):
    """Mengunduh file M3U dari URL publik."""
    print(f"Mengunduh M3U sumber dari: {url}")
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Gagal mengunduh M3U dari sumber {url}: {e}")
        return None

def is_indonesian_channel(extinf_line):
    """Menyaring apakah sebuah channel tergolong channel Indonesia."""
    line_lower = extinf_line.lower()
    
    indo_keywords = [
        'group-title="indonesia"', 'group-title="id"', 'tvg-country="id"', 
        'indonesia', 'rcti', 'sctv', 'indosiar', 'mnctv', 'antv', 'trans7', 
        'transtv', 'metrotv', 'tvone', 'kompastv', 'nettv', 'net.', 'rtv', 
        'inews', 'gictv', 'beritasatu', 'cnn indonesia', 'cnbc indonesia', 
        'tvri', 'jaktv', 'doremi', 'indonesiana'
    ]
    
    for keyword in indo_keywords:
        if keyword in line_lower:
            return True
            
    return False

def standardize_group_title(extinf_line):
    """Mengubah atau menambahkan group-title menjadi 'Lokal (auto)'."""
    # Cek apakah sudah ada atribut group-title="..." di dalam tag EXTINF
    if 'group-title=' in extinf_line:
        # Ganti nilai group-title yang lama dengan "Lokal (auto)"
        updated_line = re.sub(r'group-title="[^"]*?"', 'group-title="Lokal (auto)"', extinf_line, flags=re.IGNORECASE)
        return updated_line
    else:
        # Jika belum ada atribut group-title, sisipkan di sebelah tulisan #EXTINF:-1
        updated_line = extinf_line.replace('#EXTINF:', '#EXTINF:-1 group-title="Lokal (auto)"', 1)
        return updated_line

def grab_and_filter_indo_channels():
    m3u_sources = load_m3u_sources(SOURCE_FILE)
    if not m3u_sources:
        print("Tidak ada sumber M3U yang dimuat dari file.")
        return

    print(f"Berhasil memuat {len(m3u_sources)} sumber M3U dari {SOURCE_FILE}.")
    
    all_filtered_channels = []
    seen_urls = set()

    for url in m3u_sources:
        raw_content = download_m3u_from_url(url)
        if not raw_content:
            continue

        lines = raw_content.splitlines()
        current_inf = None
        
        for line in lines:
            line_str = line.strip()
            if line_str.startswith('#EXTINF:'):
                current_inf = line_str
            elif line_str and not line_str.startswith('#') and current_inf:
                # Saring channel Indonesia dan pastikan URL tidak duplikat
                if (is_indonesian_channel(current_inf) or is_indonesian_channel(line_str)) and line_str not in seen_urls:
                    seen_urls.add(line_str)
                    
                    # Ubah nama grup otomatis menjadi "Lokal (auto)"
                    formatted_inf = standardize_group_title(current_inf)
                    
                    all_filtered_channels.append({'inf': formatted_inf, 'url': line_str})
                current_inf = None

    # Simpan hasil saringan ke ich-iptv.m3u
    with open(OUTPUT_M3U, 'w', encoding='utf-8') as f:
        f.write(f"{M3U_HEADER}\n")
        for ch in all_filtered_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    print(f"Selesai! Berhasil menyaring, mengubah grup, dan menyimpan {len(all_filtered_channels)} channel ke {OUTPUT_M3U}.")

if __name__ == '__main__':
    grab_and_filter_indo_channels()

