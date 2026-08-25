from datetime import datetime, timezone
import urllib.request
import xml.etree.ElementTree as ET

# Daftar URL file EPG yang ingin digabungkan (Ganti dengan link RAW masing-masing)
EPG_URLS = [
    "https://raw.githubusercontent.com/ic-wan/iptv/main/epg.xml",
    "https://raw.githubusercontent.com/dhasap/dhanytv/main/epg.xml",
    "https://www.open-epg.com/files/indonesia6.xml",
    "https://www.open-epg.com/files/indonesia5.xml",
    "https://www.open-epg.com/files/indonesia4.xml",
    "https://www.open-epg.com/files/indonesia3.xml",
    "https://www.open-epg.com/files/indonesia2.xml",
    "https://www.open-epg.com/files/indonesia1.xml",
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
            return ET.fromstring(response.read())
    except Exception as e:
        print(f"Gagal mendownload dari {url}: {e}")
        return None

def merge_and_clean_epgs():
    root_master = None
    channels_set = set()
    
    # Waktu sekarang (UTC) untuk memfilter program lampau
    now = datetime.now(timezone.utc)

    for url in EPG_URLS:
        tree = fetch_xml(url)
        if tree is None:
            continue
        
        if root_master is None:
            root_master = tree # Jadikan EPG pertama sebagai basis

        # Ambil dan filter channel (mencegah duplikat ID)
        for channel in tree.findall('channel'):
            channel_id = channel.get('id')
            if channel_id not in channels_set:
                channels_set.add(channel_id)
                root_master.append(channel)

        # Ambil dan filter programme (buang yang sudah lewat)
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
        with open('epg.xml', 'wb') as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            tree_out.write(f, encoding='utf-8', xml_declaration=False)
        print("Berhasil menggabungkan dan membersihkan EPG dari jadwal kadaluarsa!")

if __name__ == '__main__':
    merge_and_clean_epgs()
