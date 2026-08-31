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
            "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        ]
        
        cookie_file = "cookies.txt"
        temp_cookie = "active_cookies.txt"

        if os.path.exists(cookie_file):
            with open(cookie_file, "r", encoding="utf-8") as cf:
                content = cf.read()
                if "SID=" not in content and "__Secure" not in content:
                    print("[WARNING] File cookies.txt TIDAK MEMILIKI TOKEN SESI AKUN!")
                else:
                    print("[INFO] Token sesi akun terdeteksi di dalam cookies.txt.")

            shutil.copy(cookie_file, temp_cookie)
            base_args += ["--cookies", temp_cookie]
        else:
            print("[WARNING] File cookies.txt TIDAK DITEMUKAN!")
            
        cmd = base_args + args
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        if os.path.exists(temp_cookie):
            os.remove(temp_cookie)
            
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if os.path.exists("active_cookies.txt"):
            os.remove("active_cookies.txt")
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

        # Mengubah parameter format dari bestaudio ke format default terbaik yang didukung langsung tanpa ffmpeg
        stream_res = run_ytdlp(["-g", "-f", "bv*+ba/b", url])
        
        if not stream_res:
            # Fallback jika format pertama gagal, coba ambil format paling universal (biasanya mp4/webm standar)
            stream_res = run_ytdlp(["-g", "-f", "b", url])

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
        skip = False
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
