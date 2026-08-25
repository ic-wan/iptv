from datetime import datetime, timezone
import urllib.request
import xml.etree.ElementTree as ET
import gzip
import io

# Daftar URL file EPG (mendukung .xml dan .xml.gz)
EPG_URLS = [
    "https://raw.githubusercontent.com/ic-wan/iptv/main/epg.xml.gz", 
    "https://raw.githubusercontent.com/dhasap/dhanytv/main/epg.xml",
    "https://www.open-epg.com/files/indonesia6.xml.gz",
    "https://www.open-epg.com/files/indonesia5.xml.gz",
    "https://www.open-epg.com/files/indonesia4.xml.gz",
    "https://www.open-epg.com/files/indonesia3.xml.gz",
    "https://www.open-epg.com/files/indonesia2.xml.gz",
    "https://www.open-epg.com/files/indonesia1.xml.gz",
]

def parse_xml_time(time_str):
    """Mengubah format waktu EPG (misal: 20260825193000 +0700) menjadi objek datetime."""
    try:
        dt_part = time_str.split()[0]
        return datetime.strptime(dt_part, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    except Exception:
        return None

def fetch_xml(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            
            # Jika URL berakhiran .gz, ekstrak terlebih dahulu di memori
            if url.endswith('.gz'):
                with gzip.GzipFile(fileobj=io.BytesIO(content)) as gz:
                    content = gz.read()
                    
            return ET.fromstring(content)
    except Exception as e:
        print(f"Gagal mendownload/mengekstrak dari {url}: {e}")
        return None

def merge_and_clean_epgs():
    root_master = None
    channels_set = set()
    
    # Waktu sekarang (UTC) untuk memfilter program lampau
    now = datetime.now(timezone.utc)

    for url in EPG_URLS:
        print(f"Memproses: {url}")
        tree = fetch_xml(url)
        if tree is None:
            continue
        
        if root_master is None:
            root_master = tree # Jadikan EPG pertama sebagai basis

        # Ambil dan filter channel (ID channel tetap dicek agar tidak error dobel di XML)
        for channel in tree.findall('channel'):
            channel_id = channel.get('id')
            if channel_id not in channels_set:
                channels_set.add(channel_id)
                root_master.append(channel)

        # Ambil programme: Masukkan semuanya TANPA CEK DUPLIKAT, 
        # asalkan jadwal selesainya (stop) belum kedaluwarsa dari waktu sekarang.
        for programme in tree.findall('programme'):
            stop_time_str = programme.get('stop')
            
            if stop_time_str:
                stop_time = parse_xml_time(stop_time_str)
                if stop_time and stop_time >= now:
                    root_master.append(programme)
            else:
                root_master.append(programme)

    if root_master is not None:
        tree_out = ET.ElementTree(root_master)
        
        # Simpan sementara string XML ke memori bytes
        xml_bytes = b'<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root_master, encoding='utf-8', xml_declaration=False)
        
        # Kompresi ke format .gz dan simpan sebagai epg.xml.gz
        with gzip.open('epg.xml.gz', 'wb') as f:
            f.write(xml_bytes)
            
        print("Berhasil menggabungkan semua program (tanpa hapus duplikat), membersihkan jadwal lama, dan mengompresi ke epg.xml.gz!")

if __name__ == '__main__':
    merge_and_clean_epgs()
