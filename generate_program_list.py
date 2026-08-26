import os
import re

def parse_m3u_file(file_path):
    grouped_channels = {}
    if not os.path.exists(file_path):
        return grouped_channels
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            line_str = line.strip()
            if line_str.startswith('#EXTINF:'):
                channel_name = line_str.split(',')[-1].strip() if ',' in line_str else "Unknown"
                group_match = re.search(r'group-title="([^"]*)"', line_str, re.IGNORECASE)
                group_name = group_match.group(1).strip() if group_match else "Uncategorized"
                
                if group_name not in grouped_channels:
                    grouped_channels[group_name] = []
                if channel_name not in grouped_channels[group_name]:
                    grouped_channels[group_name].append(channel_name)
    except Exception:
        pass
    return grouped_channels

def generate_program_list():
    output_txt = 'List_program.txt'
    sources = {
        "Playlist Utama (ich-iptv.m3u)": "ich-iptv.m3u",
        "Arsip Link Mati (hapus.m3u)": "hapus.m3u"
    }
    with open(output_txt, 'w', encoding='utf-8') as out:
        out.write("========================================\n")
        out.write(" DAFTAR PROGRAM / CHANNEL IPTV\n")
        out.write("========================================\n\n")
        for title, filepath in sources.items():
            out.write(f"📂 SUMBER FILE: {title}\n")
            out.write("=" * 45 + "\n")
            grouped_data = parse_m3u_file(filepath)
            if not grouped_data:
                out.write("  (Kosong)\n\n")
                continue
            for group_name, channels in sorted(grouped_data.items()):
                out.write(f"\n  📁 Grup: [{group_name}] ({len(channels)} Channel)\n")
                out.write("  " + "-" * 40 + "\n")
                for idx, ch in enumerate(sorted(channels), 1):
                    out.write(f"    {idx}. {ch}\n")
            out.write("\n" + "=" * 45 + "\n\n")

if __name__ == '__main__':
    generate_program_list()
