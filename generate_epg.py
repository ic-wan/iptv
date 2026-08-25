import gzip
import io
import urllib.request
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

M3U_FILE = 'ich-iptv.m3u'
OUTPUT_EPG = 'epg-ich.xml.gz'
SOURCE_FILE = 'epg_source.txt'

def load_epg_sources(source_path):
    """Membaca daftar URL sumber EPG dari file teks (per baris)."""
    sources = []
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            for line in f:
                url = line.strip()
                # Abaikan baris kosong atau baris komentar (#)
                if url and not url.startswith('#'):
                    sources.append(url)
    except FileNotFoundError:
        print(f"File sumber {source_path} tidak ditemukan!")
    except Exception as e:
        print(f"Gagal membaca {source_path}: {e}")
    return sources

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def parse_m3u_channels(m3u_path):
    channels = []
    try:
        with open(m3u_path, 'r', encoding='utf-8') as f:
            for line in f:
                line_str = line.strip()
                if line_str.startswith('#EXTINF:'):
                    name = ""
                    if 'tvg-name="' in line_str:
                        try:
                            start = line_str.index('tvg-name="') + 10
                            end = line_str.index('"', start)
                            name = line_str[start:end]
                        except ValueError:
                            pass
                    
                    if not name and ',' in line_str:
                        name = line_str.split(',')[-1].strip()
                    
                    if name and name not in channels:
                        channels.append(name)
    except Exception as e:
        print(f"Gagal membaca M3U: {e}")
    
    return channels

def download_and_parse_xml(url):
    print(f"Mengunduh EPG dari: {url}")
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read()
            
        if url.endswith('.gz') or content[:2] == b'\x1f\x8b':
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
    epg_sources = load_epg_sources(SOURCE_FILE)
    if not epg_sources:
        print("Tidak ada sumber EPG yang dimuat dari file.")
        return

    print(f"Berhasil memuat {len(epg_sources)} sumber EPG dari {SOURCE_FILE}.")
    print("Membaca channel dari M3U...")
    
    m3u_channels = parse_m3u_channels(M3U_FILE)
    print(f"Ditemukan {len(m3u_channels)} unique channel di {M3U_FILE}.")

    if not m3u_channels:
        print("Tidak ada channel untuk dicocokkan.")
        return

    new_root = ET.Element('tv')
    matched_channel_ids = set()
    all_programmes = []

    for url in epg_sources:
        root = download_and_parse_xml(url)
        if root is None:
            continue
        
        source_channels = root.findall('channel')
        source_programmes = root.findall('programme')

        print(f"Mencocokkan channel dari sumber: {url}")
        
        id_map = {}
        for ch in source_channels:
            ch_id = ch.get('id')
            display_name_elem = ch.find('display-name')
            if display_name_elem is not None and display_name_elem.text:
                ch_name = display_name_elem.text.strip()
                
                for m3u_name in m3u_channels:
                    score = similarity(ch_name, m3u_name)
                    if score >= 0.85:
                        id_map[ch_id] = ch
                        matched_channel_ids.add(ch_id)
                        new_root.append(ch)
                        break

        for prog in source_programmes:
            prog_channel = prog.get('channel')
            if prog_channel in id_map:
                all_programmes.append(prog)

    for prog in all_programmes:
        new_root.append(prog)

    print(f"Menyimpan hasil EPG ke {OUTPUT_EPG}...")
    xml_str = ET.tostring(new_root, encoding='utf-8', xml_declaration=True)
    
    with gzip.open(OUTPUT_EPG, 'wb') as f:
        f.write(xml_str)

    print(f"Selesai! Berhasil menyimpan ke {OUTPUT_EPG}.")

if __name__ == '__main__':
    generate_filtered_epg()
