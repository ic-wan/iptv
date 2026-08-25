import urllib.request
import re
import os

SOURCE_FILE = 'm3u_source.txt'
KEYWORD_FILE = 'keyword.txt'
OUTPUT_M3U = 'ich-iptv.m3u'

# Header M3U lengkap dengan tautan otomatis EPG
M3U_HEADER = '#EXTM3U url-tvg="https://raw.githubusercontent.com/ic-wan/iptv/main/epg-ich.xml.gz"'

def load_keywords(keyword_path):
    """Membaca daftar kata kunci dari file teks (per baris)."""
    keywords = []
    try:
        with open(keyword_path, 'r', encoding='utf-8') as f:
            for line in f:
                kw = line.strip().lower()
                # Abaikan baris kosong atau baris komentar (#)
                if kw and not kw.startswith('#'):
                    keywords.append(kw)
    except FileNotFoundError:
        print(f"File kata kunci {keyword_path} tidak ditemukan! Menggunakan kata kunci default.")
        # Cadangan default jika file belum dibuat
        keywords = ['indonesia', 'rcti', 'sctv', 'indosiar', 'trans7', 'transtv']
    except Exception as e:
        print(f"Gagal membaca {keyword_path}: {e}")
    return keywords

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

def is_indonesian_channel(extinf_line, keywords):
    """Menyaring apakah sebuah channel tergolong channel Indonesia berdasarkan keyword.txt."""
    line_lower = extinf_line.lower()
    
    for keyword in keywords:
        if keyword in line_lower:
            return True
            
    return False

def standardize_group_title(extinf_line):
    """Mengubah atau menambahkan group-title menjadi 'Lokal (auto)'."""
    if 'group-title=' in extinf_line:
        updated_line = re.sub(r'group-title="[^"]*?"', 'group-title="Lokal (auto)"', extinf_line, flags=re.IGNORECASE)
        return updated_line
    else:
        updated_line = extinf_line.replace('#EXTINF:', '#EXTINF:-1 group-title="Lokal (auto)"', 1)
        return updated_line

def parse_existing_m3u(file_path):
    """Membaca file M3U yang sudah ada di lokal agar datanya tidak hilang."""
    channels = []
    seen_urls = set()
    if not os.path.exists(file_path):
        return channels, seen_urls

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        current_inf = None
        for line in lines:
            line_str = line.strip()
            if line_str.startswith('#EXTINF:'):
                current_inf = line_str
            elif line_str and not line_str.startswith('#') and current_inf:
                if line_str not in seen_urls:
                    seen_urls.add(line_str)
                    channels.append({'inf': current_inf, 'url': line_str})
                current_inf = None
    except Exception as e:
        print(f"Gagal membaca file M3U lama: {e}")
        
    return channels, seen_urls

def grab_and_merge_indo_channels():
    # Muat kata kunci dari keyword.txt
    keywords = load_keywords(KEYWORD_FILE)
    print(f"Berhasil memuat {len(keywords)} kata kunci penyaringan dari {KEYWORD_FILE}.")

    # Muat channel lama yang sudah ada di ich-iptv.m3u
    existing_channels, seen_urls = parse_existing_m3u(OUTPUT_M3U)
    print(f"Memuat {len(existing_channels)} channel yang sudah ada di dalam {OUTPUT_M3U}.")

    m3u_sources = load_m3u_sources(SOURCE_FILE)
    if not m3u_sources:
        print("Tidak ada sumber M3U yang dimuat dari file.")
        return

    print(f"Berhasil memuat {len(m3u_sources)} sumber M3U baru dari {SOURCE_FILE}.")
    
    new_added_count = 0

    # Ambil channel baru dari internet
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
                # Saring menggunakan daftar kata kunci dari file keyword.txt
                if (is_indonesian_channel(current_inf, keywords) or is_indonesian_channel(line_str, keywords)) and line_str not in seen_urls:
                    seen_urls.add(line_str)
                    
                    # Ubah nama grup otomatis menjadi "Lokal (auto)"
                    formatted_inf = standardize_group_title(current_inf)
                    
                    existing_channels.append({'inf': formatted_inf, 'url': line_str})
                    new_added_count += 1
                current_inf = None

    # Tulis ulang file dengan menggabungkan data lama + data baru di bawahnya
    with open(OUTPUT_M3U, 'w', encoding='utf-8') as f:
        f.write(f"{M3U_HEADER}\n")
        for ch in existing_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    print(f"Selesai! Berhasil menambahkan {new_added_count} channel baru ke baris bawah. Total keseluruhan: {len(existing_channels)} channel.")

if __name__ == '__main__':
    grab_and_clone = grab_and_merge_indo_channels()
