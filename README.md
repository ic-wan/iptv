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

  📁 Grup: [Lokal] (55 Channel)
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
    14. Dhoho tv (720p)
    15. Duta tv (360p) [not 24/7]
    16. Efarina tv (720p)
    17. Garuda tv (1080p)
    18. Indonesiana tv
    19. Izzah tv (480p)
    20. Jawa pos tv jakarta (720p)
    21. Jogja istimewa tv (720p)
    22. Jogja tv (720p) [not 24/7]
    23. Jowo
    24. Jtv (480p)
    25. Kawanua tv (720p)
    26. Kompas tv
    27. Lingkar tv
    28. Madani tv (720p)
    29. Madu tv (576p)
    30. Magna channel (1080p) [not 24/7]
    31. Metro tv
    32. Moji tv
    33. Mqtv (720p) [not 24/7]
    34. Nhk world japan
    35. Padang tv (720p) [not 24/7]
    36. Pontv (720p)
    37. R tv
    38. Radar tasikmalaya tv (720p) [not 24/7]
    39. Radio kita tv (1080p)
    40. Rri net (1080p)
    41. Salira tv (720p)
    42. Smtv (720p) [not 24/7]
    43. Stara tv (720p)
    44. Stara tv bandung (1080p)
    45. Stara tv cianjur (720p)
    46. Stara tv malang (1080p)
    47. Tatv (720p) [not 24/7]
    48. Tv one
    49. Tv tabalong (720p) [not 24/7]
    50. Tv9 nusantara (720p)
    51. Tvku (720p)
    52. Tvri jawa barat (480p)
    53. Tvri jawa timur (720p)
    54. Tvri world
    55. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (120 Channel)
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
    12. Atambua TV (720p)
    13. Atomic Academy TV (480p)
    14. Atomic TV (360p)
    15. Azan TV
    16. BALI TV
    17. BBC LIFESTYLE
    18. BN Channel (ChannelFeed)
    19. Baan Baan TV 73
    20. Balapan HD (1080p)
    21. Balikpapan TV (720p)
    22. Banjar TV (720p) [Not 24/7]
    23. Batam TV (480p) [Not 24/7]
    24. Bungo TV
    25. CBC (576p)
    26. CBC Drama (576p)
    27. CBC Sofra (576p)
    28. Canal 24 Horas (720p)
    29. Cao Bằng TV (720p)
    30. Clan Internacional Americas (1080p) [Geo-blocked]
    31. DAAI TV (Dens)
    32. DMI TV (576i)
    33. Davika TV (480p)
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
    50. Kordia TV (1080p)
    51. La 2
    52. Libya Al Ahrar TV (1080p)
    53. Love the Planet (1080p)
    54. MAGNA Channel (Flashcon)
    55. MAGNA TV (ChannelFeed)
    56. MBG TV (1080p)
    57. MDTV
    58. MOJI TV HD (Alt 3 - DensTV flashcon)
    59. MTV Ridiculousness
    60. MTV Ridiculousness (720p)
    61. Matrix TV Yogyakarta (720p)
    62. Metro TV
    63. MetroTV (Flashcon)
    64. Outdoor Channel (1080p)
    65. PKTV (480p)
    66. Radio 51 TV
    67. Rajawali TV
    68. Riau TV (1080p) [Not 24/7]
    69. Rinjani TV
    70. SCTV (DASH/MPD)
    71. SCTV HD
    72. Salam TV (720p)
    73. Sangaji TV (720p)
    74. SindoNews
    75. Sooriyan TV (1080p)
    76. Sriwijaya TV (720p) [Not 24/7]
    77. Stara TV Bojonegoro (720p)
    78. Stara TV Jakarta (1080p)
    79. Stara TV Parahyangan (720p)
    80. TV Mu (720p) [Not 24/7]
    81. TVE Star (576p)
    82. TVE Star HD (1080p)
    83. TVRI (1080i)
    84. TVRI Aceh (720p)
    85. TVRI Bali (480p)
    86. TVRI Bangka Belitung (480p)
    87. TVRI Bengkulu (480p)
    88. TVRI Gorontalo (480p)
    89. TVRI Jakarta (576i) [Not 24/7]
    90. TVRI Jambi (720p) [Not 24/7]
    91. TVRI Jawa Tengah (720p)
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
    118. dTVi
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
