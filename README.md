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

  📁 Grup: [Entertainment] (3 Channel)
  ----------------------------------------
    1. Just for laughs gags (720p)
    2. Pluto tv science
    3. Top gear

  📁 Grup: [INDONESIA] (1 Channel)
  ----------------------------------------
    1. Indonesia raya

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

  📁 Grup: [Kids] (11 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Biznet kids (1080p)
    4. Forever kids
    5. Kidsflix (1080p) [not 24/7]
    6. Lego kids tv
    7. Moonbug kids (1080p)
    8. Nick jr. pluto tv
    9. Nickelodeon
    10. Pbs kids
    11. Vtv (720p)

  📁 Grup: [Lokal] (56 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banten tv (720p) [not 24/7]
    3. Banyumas tv (720p) [not 24/7]
    4. Biznet adventure (1080p)
    5. Biznet lifestyle (1080p)
    6. Bn channel (720p)
    7. Brtv (720p)
    8. Bungo tv (480p) [not 24/7]
    9. Caruban tv (1080p)
    10. Cnbc hd
    11. Cnn 1 hd
    12. Cnn 2
    13. Daai tv
    14. Dens tv learning
    15. Dhamma tv (720p) [not 24/7]
    16. Dhoho tv (720p)
    17. Duta tv (360p) [not 24/7]
    18. Efarina tv (720p)
    19. Garuda tv (1080p)
    20. Indonesiana tv
    21. Izzah tv (480p)
    22. Jawa pos tv jakarta (720p)
    23. Jogja istimewa tv (720p)
    24. Jowo
    25. Jtv (480p)
    26. Kawanua tv (720p)
    27. Kompas tv
    28. Ktv (720p)
    29. Lingkar tv
    30. Madani tv (720p)
    31. Madu tv (576p)
    32. Magna channel (1080p) [not 24/7]
    33. Metro tv
    34. Moji tv
    35. Mqtv (720p) [not 24/7]
    36. Nhk world japan
    37. Padang tv (720p) [not 24/7]
    38. Pontv (720p)
    39. R tv
    40. Radio kita tv (1080p)
    41. Rodja tv (720p)
    42. Rri net (1080p)
    43. Salira tv (720p)
    44. Smtv (720p) [not 24/7]
    45. Stara tv (720p)
    46. Stara tv bandung (1080p)
    47. Stara tv cianjur (720p)
    48. Stara tv malang (1080p)
    49. Timor tv (1080p)
    50. Tv tabalong (720p) [not 24/7]
    51. Tv9 nusantara (720p)
    52. Tvku (720p)
    53. Tvri jawa barat (480p)
    54. Tvri jawa timur (720p)
    55. Tvri world
    56. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (131 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ANTV HD (Alt 3 - DensTV flashcon)
    3. Abadan
    4. Ahsan TV
    5. Ajwa TV (1080p)
    6. Al Qamar TV (1080p)
    7. Al Quran Al Kareem TV (720p)
    8. Anadolu Net TV (1080p)
    9. Angel TV Indonesia (720p)
    10. Ashiil TV (480p)
    11. Astro Blitar TV (720p)
    12. Atambua TV (720p)
    13. Atomic Academy TV (480p)
    14. Atomic TV (360p)
    15. Aupur Television (1080p)
    16. Azan TV
    17. BALI TV
    18. BBC LIFESTYLE
    19. BIOSKOP INDONESIA
    20. BN Channel (ChannelFeed)
    21. Baan Baan TV 73
    22. Balapan HD (1080p)
    23. Balikpapan TV (720p)
    24. Batam TV (480p) [Not 24/7]
    25. CBC (576p)
    26. CBC Drama (576p)
    27. CBC Sofra (576p)
    28. CNBC Indonesia (ChannelFeed)
    29. CNN INDONESIA
    30. CNN INDONESIA HD
    31. CNN Indonesia (ChannelFeed)
    32. CNN https://live.cnnindonesia.com/livecnn/smil:cnntv.smil/playlist.m3u8
    33. Canal 24 Horas (720p)
    34. Cao Bằng TV (720p)
    35. Clan Internacional Americas (1080p) [Geo-blocked]
    36. DMI TV (576i)
    37. EmanTv (1080p)
    38. Ficom Channel
    39. Food Travel (V+)
    40. GTV
    41. Garuda TV (ChannelFeed)
    42. Garuda TV HD
    43. Hmong Star TV (720p) [Not 24/7]
    44. Hyder TV (720p)
    45. I Am Channel (576p)
    46. Indosiar
    47. Indosiar HD
    48. Inter TV (1080p)
    49. Iunior TV (1080p)
    50. JAKTV
    51. JTV Kediri (1080p) [Not 24/7]
    52. JTV Madiun
    53. JTV Malang
    54. Jogja TV (720p) [Not 24/7]
    55. Kompas TV HD (Alt 3 - DensTV flashcon)
    56. Kordia TV (1080p)
    57. La 2
    58. Libya Al Ahrar TV (1080p)
    59. Love the Planet (1080p)
    60. MAGNA TV (ChannelFeed)
    61. MBG TV (1080p)
    62. MDTV
    63. MDTV HD
    64. MTV Ridiculousness
    65. MTV Ridiculousness (720p)
    66. Matrix TV Yogyakarta (720p)
    67. Metro TV
    68. MetroTV (Flashcon)
    69. Music JapanTV
    70. Outdoor Channel (1080p)
    71. PKTV (480p)
    72. RCTI
    73. Radar Lampung TV (480p)
    74. Radio 51 TV
    75. Rajawali TV
    76. SCTV (DASH/MPD)
    77. SCTV HD (Alt 3 - DensTV flashcon)
    78. SMTV (720p)
    79. Salam TV (720p)
    80. Sangaji TV (720p)
    81. SindoNews
    82. Sooriyan TV (1080p)
    83. Sriwijaya TV (720p) [Not 24/7]
    84. Stara TV Bojonegoro (720p)
    85. Stara TV Jakarta (1080p)
    86. Stara TV Parahyangan (720p)
    87. Surau TV (720p)
    88. TV Mu (720p) [Not 24/7]
    89. TVE Star (576p)
    90. TVE Star HD (1080p)
    91. TVRI (1080i)
    92. TVRI Aceh (720p)
    93. TVRI Bali (480p)
    94. TVRI Bangka Belitung (480p)
    95. TVRI Bengkulu (480p)
    96. TVRI Gorontalo (480p)
    97. TVRI Jakarta (576i) [Not 24/7]
    98. TVRI Jambi (720p) [Not 24/7]
    99. TVRI Jawa Tengah (720p)
    100. TVRI Kalimantan Barat (480p)
    101. TVRI Kalimantan Selatan (720p)
    102. TVRI Kalimantan Tengah (480p)
    103. TVRI Kalimantan Timur (720p)
    104. TVRI Lampung (720p)
    105. TVRI Maluku (480p)
    106. TVRI North Sulawesi (1080p)
    107. TVRI North Sumatra (1080p)
    108. TVRI Nusa Tenggara Barat (720p)
    109. TVRI Nusa Tenggara Timur (480p)
    110. TVRI Papua (480p)
    111. TVRI Riau
    112. TVRI Riau (720p) [Not 24/7]
    113. TVRI Sulawesi Barat (720p)
    114. TVRI Sulawesi Selatan (480p)
    115. TVRI Sulawesi Tengah (720p)
    116. TVRI Sulawesi Tenggara (480p)
    117. TVRI Sumatera Barat (720p)
    118. TVRI Sumatera Selatan (480p)
    119. TVRI WORLD
    120. TVRI West Papua (1080p)
    121. TVRI World
    122. TVRI Yogyakarta (720p)
    123. The Indonesia Channel (1080p)
    124. Trans7 HD
    125. TransTV HD
    126. U Channel
    127. UCL (720p)
    128. VTV HD (1080p)
    129. group-title="Lokal (auto)"CNN TV https://live.cnnindonesia.com/livecnn/smil:cnntv.smil/chunklist_w1299546647_b384000_sleng.m3u8
    130. iNews
    131. Хузур ТВ (1080p) [Not 24/7]

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

  📁 Grup: [Uncategorized] (1 Channel)
  ----------------------------------------
    1. expired_YouTube Stream

=============================================
```
<!-- END_PROGRAM_LIST -->
