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

  📁 Grup: [Lokal] (53 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banyumas tv (720p) [not 24/7]
    3. Biznet adventure (1080p)
    4. Biznet lifestyle (1080p)
    5. Bn channel (720p)
    6. Brtv (720p)
    7. Caruban tv (1080p)
    8. Daai tv
    9. Dens tv learning
    10. Dhamma tv (720p) [not 24/7]
    11. Dhoho tv (720p)
    12. Duta tv (360p) [not 24/7]
    13. Efarina tv (720p)
    14. Garuda tv (1080p)
    15. Indonesiana tv
    16. Izzah tv (480p)
    17. Jawa pos tv jakarta (720p)
    18. Jogja istimewa tv (720p)
    19. Jogja tv (720p) [not 24/7]
    20. Jowo
    21. Jtv (480p)
    22. Kawanua tv (720p)
    23. Kompas tv
    24. Lingkar tv
    25. Madani tv (720p)
    26. Madu tv (576p)
    27. Magna channel (1080p) [not 24/7]
    28. Metro tv
    29. Moji tv
    30. Mqtv (720p) [not 24/7]
    31. Nhk world japan
    32. Padang tv (720p) [not 24/7]
    33. Pontv (720p)
    34. R tv
    35. Radar tasikmalaya tv (720p) [not 24/7]
    36. Radio kita tv (1080p)
    37. Rodja tv (720p)
    38. Rri net (1080p)
    39. Salira tv (720p)
    40. Smtv (720p) [not 24/7]
    41. Stara tv (720p)
    42. Stara tv bandung (1080p)
    43. Stara tv cianjur (720p)
    44. Stara tv malang (1080p)
    45. Tatv (720p) [not 24/7]
    46. Tv one
    47. Tv tabalong (720p) [not 24/7]
    48. Tv9 nusantara (720p)
    49. Tvku (720p)
    50. Tvri jawa barat (480p)
    51. Tvri jawa timur (720p)
    52. Tvri world
    53. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (120 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ANTV HD
    3. Abadan
    4. Ahsan TV
    5. Ajman TV (1080p)
    6. Al Qamar TV (1080p)
    7. Anadolu Net TV (1080p)
    8. Angel TV Indonesia (720p)
    9. Ashiil TV (480p)
    10. Astro Blitar TV (720p)
    11. Atambua TV (720p)
    12. Atomic Academy TV (480p)
    13. Atomic TV (360p)
    14. Azan TV
    15. BALI TV
    16. BBC LIFESTYLE
    17. BN Channel (ChannelFeed)
    18. BTV (Channel Feed)
    19. BTV (V+)
    20. Baan Baan TV 73
    21. Balapan HD (1080p)
    22. Balikpapan TV (720p)
    23. Banjar TV (720p) [Not 24/7]
    24. Batam TV (480p) [Not 24/7]
    25. Berita Satu
    26. CBC (576p)
    27. CBC Drama (576p)
    28. CBC Sofra (576p)
    29. Canal 24 Horas (720p)
    30. Cao Bằng TV (720p)
    31. Clan Internacional Americas (1080p) [Geo-blocked]
    32. DAAI TV (Dens)
    33. DMI TV (576i)
    34. EmanTv (1080p)
    35. Fajar TV (720p) [Not 24/7]
    36. Ficom Channel
    37. Food Travel (V+)
    38. Garuda TV (Flashcon)
    39. Hmong Star TV (720p) [Not 24/7]
    40. Hyder TV (720p)
    41. I Am Channel (576p)
    42. Indosiar
    43. Indosiar HD
    44. Inter TV (1080p)
    45. Iunior TV (1080p)
    46. JAKTV
    47. JTV Kediri (1080p) [Not 24/7]
    48. JTV Madiun
    49. JTV Malang
    50. Jagantara TV
    51. Kordia TV (1080p)
    52. La 2
    53. Libya Al Ahrar TV (1080p)
    54. Love the Planet (1080p)
    55. MAGNA Channel (Flashcon)
    56. MAGNA TV (ChannelFeed)
    57. MBG TV (1080p)
    58. MOJI TV HD (Alt 3 - DensTV flashcon)
    59. MTV Ridiculousness
    60. MTV Ridiculousness (720p)
    61. Matrix TV Yogyakarta (720p)
    62. Metro TV
    63. MetroTV (Flashcon)
    64. Nusantara TV (ChannelFeed)
    65. Outdoor Channel (1080p)
    66. PKTV (480p)
    67. Radio 51 TV
    68. Rajawali TV
    69. Riau TV (1080p) [Not 24/7]
    70. Rinjani TV
    71. SCTV (DASH/MPD)
    72. SCTV HD
    73. SMTV (720p)
    74. Salam TV (720p)
    75. Sangaji TV (720p)
    76. SindoNews
    77. Sooriyan TV (1080p)
    78. Sriwijaya TV (720p) [Not 24/7]
    79. Stara TV Bojonegoro (720p)
    80. Stara TV Jakarta (1080p)
    81. Stara TV Parahyangan (720p)
    82. TV Mu (720p) [Not 24/7]
    83. TVE Star (576p)
    84. TVE Star HD (1080p)
    85. TVRI Aceh (720p)
    86. TVRI Bali (480p)
    87. TVRI Bangka Belitung (480p)
    88. TVRI Bengkulu (480p)
    89. TVRI Gorontalo (480p)
    90. TVRI Jakarta (576i) [Not 24/7]
    91. TVRI Jambi (720p) [Not 24/7]
    92. TVRI Kalimantan Barat (480p)
    93. TVRI Kalimantan Selatan (720p)
    94. TVRI Kalimantan Tengah (480p)
    95. TVRI Kalimantan Timur (720p)
    96. TVRI Lampung (720p)
    97. TVRI Maluku (480p)
    98. TVRI North Sulawesi (1080p)
    99. TVRI North Sumatra (1080p)
    100. TVRI Nusa Tenggara Barat (720p)
    101. TVRI Nusa Tenggara Timur (480p)
    102. TVRI Papua (480p)
    103. TVRI Riau
    104. TVRI Riau (720p) [Not 24/7]
    105. TVRI Sulawesi Barat (720p)
    106. TVRI Sulawesi Selatan (480p)
    107. TVRI Sulawesi Tengah (720p)
    108. TVRI Sulawesi Tenggara (480p)
    109. TVRI Sumatera Barat (720p)
    110. TVRI Sumatera Selatan (480p)
    111. TVRI WORLD
    112. TVRI West Papua (1080p)
    113. TVRI Yogyakarta (720p)
    114. The Indonesia Channel (1080p)
    115. Timor TV
    116. U Channel
    117. UCL (720p)
    118. Viasat Kino Action (576p)
    119. iNews HD
    120. Хузур ТВ (1080p) [Not 24/7]

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
