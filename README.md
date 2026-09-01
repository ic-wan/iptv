# IPTV Playlist & EPG Automation 
# [ INDONESIAN CHANNEL ]

Sistem otomatisasi pembaruan playlist IPTV dan EPG Indonesia yang berjalan secara terpadu menggunakan GitHub Actions.

## 🚀 Arsitektur Pipeline

1. **Grabber Pintar & Filter Keyword (`grab_indo_m3u.py`)**
   - Mengambil tautan sumber M3U mentah yang terdaftar di `m3u_source.txt`.
   - Menyaring channel lokal berdasarkan daftar kata kunci fleksibel di `keyword.txt`.
   - Menyeragamkan atribut grup secara bersih menjadi `Lokal (auto)` dan mencegah duplikasi URL.

2. **Pengecek Link 2-Level & Pemulihan (`check_m3u.py`)**
   - **Level 1 (Quick Check):** Memastikan server merespons dengan status HTTP `200 OK`.
   - **Level 2 (Deep Check):** Memeriksa isi payload stream `.m3u8` agar bebas dari halaman error atau blokir.
   - Memindahkan link mati ke `hapus.m3u` serta otomatis memulihkan (*revival*) link yang kembali aktif.

3. **Penyaring Blacklist Global (`apply_blacklist.py`)**
   - Membersihkan channel yang terdaftar di dalam daftar blokir (`blacklist_program.txt`) dari playlist utama maupun arsip link mati.

4. **Generator Laporan Program (`generate_program_list.py`)**
   - Membuat laporan rekapitulasi terstruktur per kategori ke dalam file `List_program.txt`.

5. **Otomatisasi GitHub Actions (`update-m3u-epg.yml`)**
   - Menjalankan seluruh rangkaian skrip secara otomatis setiap hari sekali pada pukul 09:00 WIB (02:00 UTC) atau via tombol *Run workflow* manual.

---

## 📁 Struktur File Repository

- `List_program.txt` — Laporan rekapitulasi daftar channel dan grup.
- `keyword.txt` — Konfigurasi kata kunci pencarian channel.
- `blacklist_program.txt` — Daftar hitam channel/program yang ingin diabaikan.
- `m3u_source.txt` — Daftar tautan sumber M3U eksternal.
- `youtube_source.txt` — Daftar tautan sumber playlist/live stream YouTube.
- `epg_source.txt` — Daftar tautan atau sumber data EPG eksternal.
- 
---

## 🚀 Cara Penggunaan di Aplikasi IPTV

Salin tautan *Raw* dari file berikut untuk dimasukkan ke aplikasi pemutar IPTV Anda (seperti TiviMate, OTT Navigator, dll.):
* **Link Playlist Utama (`ich-iptv.m3u`):** Cukup masukkan link ini ke aplikasi, maka daftar channel dan EPG akan otomatis tersinkronisasi.
  *https://raw.githubusercontent.com/ic-wan/iptv/refs/heads/main/ich-iptv.m3u*
  
* **Link EPG Utama (`epg-ich.xml.gz`):** Dapat digunakan secara terpisah apabila aplikasi IPTV Anda memerlukan pengaturan EPG secara manual.
  *https://raw.githubusercontent.com/ic-wan/iptv/main/epg-ich.xml.gz*


---

## 📺 Daftar Channel Aktif & Rekap Program


> *Catatan: Daftar di bawah ini diperbarui secara otomatis oleh sistem.*

<!-- START_PROGRAM_LIST -->
```text
========================================
 DAFTAR PROGRAM / CHANNEL IPTV
========================================

📂 SUMBER FILE: Playlist Utama (ich-iptv.m3u)
=============================================

  📁 Grup: [Adhimix] (3 Channel)
  ----------------------------------------
    1. Adhimix (360p)
    2. Adhimix (720p)
    3. Indonesia raya

  📁 Grup: [Entertainment] (1 Channel)
  ----------------------------------------
    1. Just for laughs gags (720p)

  📁 Grup: [Indihome] (8 Channel)
  ----------------------------------------
    1. Berita satu
    2. I news
    3. Jtv
    4. Kompas tv
    5. Max sport
    6. Prambors tv
    7. Rtv
    8. Sctv

  📁 Grup: [Kids] (8 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Biznet kids (1080p)
    4. Kidsflix (1080p) [not 24/7]
    5. Moonbug kids (1080p)
    6. Nickelodeon
    7. Pbs kids
    8. Vtv (720p)

  📁 Grup: [Lokal] (51 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banten tv (720p) [not 24/7]
    3. Banyumas tv (720p) [not 24/7]
    4. Batam tv (480p) [not 24/7]
    5. Biznet adventure (1080p)
    6. Biznet lifestyle (1080p)
    7. Bn channel (720p)
    8. Brtv (720p)
    9. Bungo tv (480p) [not 24/7]
    10. Caruban tv (1080p)
    11. Daai tv
    12. Dens tv learning
    13. Dhamma tv (720p) [not 24/7]
    14. Duta tv (360p) [not 24/7]
    15. Efarina tv (720p)
    16. Garuda tv (1080p)
    17. Indonesiana tv
    18. Izzah tv (480p)
    19. Jawa pos tv jakarta (720p)
    20. Jogja istimewa tv (720p)
    21. Jogja tv (720p) [not 24/7]
    22. Jowo
    23. Jtv (480p)
    24. Kawanua tv (720p)
    25. Kompas tv
    26. Lingkar tv
    27. Madani tv (720p)
    28. Madu tv (576p)
    29. Magna channel (1080p) [not 24/7]
    30. Metro tv
    31. Moji tv
    32. Mqtv (720p) [not 24/7]
    33. Nhk world japan
    34. Pontv (720p)
    35. R tv
    36. Rodja tv (720p)
    37. Rri net (1080p)
    38. Salira tv (720p)
    39. Smtv (720p) [not 24/7]
    40. Stara tv (720p)
    41. Stara tv bandung (1080p)
    42. Stara tv cianjur (720p)
    43. Stara tv malang (1080p)
    44. Tv one
    45. Tv tabalong (720p) [not 24/7]
    46. Tv9 nusantara (720p)
    47. Tvku (720p)
    48. Tvri jawa barat (480p)
    49. Tvri jawa timur (720p)
    50. Tvri world
    51. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (110 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ANTV HD
    3. Abadan
    4. Ahsan TV
    5. Ajwa TV (1080p)
    6. Al Qamar TV (1080p)
    7. Anadolu Net TV (1080p)
    8. Angel TV Indonesia (720p)
    9. Ashiil TV (480p)
    10. Astro Blitar TV (720p)
    11. Atomic Academy TV (480p)
    12. Atomic TV (360p)
    13. Azan TV
    14. BALI TV
    15. BBC LIFESTYLE
    16. BN Channel (ChannelFeed)
    17. Baan Baan TV 73
    18. Balapan HD (1080p)
    19. Balikpapan TV (720p)
    20. CBC (576p)
    21. CBC Drama (576p)
    22. CBC Sofra (576p)
    23. Canal 24 Horas (720p)
    24. Cao Bằng TV (720p)
    25. Clan Internacional Americas (1080p) [Geo-blocked]
    26. DMI TV (576i)
    27. EmanTv (1080p)
    28. Food Travel (V+)
    29. Garuda TV (Flashcon)
    30. Hmong Star TV (720p) [Not 24/7]
    31. Hyder TV (720p)
    32. I Am Channel (576p)
    33. Indosiar
    34. Indosiar HD
    35. Inter TV (1080p)
    36. Iunior TV (1080p)
    37. JAKTV
    38. JTV Kediri (1080p) [Not 24/7]
    39. JTV Madiun
    40. JTV Malang
    41. Kordia TV (1080p)
    42. La 2
    43. Libya Al Ahrar TV (1080p)
    44. Love the Planet (1080p)
    45. MAGNA Channel (Flashcon)
    46. MAGNA TV (ChannelFeed)
    47. MBG TV (1080p)
    48. MDTV
    49. MOJI TV HD (Alt 3 - DensTV flashcon)
    50. MTV Ridiculousness
    51. MTV Ridiculousness (720p)
    52. Matrix TV Yogyakarta (720p)
    53. Metro TV
    54. MetroTV (Flashcon)
    55. Outdoor Channel (1080p)
    56. PKTV (480p)
    57. Radar Lampung TV (480p)
    58. Radio 51 TV
    59. Rajawali TV
    60. Riau TV (1080p) [Not 24/7]
    61. SCTV (DASH/MPD)
    62. SCTV HD
    63. SMTV (720p)
    64. Salam TV (720p)
    65. Sangaji TV (720p)
    66. SindoNews
    67. Sooriyan TV (1080p)
    68. Stara TV Bojonegoro (720p)
    69. Stara TV Jakarta (1080p)
    70. Stara TV Parahyangan (720p)
    71. Surau TV (720p)
    72. TV Mu (720p) [Not 24/7]
    73. TVE Star (576p)
    74. TVE Star HD (1080p)
    75. TVRI (1080i)
    76. TVRI Aceh (720p)
    77. TVRI Bali (480p)
    78. TVRI Bangka Belitung (480p)
    79. TVRI Bengkulu (480p)
    80. TVRI Gorontalo (480p)
    81. TVRI Jakarta (576i) [Not 24/7]
    82. TVRI Jambi (720p) [Not 24/7]
    83. TVRI Jawa Tengah (720p)
    84. TVRI Kalimantan Barat (480p)
    85. TVRI Kalimantan Selatan (720p)
    86. TVRI Kalimantan Tengah (480p)
    87. TVRI Kalimantan Timur (720p)
    88. TVRI Lampung (720p)
    89. TVRI Maluku (480p)
    90. TVRI North Sulawesi (1080p)
    91. TVRI North Sumatra (1080p)
    92. TVRI Nusa Tenggara Barat (720p)
    93. TVRI Nusa Tenggara Timur (480p)
    94. TVRI Papua (480p)
    95. TVRI Riau
    96. TVRI Riau (720p) [Not 24/7]
    97. TVRI Sulawesi Barat (720p)
    98. TVRI Sulawesi Selatan (480p)
    99. TVRI Sulawesi Tengah (720p)
    100. TVRI Sulawesi Tenggara (480p)
    101. TVRI Sumatera Barat (720p)
    102. TVRI Sumatera Selatan (480p)
    103. TVRI WORLD
    104. TVRI West Papua (1080p)
    105. TVRI Yogyakarta (720p)
    106. The Indonesia Channel (1080p)
    107. U Channel
    108. UCL (720p)
    109. VTV HD (1080p)
    110. Хузур ТВ (1080p) [Not 24/7]

  📁 Grup: [Radio] (4 Channel)
  ----------------------------------------
    1. Prambors fm
    2. Rodja fm
    3. The rockin life
    4. The rockin life (indirect)

  📁 Grup: [Travels] (5 Channel)
  ----------------------------------------
    1. China travel (1080p)
    2. Dronetv (1080p)
    3. Intravel (1080p)
    4. Travel escapes (1080p)
    5. Travel tv (576p)

  📁 Grup: [Youtube Music] (1 Channel)
  ----------------------------------------
    1. YouTube Stream (DNL6Wy6IstE)

=============================================
```
<!-- END_PROGRAM_LIST -->
