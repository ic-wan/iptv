import os
import re

BLACKLIST_FILE = 'blacklist_program.txt'
TARGET_FILES = ['ich-iptv.m3u', 'hapus.m3u']

def load_blacklist():
    """Memuat daftar judul program yang harus diblacklist."""
    blacklist = set()
    if not os.path.exists(BLACKLIST_FILE):
        return blacklist
    
    try:
        with open(BLACKLIST_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                item = line.strip().lower()
                if item and not item.startswith('#'):
                    blacklist.add(item)
    except Exception as e:
        print(f"Gagal memuat {BLACKLIST_FILE}: {e}")
        
    return blacklist

def extract_channel_name(extinf_line):
    """Mengekstrak nama channel dari baris EXTINF."""
    if ',' in extinf_line:
        return extinf_line.split(',')[-1].strip().lower()
    return ""

def clean_file_from_blacklist(file_path, blacklist):
    """Membersihkan satu file M3U dari channel yang masuk dalam blacklist."""
    if not os.path.exists(file_path) or not blacklist:
        return 0

    removed_count = 0
    cleaned_lines = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        header = lines[0] if lines and lines[0].startswith('#EXTM3U') else '#EXTM3U\n'
        cleaned_lines.append(header)

        current_inf = None
        for line in lines[1:]:
            line_str = line.strip()
            if line_str.startswith('#EXTINF:'):
                current_inf = line_str
            elif line_str and not line_str.startswith('#') and current_inf:
                ch_name = extract_channel_name(current_inf)
                
                # Cek apakah nama channel cocok dengan daftar blacklist
                is_blacklisted = any(bl_item in ch_name for bl_item in blacklist)
                
                if is_blacklisted:
                    print(f" -> [BLACKLIST] Dibuang dari {file_path}: {current_inf.split(',')[-1].strip()}")
                    removed_count += 1
                else:
                    cleaned_lines.append(f"{current_inf}\n")
                    cleaned_lines.append(f"{line_str}\n")
                
                current_inf = None

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(cleaned_lines)
            
    except Exception as e:
        print(f"Gagal memproses pembersihan {file_path}: {e}")

    return removed_count

def run_blacklist_filter():
    blacklist = load_blacklist()
    if not blacklist:
        print("File blacklist kosong atau tidak ditemukan. Tidak ada yang dibersihkan.")
        return

    print(f"Berhasil memuat {len(blacklist)} aturan blacklist.")
    
    total_removed = 0
    for target in TARGET_FILES:
        print(f"\nMemeriksa file: {target}")
        removed = clean_file_from_blacklist(target, blacklist)
        total_removed += removed

    print(f"\nPembersihan selesai! Total {total_removed} channel/program dibuang dari playlist.")

if __name__ == '__main__':
    run_blacklist_filter()

