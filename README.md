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

  📁 Grup: [Kids] (7 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Biznet kids (1080p)
    4. Kidsflix (1080p) [not 24/7]
    5. Moonbug kids (1080p)
    6. Pbs kids
    7. Vtv (720p)

  📁 Grup: [Lokal] (54 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banten tv (720p) [not 24/7]
    3. Banyumas tv (720p) [not 24/7]
    4. Biznet adventure (1080p)
    5. Biznet lifestyle (1080p)
    6. Bn channel (720p)
    7. Brtv (720p)
    8. Caruban tv (1080p)
    9. Daai tv
    10. Dens tv learning
    11. Dhamma tv (720p) [not 24/7]
    12. Dhoho tv (720p)
    13. Duta tv (360p) [not 24/7]
    14. Efarina tv (720p)
    15. Garuda tv (1080p)
    16. Indonesiana tv
    17. Izzah tv (480p)
    18. Jawa pos tv jakarta (720p)
    19. Jogja istimewa tv (720p)
    20. Jogja tv (720p) [not 24/7]
    21. Jowo
    22. Jtv (480p)
    23. Kawanua tv (720p)
    24. Kompas tv
    25. Lingkar tv
    26. Madani tv (720p)
    27. Madu tv (576p)
    28. Magna channel (1080p) [not 24/7]
    29. Metro tv
    30. Moji tv
    31. Mqtv (720p) [not 24/7]
    32. Nhk world japan
    33. Padang tv (720p) [not 24/7]
    34. Pontv (720p)
    35. R tv
    36. Radar tasikmalaya tv (720p) [not 24/7]
    37. Radio kita tv (1080p)
    38. Rodja tv (720p)
    39. Rri net (1080p)
    40. Salira tv (720p)
    41. Smtv (720p) [not 24/7]
    42. Stara tv (720p)
    43. Stara tv bandung (1080p)
    44. Stara tv cianjur (720p)
    45. Stara tv malang (1080p)
    46. Tatv (720p) [not 24/7]
    47. Tv one
    48. Tv tabalong (720p) [not 24/7]
    49. Tv9 nusantara (720p)
    50. Tvku (720p)
    51. Tvri jawa barat (480p)
    52. Tvri jawa timur (720p)
    53. Tvri world
    54. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (125 Channel)
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
    11. Atomic Academy TV (480p)
    12. Atomic TV (360p)
    13. Azan TV
    14. BALI TV
    15. BBC LIFESTYLE
    16. BN Channel (ChannelFeed)
    17. BTV (Channel Feed)
    18. BTV (V+)
    19. Baan Baan TV 73
    20. Balapan HD (1080p)
    21. Balikpapan TV (720p)
    22. Banjar TV (720p) [Not 24/7]
    23. Batam TV (480p) [Not 24/7]
    24. Berita Satu
    25. Bungo TV
    26. CBC (576p)
    27. CBC Drama (576p)
    28. CBC Sofra (576p)
    29. Canal 24 Horas (720p)
    30. Cao Bằng TV (720p)
    31. Clan Internacional Americas (1080p) [Geo-blocked]
    32. DAAI TV (Dens)
    33. DMI TV (576i)
    34. Davika TV (480p)
    35. EmanTv (1080p)
    36. Fajar TV (720p) [Not 24/7]
    37. Ficom Channel
    38. Food Travel (V+)
    39. Garuda TV (Flashcon)
    40. Hmong Star TV (720p) [Not 24/7]
    41. Hyder TV (720p)
    42. I Am Channel (576p)
    43. Indosiar
    44. Indosiar HD
    45. Inter TV (1080p)
    46. Iunior TV (1080p)
    47. JAKTV
    48. JTV Kediri (1080p) [Not 24/7]
    49. JTV Madiun
    50. JTV Malang
    51. Jagantara TV
    52. Kordia TV (1080p)
    53. La 2
    54. Libya Al Ahrar TV (1080p)
    55. Love the Planet (1080p)
    56. MAGNA Channel (Flashcon)
    57. MAGNA TV (ChannelFeed)
    58. MBG TV (1080p)
    59. MDTV
    60. MOJI TV HD (Alt 3 - DensTV flashcon)
    61. MTV Ridiculousness
    62. MTV Ridiculousness (720p)
    63. Madani TV (720p)
    64. Matrix TV Yogyakarta (720p)
    65. Metro TV
    66. MetroTV (Flashcon)
    67. Myanmar International TV
    68. Nusantara TV (ChannelFeed)
    69. Outdoor Channel (1080p)
    70. PKTV (480p)
    71. Radio 51 TV
    72. Rajawali TV
    73. Riau TV (1080p) [Not 24/7]
    74. Rinjani TV
    75. SCTV (DASH/MPD)
    76. SCTV HD
    77. SMTV (720p)
    78. Salam TV (720p)
    79. Sangaji TV (720p)
    80. SindoNews
    81. Sooriyan TV (1080p)
    82. Stara TV Bojonegoro (720p)
    83. Stara TV Jakarta (1080p)
    84. Stara TV Parahyangan (720p)
    85. TV Mu (720p) [Not 24/7]
    86. TVE Star (576p)
    87. TVE Star HD (1080p)
    88. TVRI (1080i)
    89. TVRI Aceh (720p)
    90. TVRI Bali (480p)
    91. TVRI Bangka Belitung (480p)
    92. TVRI Bengkulu (480p)
    93. TVRI Gorontalo (480p)
    94. TVRI Jakarta (576i) [Not 24/7]
    95. TVRI Jambi (720p) [Not 24/7]
    96. TVRI Jawa Tengah (720p)
    97. TVRI Kalimantan Barat (480p)
    98. TVRI Kalimantan Selatan (720p)
    99. TVRI Kalimantan Tengah (480p)
    100. TVRI Kalimantan Timur (720p)
    101. TVRI Lampung (720p)
    102. TVRI Maluku (480p)
    103. TVRI North Sulawesi (1080p)
    104. TVRI North Sumatra (1080p)
    105. TVRI Nusa Tenggara Barat (720p)
    106. TVRI Nusa Tenggara Timur (480p)
    107. TVRI Papua (480p)
    108. TVRI Riau
    109. TVRI Riau (720p) [Not 24/7]
    110. TVRI Sulawesi Barat (720p)
    111. TVRI Sulawesi Selatan (480p)
    112. TVRI Sulawesi Tengah (720p)
    113. TVRI Sulawesi Tenggara (480p)
    114. TVRI Sumatera Barat (720p)
    115. TVRI Sumatera Selatan (480p)
    116. TVRI WORLD
    117. TVRI West Papua (1080p)
    118. TVRI Yogyakarta (720p)
    119. The Indonesia Channel (1080p)
    120. Timor TV
    121. U Channel
    122. UCL (720p)
    123. dTVi
    124. iNews HD
    125. Хузур ТВ (1080p) [Not 24/7]

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
