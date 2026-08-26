import urllib.request
import urllib.error
import os
from urllib.parse import urlparse

INPUT_M3U = 'ich-iptv.m3u'
TRASH_M3U = 'hapus.m3u'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': '*/*'
}

def load_existing_trash():
    """Memuat link yang sudah ada di dalam file hapus.m3u agar tidak duplikat."""
    trash_links = set()
    if not os.path.exists(TRASH_M3U):
        return trash_links
    
    try:
        with open(TRASH_M3U, 'r', encoding='utf-8') as f:
            for line in f:
                line_str = line.strip()
                if line_str and not line_str.startswith('#'):
                    trash_links.add(line_str)
    except Exception:
        pass
    return trash_links

def level_1_quick_check(url):
    """
    Level 1: Pengecekan Cepat (Fast HTTP Response Check).
    Memastikan server merespons dengan status 200 OK dalam waktu singkat.
    """
    try:
        req = urllib.request.Request(url, headers=HEADERS, method='GET')
        # Timeout sangat cepat (5 detik) untuk menyaring link mati total
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except Exception:
        return False

def level_2_deep_check(url):
    """
    Level 2: Pengecekan Mendalam (Content & Stream Validation).
    Dijalankan khusus bagi link yang lolos Level 1 untuk memvalidasi isi payload m3u8.
    """
    try:
        parsed_url = urlparse(url)
        referer_base = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        
        custom_headers = HEADERS.copy()
        custom_headers['Referer'] = referer_base

        req = urllib.request.Request(url, headers=custom_headers)
        with urllib.request.urlopen(req, timeout=8) as response:
            if response.status != 200:
                return False
            
            # Jika berformat m3u8, baca isinya untuk memastikan validitas file streaming
            if url.endswith('.m3u8') or 'm3u8' in url.lower():
                content = response.read(1024).decode('utf-8', errors='ignore')
                # Tolak jika balasan berupa halaman HTML error atau proteksi Cloudflare
                if '<html' in content.lower() or 'access denied' in content.lower() or 'error' in content.lower():
                    return False
                if '#extinf' in content.lower() or '.ts' in content.lower() or 'm3u' in content.lower() or 'm4s' in content.lower():
                    return True
                if len(content.strip()) == 0:
                    return False
            
            return True
    except Exception:
        return False

def is_stream_valid_2levels(url):
    """Menggabungkan 2 level pengecekan untuk efisiensi waktu dan akurasi tinggi."""
    # Level 1: Cepat
    if not level_1_quick_check(url):
        return False
    
    # Level 2: Mendalam (hanya jika lolos Level 1)
    return level_2_deep_check(url)

def check_and_clean_playlists():
    if not os.path.exists(INPUT_M3U):
        print(f"File {INPUT_M3U} tidak ditemukan.")
        return

    print("Mulai memvalidasi channel dengan sistem 2 Level (Cepat & Mendalam)...")

    with open(INPUT_M3U, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    valid_channels = []
    dead_channels = []
    
    current_inf = None
    active_count = 0
    dead_count = 0

    for line in lines:
        line_str = line.strip()
        if line_str.startswith('#EXTINF:'):
            current_inf = line_str
        elif line_str and not line_str.startswith('#') and current_inf:
            url = line_str
            print(f"Menguji: {url}")
            
            if is_stream_valid_2levels(url):
                valid_channels.append({'inf': current_inf, 'url': url})
                active_count += 1
                print(" -> [AKTIF (Lolos 2 Level)]")
            else:
                dead_channels.append({'inf': current_inf, 'url': url})
                dead_count += 1
                print(" -> [MATI / GAGAL]")
            current_inf = None

    # Proses Revival Check (Memulihkan link dari hapus.m3u dengan sistem 2 level)
    existing_trash = load_existing_trash()
    revived_count = 0
    
    if os.path.exists(TRASH_M3U):
        print("\nMemeriksa kembali arsip link mati (Revival Check 2 Level)...")
        with open(TRASH_M3U, 'r', encoding='utf-8') as f:
            trash_lines = f.readlines()
        
        t_inf = None
        remaining_trash = []
        for line in trash_lines:
            line_str = line.strip()
            if line_str.startswith('#EXTINF:'):
                t_inf = line_str
            elif line_str and not line_str.startswith('#') and t_inf:
                t_url = line_str
                if is_stream_valid_2levels(t_url):
                    print(f" -> [PULIH] {t_url} kembali aktif!")
                    valid_channels.append({'inf': t_inf, 'url': t_url})
                    revived_count += 1
                else:
                    remaining_trash.append({'inf': t_inf, 'url': t_url})
                t_inf = None
        
        with open(TRASH_M3U, 'w', encoding='utf-8') as tf:
            tf.write('#EXTM3U\n')
            for item in remaining_trash:
                tf.write(f"{item['inf']}\n{item['url']}\n")
    
    # Simpan playlist utama yang sudah bersih
    header_line = '#EXTM3U url-tvg="https://raw.githubusercontent.com/ic-wan/iptv/main/epg-ich.xml.gz"'
    with open(INPUT_M3U, 'w', encoding='utf-8') as f:
        f.write(f"{header_line}\n")
        for ch in valid_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    # Masukkan link mati baru ke hapus.m3u
    if dead_channels:
        mode = 'a' if os.path.exists(TRASH_M3U) else 'w'
        with open(TRASH_M3U, mode, encoding='utf-8') as tf:
            if mode == 'w':
                tf.write('#EXTM3U\n')
            for ch in dead_channels:
                if ch['url'] not in existing_trash:
                    tf.write(f"{ch['inf']}\n{ch['url']}\n")

    print(f"\nSelesai! Aktif: {active_count} | Masuk Arsip Mati: {dead_count} | Dipulihkan: {revived_count}")

if __name__ == '__main__':
    check_and_clean_playlists()
