import os
import subprocess

def get_youtube_stream_url(youtube_url):
    """Menggunakan yt-dlp untuk mengambil direct stream URL dari video/live YouTube."""
    try:
        cmd = ["yt-dlp", "-g", "--no-warnings", youtube_url]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split("\n")
        if lines and lines[0]:
            return lines[0]
    except subprocess.CalledProcessError as e:
        print(f"Gagal mengambil stream untuk {youtube_url}: {e}")
    return None

def get_youtube_title(youtube_url):
    """Mengambil judul asli video/channel YouTube."""
    try:
        title_cmd = ["yt-dlp", "--get-title", "--no-warnings", youtube_url]
        title_res = subprocess.run(title_cmd, capture_output=True, text=True, check=True)
        if title_res.stdout.strip():
            return title_res.stdout.strip().replace(",", " ")
    except Exception:
        pass
    return "YouTube Stream"

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
        print(f"Memproses YouTube URL: {url}")
        
        # Ambil judul asli
        raw_title = get_youtube_title(url)
        stream_url = get_youtube_stream_url(url)
        
        if stream_url:
            # Jika link aktif/normal
            title = raw_title
            active_url = stream_url
            print(f"Berhasil mendapatkan stream: {title}")
        else:
            # Jika link error/mati, tambahkan awalan 'expired_' dan gunakan URL aslinya sebagai placeholder
            title = f"expired_{raw_title}"
            active_url = url
            print(f"Gagal mendapatkan stream, menandai sebagai: {title}")

        # Format baris M3U dengan group-title "Youtube Music"
        extinf = f'#EXTINF:-1 tvg-group="Youtube Music" tvg-name="{title}",{title}\n'
        youtube_entries.append(extinf)
        youtube_entries.append(f"{active_url}\n")

    if youtube_entries and os.path.exists(target_playlist):
        # Membaca isi playlist utama yang sudah ada
        with open(target_playlist, "r", encoding="utf-8") as f:
            existing_content = f.readlines()

        # Filter keluar entri YouTube lama (jika ada) agar tidak terjadi duplikasi
        cleaned_content = []
        skip = False
        for line in existing_content:
            if 'tvg-group="Youtube Music"' in line:
                skip = True
                continue
            if skip and (line.startswith("http://") or line.startswith("https://") or "youtube.com" in line or "youtu.be" in line):
                skip = False
                continue
            if not skip:
                cleaned_content.append(line)

        # Pastikan baris pertama tetap #EXTM3U
        if not cleaned_content or not cleaned_content[0].startswith("#EXTM3U"):
            cleaned_content.insert(0, "#EXTM3U\n")

        # Tambahkan entri YouTube baru di bagian bawah playlist
        cleaned_content.append("\n# --- YouTube Streams ---\n")
        cleaned_content.extend(youtube_entries)

        # Tulis ulang kembali ke ich-iptv.m3u
        with open(target_playlist, "w", encoding="utf-8") as f:
            f.writelines(cleaned_content)
        print(f"Berhasil memperbarui channel YouTube ke {target_playlist}")

if __name__ == "__main__":
    main()

