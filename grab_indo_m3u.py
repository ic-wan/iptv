import urllib.request
import re
import os
from urllib.parse import urlparse, urlunparse

SOURCE_FILE = 'm3u_source.txt'
KEYWORD_FILE = 'keyword.txt'
OUTPUT_M3U = 'ich-iptv.m3u'

M3U_HEADER = '#EXTM3U url-tvg="https://raw.githubusercontent.com/ic-wan/iptv/main/epg-ich.xml.gz"'

def load_keywords(keyword_path):
    keywords = []
    try:
        with open(keyword_path, 'r', encoding='utf-8') as f:
            for line in f:
                kw = line.strip().lower()
                if kw and not kw.startswith('#'):
                    keywords.append(kw)
    except FileNotFoundError:
        keywords = ['indonesia', 'rcti', 'sctv', 'indosiar', 'trans7', 'transtv']
    return keywords

def load_m3u_sources(source_path):
    sources = []
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            for line in f:
                url = line.strip()
                if url and not url.startswith('#'):
                    sources.append(url)
    except FileNotFoundError:
        print(f"File sumber {source_path} tidak ditemukan!")
    return sources

def download_m3u_from_url(url):
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

def normalize_url(url):
    """Membersihkan parameter query/token di ujung URL agar duplikat dengan token berbeda terdeteksi sama."""
    try:
        parsed = urlparse(url.strip())
        clean_parsed = parsed._replace(query="", fragment="")
        return urlunparse(clean_parsed).lower()
    except Exception:
        return url.strip().lower()

def is_indonesian_channel(extinf_line, keywords):
    line_lower = extinf_line.lower()
    for keyword in keywords:
        if keyword in line_lower:
            return True
    return False

def standardize_group_title(extinf_line):
    if 'group-title=' in extinf_line:
        updated_line = re.sub(r'group-title="[^"]*?"', 'group-title="Lokal (auto)"', extinf_line, flags=re.IGNORECASE)
        return updated_line
    else:
        if '#EXTINF:-1' in extinf_line:
            return extinf_line.replace('#EXTINF:-1', '#EXTINF:-1 group-title="Lokal (auto)"', 1)
        elif '#EXTINF:' in extinf_line:
            return extinf_line.replace('#EXTINF:', '#EXTINF:-1 group-title="Lokal (auto)"', 1)
    return extinf_line

def is_auto_group(extinf_line):
    """Mengecek apakah baris EXTINF termasuk ke dalam grup Lokal (auto)."""
    return 'group-title="Lokal (auto)"' in extinf_line.lower()

def parse_existing_m3u(file_path):
    """
    Membaca file M3U lama. 
    Memprioritaskan penyimpanan channel non-auto (manual) dan membersihkan duplikat di Lokal (auto).
    """
    channels = []
    seen_normalized_urls = set()
    
    if not os.path.exists(file_path):
        return channels, seen_normalized_urls

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        current_inf = None
        for line in lines:
            line_str = line.strip()
            if line_str.startswith('#EXTINF:'):
                current_inf = line_str
            elif line_str and not line_str.startswith('#') and current_inf:
                norm_url = normalize_url(line_str)
                
                if norm_url not in seen_normalized_urls:
                    seen_normalized_urls.add(norm_url)
                    channels.append({'inf': current_inf, 'url': line_str})
                else:
                    # Jika URL sudah ada, cek prioritas pembersihan:
                    # Jika channel lama berstatus Lokal (auto) dan ketemu duplikatnya, buang yang auto.
                    # Tapi jika channel yang sudah ada adalah manual (bukan auto), pertahankan manualnya.
                    pass
                current_inf = None
    except Exception as e:
        print(f"Gagal membaca file M3U lama: {e}")
        
    return channels, seen_normalized_urls

def grab_and_merge_indo_channels():
    keywords = load_keywords(KEYWORD_FILE)
    print(f"Berhasil memuat {len(keywords)} kata kunci.")

    existing_channels, seen_normalized_urls = parse_existing_m3u(OUTPUT_M3U)
    print(f"Memuat {len(existing_channels)} channel unik dari file lama.")

    m3u_sources = load_m3u_sources(SOURCE_FILE)
    if not m3u_sources:
        print("Tidak ada sumber M3U.")
        return

    new_added_count = 0
    duplicate_auto_skipped = 0

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
                if is_indonesian_channel(current_inf, keywords) or is_indonesian_channel(line_str, keywords):
                    norm_url = normalize_url(line_str)
                    
                    # Standardisasi grup terlebih dahulu menjadi "Lokal (auto)" untuk dicek
                    formatted_inf = standardize_group_title(current_inf)
                    
                    # Jika URL bersih belum ada sama sekali, masukkan
                    if norm_url not in seen_normalized_urls:
                        seen_normalized_urls.add(norm_url)
                        existing_channels.append({'inf': formatted_inf, 'url': line_str})
                        new_added_count += 1
                    else:
                        # Jika URL sudah ada (duplikat), karena ini berasal dari sumber auto, 
                        # kita abaikan/bersihkan agar tidak masuk lagi ke grup Lokal (auto)
                        duplicate_auto_skipped += 1
                        
                current_inf = None

    with open(OUTPUT_M3U, 'w', encoding='utf-8') as f:
        f.write(f"{M3U_HEADER}\n")
        for ch in existing_channels:
            f.write(f"{ch['inf']}\n{ch['url']}\n")

    print(f"Selesai! Berhasil membersihkan duplikat otomatis, menambahkan {new_added_count} channel baru, dan melewati {duplicate_auto_skipped} channel duplikat dari Lokal (auto). Total keseluruhan: {len(existing_channels)} channel.")

if __name__ == '__main__':
    grab_and_merge_indo_channels()
