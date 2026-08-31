import os
import subprocess

def run_ytdlp(args):
    """Fungsi helper untuk menjalankan yt-dlp dengan pengecekan cookies yang ketat."""
    try:
        base_args = [
            "yt-dlp",
            "--no-warnings",
            "--geo-bypass"
        ]
        
        # Cek apakah file cookies.txt ada di direktori saat ini
        if os.path.exists("cookies.txt"):
            base_args += ["--cookies", "cookies.txt"]
            print("[INFO] Menggunakan file cookies.txt untuk autentikasi.")
        else:
            print("[WARNING] File cookies.txt TIDAK DITEMUKAN di direktori! YouTube akan memblokir request.")
            
        cmd = base_args + args
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"yt-dlp error detail: {e.stderr.strip() if e.stderr else e}")
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
        raw_title = title_res.replace(",", " ") if title_res else "YouTube Stream"

        stream_res = run_ytdlp(["-g", "-f", "bestaudio/best", url])
        
        if stream_res:
            lines = stream_res.split("\n")
            active_url = lines[0] if lines else url
            title = raw_title
            print(f"Berhasil mendapatkan stream: {title}")
        else:
            title = f"expired_{raw_title}"
            active_url = url
            print(f"Gagal mendapatkan stream, menandai sebagai: {title}")

        extinf = f'#EXTINF:-1 tvg-group="Youtube Music" tvg-name="{title}",{title}\n'
        youtube_entries.append(extinf)
        youtube_entries.append(f"{active_url}\n")

    if youtube_entries and os.path.exists(target_playlist):
        with open(target_playlist, "r", encoding="utf-8") as f:
            existing_content = f.readlines()

        cleaned_content = []
        skip = false = False
        for line in existing_content:
            if 'tvg-group="Youtube Music"' in line:
                skip = True
                continue
            if skip and (line.startswith("http://") or line.startswith("https://") or "youtube.com" in line or "youtu.be" in line):
                skip = True
                continue
            if skip and not (line.startswith("http://") or line.startswith("https://")):
                skip = False

            if not skip:
                cleaned_content.append(line)

        while cleaned_content and cleaned_content[-1].strip() == "":
            cleaned_content.pop()

        if not cleaned_content or not cleaned_content[0].startswith("#EXTM3U"):
            cleaned_content.insert(0, "#EXTM3U\n")

        cleaned_content.append("\n# --- YouTube Streams ---\n")
        cleaned_content.extend(youtube_entries)

        with open(target_playlist, "w", encoding="utf-8") as f:
            f.writelines(cleaned_content)
        print(f"\nBerhasil memperbarui channel YouTube ke {target_playlist}")

if __name__ == "__main__":
    main()
