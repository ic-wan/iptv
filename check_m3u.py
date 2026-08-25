import urllib.request
import urllib.error
import os
from urllib.parse import urlparse

INPUT_M3U = 'ich-iptv.m3u'
TRASH_M3U = 'hapus.m3u'

# Header standar agar dianggap sebagai pemutar media sah oleh server tujuan
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

def is_stream_actually_working(url):
    """
    Melakukan validasi mendalam:
    1. Cek koneksi HTTP (harus 200 OK).
    2. Jika berupa file m3u8, pastikan isi teksnya mengandung tag valid IPTV (#EXTINF atau #EXTM3U atau segmen .ts/.m4s).
    """
    try:
        # Ekstrak domain untuk dijadikan referer otomatis jika dibutuhkan server
        parsed_url = urlparse(url)
        referer_base = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        
        custom_headers = HEADERS.copy()
        custom_headers['Referer'] = referer_base

        req = urllib.request.Request(url, headers=custom_headers)
        # Timeout diperkecil ke 10 detik agar proses berjalan efisien
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status != 200:
                return False
            
            # Jika link berformat m3u8 / playlist kecil, baca beberapa byte awal untuk verifikasi isi
            if url.endswith('.m3u8') or 'm3u8' in url.lower():
                content = response.read(1024).decode('utf-8', errors='ignore')
                # Pastikan file balasan bukan halaman HTML error / Cloudflare challenge
                if '<html' in content.lower() or 'access denied' in content.lower():
                    return False
                if '#extinf' in content.lower() or '.ts' in content.lower() or 'm3u' in content.lower():
                    return True
                # Jika m3u8 tapi kosong isinya
                if len(content.strip()) == 0:
                    return False
            
            return True
    except Exception:
        return False

def check_and_clean_playlists():
    if not os.path.exists(INPUT_M3U):
        print(f"File {INPUT_M3U} tidak ditemukan.")
        return

    print("Mulai memvalidasi status keaktifan channel dengan pengujian mendalam...")

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
            
            if is_stream_actually_working(url):
                valid_channels.append({'inf': current_inf, 'url': url})
                active_count += 1
                print(" -> [AKTIF]")
            else:
                dead_channels.append({'inf': current_inf, 'url': url})
                dead_count += 1
                print(" -> [MATI / GAGAL DIPUTAR]")
            current_inf = None

    # Proses Revival Check (Memulihkan link dari hapus.m3u yang kini hidup kembali)
    existing_trash = load_existing_trash()
    revived_count = 0
    
    if os.path.exists(TRASH_M3U):
        print("\nMemeriksa kembali arsip link mati (Revival Check)...")
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
                if is_stream_actually_working(t_url):
                    print(f" -> [PULIH] {t_url} kembali aktif dan dikembalikan ke playlist!")
                    valid_channels.append({'inf': t_inf, 'url': t_url})
                    revived_count += 1
                else:
                    remaining_trash.append({'inf': t_inf, 'url': t_url})
                t_inf = None
        
        # Simpan sisa trash yang masih mati
        with open(TRASH_M3U, 'w', encoding='utf-8') as tf:
            tf.write('#EXTM3U\n')
            for item in remaining_trash:
                tf.write(f"{item['inf']}\n{item['url']}\n")
    
    # Tulis ulang file M3U utama dengan channel yang benar-benar lolos uji
    header_line = '#EXTM3U url-tvg="https://raw.githubusercontent.com/ic-wan/iptv/main/epg-ich.xml.gz"'
    with open(INPUT_M3U, 'w', encoding='utf-8') as f:
        f.write(f"{header_line}\n")
        for ch in valid_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    # Tambahkan channel mati baru ke file hapus.m3u (tanpa duplikat)
    if dead_channels:
        mode = 'a' if os.path.exists(TRASH_M3U) else 'w'
        with open(TRASH_M3U, mode, encoding='utf-8') as tf:
            if mode == 'w':
                tf.write('#EXTM3U\n')
            for ch in dead_channels:
                if ch['url'] not in existing_trash:
                    tf.write(f"{ch['inf']}\n{ch['url']}\n")

    print(f"\nSelesai! Aktif: {active_count} | Dipindahkan ke Arsip Mati: {dead_count} | Dipulihkan: {revived_count}")

if __name__ == '__main__':
    check_and_clean_playlists()
