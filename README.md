# 📺 Otomatisasi IPTV, Pembersih Link & Custom EPG (`ic-wan/iptv`)

Sistem otomatisasi berbasis **GitHub Actions** yang berjalan setiap 12 jam sekali (atau dapat dijalankan secara manual) untuk mengelola playlist IPTV, membersihkan link mati, memulihkan link yang hidup kembali, dan menghasilkan jadwal EPG secara spesifik.

---

## 📂 Struktur File di Repository

* **`ich-iptv.m3u`** : Playlist M3U utama (dilengkapi header `url-tvg` otomatis) yang berisi daftar channel dan link *streaming* aktif.
* **`hapus.m3u`** : File arsip penampung link *streaming* yang mati (terakumulasi secara otomatis tanpa duplikat baris).
* **`epg-ich.xml.gz`** : File jadwal siaran (EPG) terkompresi yang murni hanya berisi jadwal untuk channel-channel yang aktif di playlist.
* **`epg_source.txt`** : File daftar link sumber EPG publik (satu link per baris) yang dapat diubah dengan mudah tanpa mengedit kode Python.
* **`check_m3u.py`** : Skrip Python untuk memvalidasi status link, membuang link mati ke arsip, serta mengetes ulang arsip untuk memulihkan link yang hidup kembali.
* **`generate_epg.py`** : Skrip Python untuk mencocokkan nama channel aktif dengan sumber EPG menggunakan metode *fuzzy matching* (ambang batas kemiripan 75%).
* **`.github/workflows/update-m3u-epg.yml`** : Konfigurasi alur kerja GitHub Actions yang mengatur seluruh proses otomatisasi secara berurutan.

---

## ⚙️ Alur Kerja Sistem (Workflow)

1. **Pengecekan & Pemulihan Playlist (`check_m3u.py`):**
   * **Penyaringan Utama:** Menguji link di `ich-iptv.m3u`. Link yang mati akan dipindahkan ke `hapus.m3u`.
   * **Pemulihan (Revival Check):** Menguji ulang link-link yang ada di dalam arsip `hapus.m3u`. Jika ada yang aktif kembali, link tersebut akan **otomatis dikembalikan** ke `ich-iptv.m3u`.
   * **Pencegahan Duplikat:** Arsip link mati diatur agar tidak memiliki baris ganda.

2. **Pembuatan EPG Khusus Playlist (`generate_epg.py`):**
   * Membaca daftar link sumber dari `epg_source.txt` dan channel aktif dari `ich-iptv.m3u`.
   * Mencocokkan nama channel menggunakan *fuzzy matching* (skor $\ge 0.75$ untuk cakupan yang lebih luas dan fleksibel), lalu mengompres hasilnya menjadi file standar XMLTV `epg-ich.xml.gz`.

3. **Penyimpanan Otomatis (`Commit & Push`):**
   * GitHub Actions mendeteksi perubahan file, melakukan *commit* otomatis, dan menyimpannya kembali ke repository.

---

## 🚀 Cara Penggunaan di Aplikasi IPTV

Salin tautan *Raw* dari file berikut untuk dimasukkan ke aplikasi pemutar IPTV Anda (seperti TiviMate, OTT Navigator, dll.):
* **Link Playlist Utama:** Mengarah ke file `ich-iptv.m3u` *(Karena sudah memiliki header url-tvg, EPG akan otomatis terhubung di aplikasi)*
* **Link EPG Utama:** Mengarah ke file `epg-ich.xml.gz`
