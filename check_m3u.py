import urllib.request

# Konfigurasi nama file sesuai punya Anda
INPUT_M3U = 'ich-iptv.m3u'
ACTIVE_M3U = 'ich-iptv.m3u'
DEAD_M3U = 'hapus.m3u'

def is_link_active(url, timeout=4):
    """Mengecek apakah link streaming m3u8/http masih aktif."""
    if not url or not url.startswith('http'):
        return False
    
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status < 400:
                return True
    except Exception:
        return False
    return False

def parse_m3u(file_path):
    """Membaca file M3U dan mengambil baris EXTINF serta URL-nya."""
    channels = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        current_inf = None
        for line in lines:
            line_str = line.strip()
            if line_str.startswith('#EXTINF:'):
                current_inf = line_str
            elif line_str and not line_str.startswith('#') and current_inf:
                channels.append({'inf': current_inf, 'url': line_str})
                current_inf = None
    except Exception as e:
        print(f"Gagal membaca {file_path}: {e}")
    
    return channels

def check_and_filter_playlist():
    print(f"Membaca file {INPUT_M3U}...")
    channels = parse_m3u(INPUT_M3U)
    
    if not channels:
        print("Tidak ada channel ditemukan atau file kosong.")
        return

    print(f"Total channel yang akan dicek: {len(channels)}")
    
    active_channels = []
    dead_channels = []

    for i, ch in enumerate(channels):
        url = ch['url']
        print(f"[{i+1}/{len(channels)}] Mengecek: {url}")
        
        if is_link_active(url):
            print(" -> STATUS: AKTIF")
            active_channels.append(ch)
        else:
            print(" -> STATUS: MATI (Dipindah ke hapus.m3u)")
            dead_channels.append(ch)

    # Simpan kembali channel yang aktif ke ich-iptv.m3u
    with open(ACTIVE_M3U, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for ch in active_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    # Simpan/tumpuk channel yang mati ke hapus.m3u
    with open(DEAD_M3U, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for ch in dead_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    print(f"\nPengecekan selesai! Channel aktif: {len(active_channels)}, Channel mati dipindah: {len(dead_channels)}")

if __name__ == '__main__':
    check_and_filter_playlist()
