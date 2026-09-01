import os
import shutil
import subprocess

def run_ytdlp(args):
    try:
        base_args = [
            "yt-dlp",
            "--no-warnings",
            "--geo-bypass",
            "--extractor-args", "youtube:player_client=android,web",
            "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        ]
        
        cookie_file = "cookies.txt"
        temp_cookie = "active_cookies.txt"

        if os.path.exists(cookie_file):
            shutil.copy(cookie_file, temp_cookie)
            base_args += ["--cookies", temp_cookie]
            
        cmd = base_args + args
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        if os.path.exists(temp_cookie):
            os.remove(temp_cookie)
            
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if os.path.exists("active_cookies.txt"):
            os.remove("active_cookies.txt")
        return None

def main():
    source_file = "youtube_source.txt"
    target_playlist = "ich-iptv.m3u"

    if not os.path.exists(source_file):
        print(f"File {source_file} tidak ditemukan. Melewati proses YouTube.")
        return

    with open(source_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not urls:
        print("Tidak ada URL ditemukan di youtube_source.txt.")
        return

    youtube_entries = []

    for url in urls:
        print(f"\nMemproses YouTube URL: {url}")
        
        title_res = run_ytdlp(["--get-title", url])
        if title_res and len(title_res) > 0:
            raw_title = title_res.replace(",", " ")
        else:
            raw_title = f"YouTube Stream ({url.split('v=')[-1]})"

        title = raw_title
        
        if "v=" in url:
            video_id = url.split("v=")[-1].split("&")[0]
        elif "youtu.be/" in url:
            video_id = url.split("youtu.be/")[-1].split("?")[0]
        else:
            video_id = url

        # Gunakan format URL standar watch yang paling aman untuk diproses parser
        active_url = f"https://www.youtube.com/watch?v={video_id}"
        
        print(f"Berhasil memuat judul: {title}")

        extinf = f'#EXTINF:-1 group-title="Youtube Music" tvg-name="{raw_title}",{title}\n'
        youtube_entries.append(extinf)
        youtube_entries.append(f"{active_url}\n")

    if os.path.exists(target_playlist):
        with open(target_playlist, "r", encoding="utf-8") as f:
            raw_lines = f.readlines()
    else:
        raw_lines = ["#EXTM3U\n"]

    # 1. Bersihkan total semua entri lama "Youtube Music" atau sisa sampah YouTube
    cleaned_lines = []
    skip = False
    for line in raw_lines:
        if 'group-title="Youtube Music"' in line or 'tvg-group="Youtube Music"' in line or '--- YouTube Streams ---' in line:
            skip = True
            continue
        if skip and (line.strip().startswith("http://") or line.strip().startswith("https://") or line.strip().startswith("intent://") or "youtube.com" in line or "youtu.be" in line):
            continue
        if skip and line.strip().startswith("#EXTINF"):
            skip = False
        
        if not skip:
            cleaned_lines.append(line)

    # 2. Perbaiki baris TV lain yang mungkin sempat menempel agar kembali normal
    final_content = []
    for line in cleaned_lines:
        line_str = line.strip()
        if not line_str:
            continue
        
        # Jika ada baris metadata yang menempel dengan link http
        if line_str.startswith("#EXTINF") and ("http://" in line_str or "https://" in line_str):
            if "https://" in line_str:
                parts = line_str.split("https://")
                final_content.append(parts[0].strip() + "\n")
                final_content.append("https://" + parts[1].strip() + "\n")
            elif "http://" in line_str:
                parts = line_str.split("http://")
                final_content.append(parts[0].strip() + "\n")
                final_content.append("http://" + parts[1].strip() + "\n")
        else:
            final_content.append(line_str + "\n")

    if not final_content or not final_content[0].startswith("#EXTM3U"):
        final_content.insert(0, "#EXTM3U\n")

    # 3. Masukkan kembali grup Youtube Music dengan format terpisah yang bersih di bagian akhir
    final_content.append("\n# --- Youtube Music ---\n")
    final_content.extend(youtube_entries)

    with open(target_playlist, "w", encoding="utf-8") as f:
        f.writelines(final_content)
    
    print(f"\nBerhasil merapikan kembali file {target_playlist}.")

if __name__ == "__main__":
    main()
