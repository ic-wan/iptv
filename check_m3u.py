import urllib.request

INPUT_M3U = 'ich-iptv.m3u'
ACTIVE_M3U = 'ich-iptv.m3u'
DEAD_M3U = 'hapus.m3u'

# Header M3U lengkap dengan tautan otomatis EPG
M3U_HEADER = '#EXTM3U url-tvg="https://raw.githubusercontent.com/ic-wan/iptv/main/epg-ich.xml.gz"'

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
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Gagal membaca {file_path}: {e}")
    
    return channels

def check_and_filter_playlist():
    print(f"--- 1. Memeriksa file utama: {INPUT_M3U} ---")
    active_channels = parse_m3u(INPUT_M3U)
    
    current_active_channels = []
    new_dead_channels = []

    # Cek channel aktif yang ada sekarang
    for i, ch in enumerate(active_channels):
        url = ch['url']
        print(f"[Utama {i+1}/{len(active_channels)}] Mengecek: {url}")
        
        if is_link_active(url):
            print(" -> STATUS: TETAP AKTIF")
            current_active_channels.append(ch)
        else:
            print(" -> STATUS: MATI (Dipindah ke hapus.m3u)")
            new_dead_channels.append(ch)

    print(f"\n--- 2. Memeriksa kembali arsip link mati: {DEAD_M3U} ---")
    dead_channels = parse_m3u(DEAD_M3U)
    
    remaining_dead_channels = []
    restored_count = 0

    # Cek apakah ada link mati yang hidup kembali (revived)
    for i, ch in enumerate(dead_channels):
        url = ch['url']
        print(f"[Arsip {i+1}/{len(dead_channels)}] Cek ulang: {url}")
        
        if is_link_active(url):
            print(" -> STATUS: HIDUP KEMBALI! (Dikembalikan ke playlist utama)")
            current_active_channels.append(ch)
            restored_count += 1
        else:
            print(" -> STATUS: Masih mati")
            remaining_dead_channels.append(ch)

    # Gabungkan sisa link mati lama + link mati baru yang baru saja tumbang
    # Gunakan set untuk mencegah duplikasi URL di dalam hapus.m3u
    seen_dead_urls = set()
    final_dead_channels = []
    
    for ch in (remaining_dead_channels + new_dead_channels):
        if ch['url'] not in seen_dead_urls:
            seen_dead_urls.add(ch['url'])
            final_dead_channels.append(ch)

    # Simpan kembali ke file ich-iptv.m3u
    with open(ACTIVE_M3U, 'w', encoding='utf-8') as f:
        f.write(f"{M3U_HEADER}\n")
        for ch in current_active_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    # Simpan kembali sisa link mati ke hapus.m3u
    with open(DEAD_M3U, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for ch in final_dead_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    print(f"\n=== RINGKASAN PROSES ===")
    print(f"- Total Channel Aktif Sekarang: {len(current_active_channels)}")
    print(f"- Channel Berhasil Dipulihkan dari hapus.m3u: {restored_count}")
    print(f"- Channel Baru yang Mati: {len(new_dead_channels)}")
    print(f"- Total Sisa di hapus.m3u: {len(final_dead_channels)}")

if __name__ == '__main__':
    check_and_filter_playlist()
