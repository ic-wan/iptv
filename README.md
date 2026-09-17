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

  📁 Grup: [Kids] (6 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Kidsflix (1080p) [not 24/7]
    4. Moonbug kids (1080p)
    5. Pbs kids
    6. Vtv (720p)

  📁 Grup: [Lokal] (46 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banten tv (720p) [not 24/7]
    3. Banyumas tv (720p) [not 24/7]
    4. Bn channel (720p)
    5. Caruban tv (1080p)
    6. Daai tv
    7. Dens tv learning
    8. Dhamma tv (720p) [not 24/7]
    9. Dhoho tv (720p)
    10. Duta tv (360p) [not 24/7]
    11. Efarina tv (720p)
    12. Garuda tv (1080p)
    13. Indonesiana tv
    14. Jawa pos tv jakarta (720p)
    15. Jogja istimewa tv (720p)
    16. Jogja tv (720p) [not 24/7]
    17. Jowo
    18. Jtv (480p)
    19. Kawanua tv (720p)
    20. Kompas tv
    21. Madu tv (576p)
    22. Magna channel (1080p) [not 24/7]
    23. Metro tv
    24. Moji tv
    25. Mqtv (720p) [not 24/7]
    26. Nhk world japan
    27. Padang tv (720p) [not 24/7]
    28. Pontv (720p)
    29. R tv
    30. Radar tasikmalaya tv (720p) [not 24/7]
    31. Rodja tv (720p)
    32. Rri net (1080p)
    33. Salira tv (720p)
    34. Smtv (720p) [not 24/7]
    35. Stara tv (720p)
    36. Stara tv bandung (1080p)
    37. Stara tv cianjur (720p)
    38. Stara tv malang (1080p)
    39. Tatv (720p) [not 24/7]
    40. Tv one
    41. Tv tabalong (720p) [not 24/7]
    42. Tv9 nusantara (720p)
    43. Tvri jawa barat (480p)
    44. Tvri jawa timur (720p)
    45. Tvri world
    46. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (125 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ANTV HD
    3. Abadan
    4. Ahsan TV
    5. Ajman TV (1080p)
    6. Al Qamar TV (1080p)
    7. Angel TV Indonesia (720p)
    8. Ashiil TV (480p)
    9. Astro Blitar TV (720p)
    10. Atomic Academy TV (480p)
    11. Atomic TV (360p)
    12. Azan TV
    13. BALI TV
    14. BBC LIFESTYLE
    15. BN Channel (ChannelFeed)
    16. BRTV (720p)
    17. BTV (Channel Feed)
    18. BTV (V+)
    19. Balapan HD (1080p)
    20. Balikpapan TV (720p)
    21. Banjar TV (720p) [Not 24/7]
    22. Batam TV (480p) [Not 24/7]
    23. Berita Satu
    24. Bungo TV
    25. CNBC Indonesia (ChannelFeed)
    26. CNN Indonesia (ChannelFeed)
    27. Canal 24 Horas (720p)
    28. Cao Bằng TV (720p)
    29. Clan Internacional Americas (1080p) [Geo-blocked]
    30. DAAI TV (Dens)
    31. DMI TV (576i)
    32. EmanTv (1080p)
    33. Fajar TV (720p) [Not 24/7]
    34. Ficom Channel
    35. Food Travel (V+)
    36. Garuda TV (Flashcon)
    37. Hmong Star TV (720p) [Not 24/7]
    38. Hyder TV (720p)
    39. I Am Channel (576p)
    40. Indosiar
    41. Indosiar HD
    42. Inter TV (1080p)
    43. Iunior TV (1080p)
    44. JAKTV
    45. JTV Kediri (1080p) [Not 24/7]
    46. JTV Madiun
    47. JTV Malang
    48. Jagantara TV
    49. Kordia TV (1080p)
    50. La 2
    51. Lingkar TV
    52. Love the Planet (1080p)
    53. MAGNA Channel (Flashcon)
    54. MAGNA TV (ChannelFeed)
    55. MBG TV (1080p)
    56. MDTV
    57. MOJI TV HD (Alt 3 - DensTV flashcon)
    58. MTV Ridiculousness
    59. MTV Ridiculousness (720p)
    60. Madani TV (720p)
    61. Matrix TV Yogyakarta (720p)
    62. Metro TV
    63. MetroTV (Flashcon)
    64. Myanmar International TV
    65. Nusantara TV (ChannelFeed)
    66. Outdoor Channel (1080p)
    67. PKTV (480p)
    68. Radar Lampung TV (480p)
    69. Radio 51 TV
    70. Riau TV (1080p) [Not 24/7]
    71. Rinjani TV
    72. SCTV (DASH/MPD)
    73. SCTV HD
    74. SMTV (720p)
    75. Salam TV (720p)
    76. Sangaji TV (720p)
    77. SindoNews
    78. Sooriyan TV (1080p)
    79. Sriwijaya TV (720p) [Not 24/7]
    80. Stara TV Bojonegoro (720p)
    81. Stara TV Jakarta (1080p)
    82. Stara TV Parahyangan (720p)
    83. TV Mu (720p) [Not 24/7]
    84. TVE Star (576p)
    85. TVE Star HD (1080p)
    86. TVRI (1080i)
    87. TVRI Aceh (720p)
    88. TVRI Bali (480p)
    89. TVRI Bangka Belitung (480p)
    90. TVRI Bengkulu (480p)
    91. TVRI Gorontalo (480p)
    92. TVRI Jakarta (576i) [Not 24/7]
    93. TVRI Jambi (720p) [Not 24/7]
    94. TVRI Jawa Tengah (720p)
    95. TVRI Kalimantan Barat (480p)
    96. TVRI Kalimantan Selatan (720p)
    97. TVRI Kalimantan Tengah (480p)
    98. TVRI Kalimantan Timur (720p)
    99. TVRI Lampung (720p)
    100. TVRI Maluku (480p)
    101. TVRI North Sulawesi (1080p)
    102. TVRI North Sumatra (1080p)
    103. TVRI Nusa Tenggara Barat (720p)
    104. TVRI Nusa Tenggara Timur (480p)
    105. TVRI Papua (480p)
    106. TVRI Riau
    107. TVRI Riau (720p) [Not 24/7]
    108. TVRI Sulawesi Barat (720p)
    109. TVRI Sulawesi Selatan (480p)
    110. TVRI Sulawesi Tengah (720p)
    111. TVRI Sulawesi Tenggara (480p)
    112. TVRI Sumatera Barat (720p)
    113. TVRI Sumatera Selatan (480p)
    114. TVRI WORLD
    115. TVRI West Papua (1080p)
    116. TVRI Yogyakarta (720p)
    117. The Indonesia Channel (1080p)
    118. Timor TV
    119. Trans7 HD
    120. TransTV HD
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
