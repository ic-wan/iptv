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

  📁 Grup: [Lokal] (52 Channel)
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
    25. Madu tv (576p)
    26. Magna channel (1080p) [not 24/7]
    27. Metro tv
    28. Moji tv
    29. Mqtv (720p) [not 24/7]
    30. Nhk world japan
    31. Padang tv (720p) [not 24/7]
    32. Pontv (720p)
    33. R tv
    34. Radar tasikmalaya tv (720p) [not 24/7]
    35. Radio kita tv (1080p)
    36. Rodja tv (720p)
    37. Rri net (1080p)
    38. Salira tv (720p)
    39. Smtv (720p) [not 24/7]
    40. Stara tv (720p)
    41. Stara tv bandung (1080p)
    42. Stara tv cianjur (720p)
    43. Stara tv malang (1080p)
    44. Tatv (720p) [not 24/7]
    45. Tv one
    46. Tv tabalong (720p) [not 24/7]
    47. Tv9 nusantara (720p)
    48. Tvku (720p)
    49. Tvri jawa barat (480p)
    50. Tvri jawa timur (720p)
    51. Tvri world
    52. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (126 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ANTV HD
    3. ATV (1080p)
    4. Abadan
    5. Ahsan TV
    6. Ajman TV (1080p)
    7. Al Qamar TV (1080p)
    8. Anadolu Net TV (1080p)
    9. Angel TV Indonesia (720p)
    10. Ashiil TV (480p)
    11. Astro Blitar TV (720p)
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
    22. Balapan International (1080p)
    23. Balikpapan TV (720p)
    24. Banjar TV (720p) [Not 24/7]
    25. Batam TV (480p) [Not 24/7]
    26. Berita Satu
    27. Bungo TV
    28. CBC (576p)
    29. CBC Drama (576p)
    30. CBC Sofra (576p)
    31. Canal 24 Horas (720p)
    32. Cao Bằng TV (720p)
    33. Clan Internacional Americas (1080p) [Geo-blocked]
    34. DAAI TV (Dens)
    35. DMI TV (576i)
    36. Davika TV (480p)
    37. EmanTv (1080p)
    38. Fajar TV (720p) [Not 24/7]
    39. Ficom Channel
    40. Food Travel (V+)
    41. Garuda TV (Flashcon)
    42. Hmong Star TV (720p) [Not 24/7]
    43. Hyder TV (720p)
    44. I Am Channel (576p)
    45. Indosiar
    46. Indosiar HD
    47. Inter TV (1080p)
    48. Iunior TV (1080p)
    49. JAKTV
    50. JTV Kediri (1080p) [Not 24/7]
    51. JTV Madiun
    52. JTV Malang
    53. Jagantara TV
    54. Kordia TV (1080p)
    55. La 2
    56. Libya Al Ahrar TV (1080p)
    57. Love the Planet (1080p)
    58. MAGNA Channel (Flashcon)
    59. MAGNA TV (ChannelFeed)
    60. MBG TV (1080p)
    61. MDTV
    62. MOJI TV HD (Alt 3 - DensTV flashcon)
    63. MTV Ridiculousness
    64. MTV Ridiculousness (720p)
    65. Madani TV (720p)
    66. Matrix TV Yogyakarta (720p)
    67. Metro TV
    68. MetroTV (Flashcon)
    69. Nusantara TV (ChannelFeed)
    70. Outdoor Channel (1080p)
    71. PKTV (480p)
    72. Radio 51 TV
    73. Rajawali TV
    74. Riau TV (1080p) [Not 24/7]
    75. Rinjani TV
    76. SCTV (DASH/MPD)
    77. SCTV HD
    78. SMTV (720p)
    79. Salam TV (720p)
    80. Sangaji TV (720p)
    81. SindoNews
    82. Sooriyan TV (1080p)
    83. Sriwijaya TV (720p) [Not 24/7]
    84. Stara TV Jakarta (1080p)
    85. Stara TV Parahyangan (720p)
    86. TV Mu (720p) [Not 24/7]
    87. TVE Star (576p)
    88. TVE Star HD (1080p)
    89. TVRI (1080i)
    90. TVRI Aceh (720p)
    91. TVRI Bali (480p)
    92. TVRI Bangka Belitung (480p)
    93. TVRI Bengkulu (480p)
    94. TVRI Gorontalo (480p)
    95. TVRI Jakarta (576i) [Not 24/7]
    96. TVRI Jambi (720p) [Not 24/7]
    97. TVRI Jawa Tengah (720p)
    98. TVRI Kalimantan Barat (480p)
    99. TVRI Kalimantan Selatan (720p)
    100. TVRI Kalimantan Tengah (480p)
    101. TVRI Kalimantan Timur (720p)
    102. TVRI Lampung (720p)
    103. TVRI Maluku (480p)
    104. TVRI North Sulawesi (1080p)
    105. TVRI North Sumatra (1080p)
    106. TVRI Nusa Tenggara Barat (720p)
    107. TVRI Nusa Tenggara Timur (480p)
    108. TVRI Papua (480p)
    109. TVRI Riau
    110. TVRI Riau (720p) [Not 24/7]
    111. TVRI Sulawesi Barat (720p)
    112. TVRI Sulawesi Selatan (480p)
    113. TVRI Sulawesi Tengah (720p)
    114. TVRI Sulawesi Tenggara (480p)
    115. TVRI Sumatera Barat (720p)
    116. TVRI Sumatera Selatan (480p)
    117. TVRI WORLD
    118. TVRI West Papua (1080p)
    119. TVRI Yogyakarta (720p)
    120. The Indonesia Channel (1080p)
    121. Timor TV
    122. U Channel
    123. UCL (720p)
    124. dTVi
    125. iNews HD
    126. Хузур ТВ (1080p) [Not 24/7]

  📁 Grup: [Radio] (3 Channel)
  ----------------------------------------
    1. Prambors fm
    2. The rockin life
    3. The rockin life (indirect)

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
