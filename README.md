
# Dokumentasi Sistem Otomatisasi IPTV & EPG (`ic-wan/iptv`)

Sistem ini berjalan secara otomatis menggunakan GitHub Actions setiap 12 jam sekali (atau dapat dijalankan secara manual) untuk:
1. Mengetes keaktifan link streaming di playlist utama.
2. Memisahkan link yang mati ke file arsip khusus.
3. Membuat dan memperbarui file EPG terkompresi yang disesuaikan secara spesifik hanya untuk channel yang aktif di playlist.

---

## 📂 Struktur File di Repository

* **`ich-iptv.m3u`** : Playlist M3U utama yang berisi daftar channel dan link *streaming* aktif.
* **`hapus.m3u`** : File arsip penampung link *streaming* yang sudah mati (terakumulasi ke bawah tanpa duplikat).
* **`epg-ich.xml.gz`** : File jadwal siaran (EPG) terkompresi khusus untuk channel-channel yang aktif di `ich-iptv.m3u`.
* **`check_m3u.py`** : Skrip Python untuk memvalidasi status HTTP link pada playlist utama.
* **`generate_epg.py`** : Skrip Python untuk mencocokkan nama channel aktif dengan sumber EPG publik menggunakan *fuzzy matching* (>85% kemiripan).
* **`.github/workflows/update-iptv.yml`** : Konfigurasi alur kerja otomatisasi GitHub Actions.

---

## ⚙️ Alur Kerja Sistem (Workflow)

1. **Pengecekan Playlist (`check_m3u.py`):**
   * Membaca file `ich-iptv.m3u` dan mengetes respons link satu per satu.
   * Link yang **aktif** tetap disimpan di `ich-iptv.m3u`.
   * Link yang **mati** dihapus dari playlist utama dan ditambahkan secara akumulatif (*append*) ke file `hapus.m3u` (tanpa duplikat baris).

2. **Pembuatan EPG Khusus (`generate_epg.py`):**
   * Membaca daftar channel aktif dari `ich-iptv.m3u`.
   * Mengunduh data EPG dari berbagai sumber publik yang terdaftar.
   * Mencocokkan nama channel menggunakan algoritma kemiripan teks, mengizinkan duplikasi sumber jika diperlukan agar jadwal lebih lengkap, lalu mengompres hasilnya menjadi `epg-ich.xml.gz`.

3. **Penyimpanan Otomatis (`Commit & Push`):**
   * GitHub Actions mendeteksi perubahan pada file `ich-iptv.m3u`, `hapus.m3u`, dan `epg-ich.xml.gz`, lalu menyimpannya kembali ke repository secara otomatis.

---

## 🚀 Cara Penggunaan di Aplikasi IPTV

Gunakan tautan *Raw* dari file berikut pada aplikasi pemutar IPTV Anda:
* **Link Playlist:** Mengarah ke file `ich-iptv.m3u`
* **Link EPG:** Mengarah ke file `epg-ich.xml.gz`
