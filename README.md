# 📺 Otomatisasi IPTV & EPG (`ic-wan/iptv`)

Sistem otomatisasi berbasis **GitHub Actions** yang berjalan setiap 12 jam sekali (atau dapat dijalankan secara manual) untuk mengelola playlist IPTV dan jadwal EPG secara spesifik dan bersih.

---

## 📂 Struktur File di Repository

* **`ich-iptv.m3u`** : Playlist M3U utama yang berisi daftar channel dan link *streaming* aktif.
* **`hapus.m3u`** : File arsip penampung link *streaming* yang sudah mati (terakumulasi ke bawah secara otomatis tanpa duplikat baris).
* **`epg-ich.xml.gz`** : File jadwal siaran (EPG) terkompresi yang murni hanya berisi jadwal untuk channel-channel yang aktif di `ich-iptv.m3u`.
* **`epg_source.txt`** : File daftar link sumber EPG publik (satu link per baris) yang dapat diubah dengan mudah tanpa mengedit kode Python.
* **`check_m3u.py`** : Skrip Python untuk memvalidasi status kesehatan (HTTP status) link pada playlist utama.
* **`generate_epg.py`** : Skrip Python untuk mencocokkan nama channel aktif dengan sumber-sumber EPG menggunakan algoritma kemiripan teks (*fuzzy matching* >85%).
* **`.github/workflows/update-m3u-epg.yml`** : Konfigurasi alur kerja GitHub Actions yang mengatur seluruh otomatisasi secara berurutan.

---

## ⚙️ Alur Kerja Sistem (Workflow)

1. **Pengecekan & Pembersihan Playlist (`check_m3u.py`):**
   * Membaca file `ich-iptv.m3u` dan menguji respons link satu per satu.
   * Link yang **aktif** tetap dipertahankan di `ich-iptv.m3u`.
   * Link yang **mati** dihapus dari playlist utama dan ditambahkan secara akumulatif ke dalam file `hapus.m3u` (dengan sistem pencegahan duplikat).

2. **Pembuatan EPG Khusus Playlist (`generate_epg.py`):**
   * Membaca daftar link sumber dari `epg_source.txt` dan channel aktif dari `ich-iptv.m3u`.
   * Mencocokkan nama channel menggunakan *fuzzy matching*, mengizinkan duplikasi sumber untuk melengkapi jadwal, lalu mengompres hasilnya menjadi file standar XMLTV `epg-ich.xml.gz`.

3. **Penyimpanan Otomatis (`Commit & Push`):**
   * GitHub Actions mendeteksi perubahan file, melakukan *commit* otomatis, dan menyimpannya kembali ke repository.

---

## 🚀 Cara Penggunaan di Aplikasi IPTV

Salin tautan *Raw* dari file berikut untuk dimasukkan ke aplikasi pemutar IPTV Anda (seperti TiviMate, OTT Navigator, dll.):
* **Link Playlist Utama:** Mengarah ke file `ich-iptv.m3u`
* **Link EPG Utama:** Mengarah ke file `epg-ich.xml.gz`
