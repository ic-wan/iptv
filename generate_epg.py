import gzip
import urllib.request
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

# Konfigurasi File
M3U_FILE = 'ich-iptv.m3u'
OUTPUT_EPG = 'epg-ich.xml.gz'

# DAFTAR SUMBER EPG ANDA
# Masukkan semua link sumber XML / XML.GZ EPG yang ingin Anda gabungkan di sini
EPG_SOURCES = [
    # Contoh sumber 1 (ganti dengan URL sumber EPG asli Anda)
    "https://raw.githubusercontent.com/user/repo/main/epg1.xml.gz",
    # Contoh sumber 2
    "https://iptv-org.github.io/epg/id.xml",
]

def similarity(a, b):
    """Menghitung persentase kemiripan dua string nama channel (0.0 - 1.0)"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def parse_m3u_channels(m3u_path):
    """Mengambil daftar nama channel dari file M3U (atribut tvg-name atau nama channel setelah koma)."""
    channels = []
    try:
        with open(m3u_path, 'r', encoding='utf-8') as f:
            for line in f:
                line_str = line.strip()
                if line_str.startswith('#EXTINF:'):
                    # Coba cari tvg-name="..."
                    name = ""
                    if 'tvg-name="' in line_str:
                        try:
                            start = line_str.index('tvg-name="') + 10
                            end = line_str.index('"', start)
                            name = line_str[start:end]
                        except ValueError:
                            pass
                    
                    # Jika tvg-name tidak ada, ambil teks setelah koma terakhir
                    if not name and ',' in line_str:
                        name = line_str.split(',')[-1].strip()
                    
                    if name and name not in channels:
                        channels.append(name)
    except Exception as e:
        print(f"Gagal membaca M3U: {e}")
    
    return channels

def download_and_parse_xml(url):
    """Mengunduh dan memparsing XML EPG (mendukung file biasa atau .gz)."""
    print(f"Mengunduh EPG dari: {url}")
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read()
            
        # Cek apakah bentuknya .gz atau xml biasa
        if url.endswith('.gz') or content[:2] == b'\x1f\x8b':
            import io
            with gzip.GzipFile(fileobj=io.BytesIO(content)) as gz:
                xml_data = gz.read()
        else:
            xml_data = content
            
        root = ET.fromstring(xml_data)
        return root
    except Exception as e:
        print(f"Gagal memproses sumber {url}: {e}")
        return None

def generate_filtered_epg():
    print("Membaca channel dari M3U...")
    m3u_channels = parse_m3u_channels(M3U_FILE)
    print(f"Ditemukan {len(m3u_channels)} unique channel di {M3U_FILE}.")

    if not m3u_channels:
        print("Tidak ada channel untuk dicocokkan.")
        return

    # Struktur dasar XML EPG baru
    new_root = ET.Element('tv')
    
    matched_channel_ids = set()
    all_programmes = []

    # Kumpulkan data dari setiap sumber EPG
    for url in EPG_SOURCES:
        root = download_and_parse_xml(url)
        if root is None:
            continue
        
        source_channels = root.findall('channel')
        source_programmes = root.findall('programme')

        print(f"Mencocokkan channel dari sumber: {url}")
        
        # Mapping id lama ke elemen channel
        id_map = {}
        for ch in source_channels:
            ch_id = ch.get('id')
            # Ambil nama display-name
            display_name_elem = ch.find('display-name')
            if display_name_elem is not None and display_name_elem.text:
                ch_name = display_name_elem.text.strip()
                
                # Cocokkan dengan nama di M3U menggunakan algoritma kemiripan (> 0.8 / 80% mirip)
                for m3u_name in m3u_channels:
                    score = similarity(ch_name, m3u_name)
                    if score >= 0.85: # Ambang batas kemiripan
                        id_map[ch_id] = ch
                        matched_channel_ids.add(ch_id)
                        # Tambahkan elemen channel ke root baru (izinkan duplikasi jika dari sumber berbeda)
                        new_root.append(ch)
                        break

        # Simpan sementara program yang cocok dengan channel id tersebut
        for prog in source_programmes:
            prog_channel = prog.get('channel')
            if prog_channel in id_map:
                all_programmes.append(prog)

    # Masukkan semua program yang cocok ke root baru
    for prog in all_programmes:
        new_root.append(prog)

    # Tulis ke file epg-ich.xml.gz
    print(f"Menyimpan hasil EPG ke {OUTPUT_EPG}...")
    xml_str = ET.tostring(new_root, encoding='utf-8', xml_declaration=True)
    
    with gzip.open(OUTPUT_EPG, 'wb') as f:
        f.write(xml_str)

    print(f"Selesai! Total elemen channel & program yang difilter berhasil disimpan ke {OUTPUT_EPG}.")

if __name__ == '__main__':
    generate_filtered_epg()
