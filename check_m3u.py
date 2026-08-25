import urllib.request

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

def get_existing_dead_urls(dead_file):
    """Membaca file hapus.m3u yang sudah ada agar tidak terjadi duplikasi."""
    existing_urls = set()
    try:
        with open(dead_file, 'r', encoding='utf-8') as f:
            for line in f:
                line_str = line.strip()
                if line_str and not line_str.startswith('#'):
                    existing_urls.add(line_str)
    except FileNotFoundError:
        pass # Jika file belum ada, abaikan
    return existing_urls

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
            print(" -> STATUS: MATI (Masuk antrean hapus.m3u)")
            dead_channels.append(ch)

    # 1. Simpan kembali channel yang aktif ke ich-iptv.m3u (di-reset bersih dari yang mati)
    with open(ACTIVE_M3U, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for ch in active_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    # 2. Ambil URL yang sudah ada di hapus.m3u sebelumnya supaya tidak dobel
    existing_dead_urls = get_existing_dead_urls(DEAD_M3U)
    
    # Filter dead_channels yang benar-benar baru (belum ada di hapus.m3u)
    new_dead_channels = [ch for ch in dead_channels if ch['url'] not in existing_dead_urls]

    # 3. Tambahkan (menumpuk ke bawah) hanya channel mati yang BARU ke file hapus.m3u
    if new_dead_channels:
        # Cek apakah file hapus.m3u sudah punya isi atau belum
        file_is_empty = True
        try:
            with open(DEAD_M3U, 'r', encoding='utf-8') as f:
                if f.read().strip():
                    file_is_empty = False
        except FileNotFoundError:
            pass

        with open(DEAD_M3U, 'a', encoding='utf-8') as f:
            if file_is_empty:
                f.write("#EXTM3U\n")
            
            for ch in new_dead_channels:
                f.write(f"{ch['inf']}\n{ch['url']}\n")
        print(f"Berhasil menambahkan {len(new_dead_channels)} link mati baru ke {DEAD_M3U}.")
    else:
        print("Tidak ada link mati baru yang perlu ditambahkan ke hapus.m3u.")

    print(f"\nPengecekan selesai! Channel aktif tersisa: {len(active_channels)}, Channel mati baru: {len(new_dead_channels)}")

if __name__ == '__main__':
    check_and_filter_playlist()
