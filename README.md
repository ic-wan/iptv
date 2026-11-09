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

  📁 Grup: [Kids] (4 Channel)
  ----------------------------------------
    1. Baby shark tv (720p)
    2. Kidsflix (1080p) [not 24/7]
    3. Moonbug kids (1080p)
    4. Pbs kids

  📁 Grup: [Lokal] (35 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banyumas tv (720p) [not 24/7]
    3. Bn channel (720p)
    4. Caruban tv (1080p)
    5. Dens tv learning
    6. Dhamma tv (720p) [not 24/7]
    7. Duta tv (360p) [not 24/7]
    8. Efarina tv (720p)
    9. Indonesiana tv
    10. Jawa pos tv jakarta (720p)
    11. Jogja istimewa tv (720p)
    12. Jowo
    13. Kawanua tv (720p)
    14. Kompas tv
    15. Madu tv (576p)
    16. Moji tv
    17. Mqtv (720p) [not 24/7]
    18. Nhk world japan
    19. Padang tv (720p) [not 24/7]
    20. Pontv (720p)
    21. R tv
    22. Radar tasikmalaya tv (720p) [not 24/7]
    23. Radio kita tv (1080p)
    24. Salira tv (720p)
    25. Smtv (720p) [not 24/7]
    26. Stara tv (720p)
    27. Stara tv bandung (1080p)
    28. Stara tv cianjur (720p)
    29. Stara tv malang (1080p)
    30. Tatv (720p) [not 24/7]
    31. Tv one
    32. Tv tabalong (720p) [not 24/7]
    33. Tv9 nusantara (720p)
    34. Tvri jawa barat (480p)
    35. Tvri world

  📁 Grup: [Lokal (auto)] (147 Channel)
  ----------------------------------------
    1. 24 Horas (720p)
    2. 24 Канал (1080p)
    3. A Spor SD (1080p)
    4. ABC Australia
    5. ANTV HD
    6. AXN Asia Indonesia
    7. Aathavan TV (720p)
    8. Abadan
    9. Ahsan TV
    10. Ajman TV (1080p)
    11. Al Qamar TV (1080p)
    12. An Ninh TV HD (1080p)
    13. Anadolu Net TV (1080p)
    14. Angel TV Indonesia (720p)
    15. Ashiil TV (480p)
    16. Atomic Academy TV (480p)
    17. Atomic TV (360p)
    18. Azan TV
    19. BBC LIFESTYLE
    20. BN Channel (ChannelFeed)
    21. BRTV (720p)
    22. BTV (Channel Feed)
    23. BTV (V+)
    24. Baan Baan TV 73
    25. Balapan HD (1080p)
    26. Balapan International (1080p)
    27. Balikpapan TV (720p)
    28. Banjar TV (720p) [Not 24/7]
    29. Banten TV
    30. Batam TV (480p) [Not 24/7]
    31. Berita Satu
    32. Berita Satu (DensTV)
    33. Bungo TV
    34. CNBC Indonesia
    35. CNBC Indonesia (ChannelFeed)
    36. CNN Indonesia
    37. CTV Dla Ciebie TV
    38. Cao Bằng TV (720p)
    39. Clan Internacional Americas (1080p) [Geo-blocked]
    40. DAAI TV
    41. DAAI TV (Dens)
    42. DMI TV (576i)
    43. Dhoho TV
    44. EmanTv (1080p)
    45. Fajar TV (720p) [Not 24/7]
    46. Fashion TV
    47. Garuda TV (1080p)
    48. Garuda TV (Flashcon)
    49. Hmong Star TV (720p) [Not 24/7]
    50. Hyder TV (720p)
    51. IDX (V+)
    52. Indosiar HD
    53. Inter TV (1080p)
    54. Iunior TV (1080p)
    55. JTV (720p)
    56. JTV Kediri (1080p) [Not 24/7]
    57. JTV Madiun
    58. JTV Malang
    59. Jagantara TV
    60. Kordia TV (1080p)
    61. La 2
    62. Lingkar TV
    63. Love the Planet (1080p)
    64. MAGNA Channel (DensTV)
    65. MAGNA TV (ChannelFeed)
    66. MBG TV (1080p)
    67. MDTV (DensTV)
    68. MOJI TV HD (Alt 3 - DensTV flashcon)
    69. MTV Ridiculousness
    70. MTV Ridiculousness (United States) LatAm (720p)
    71. Madani TV (720p)
    72. Magna Channel (1080p)
    73. Metro TV
    74. MetroTV (DensTV)
    75. MetroTV (Flashcon)
    76. Myanmar International TV
    77. Nusantara TV (ChannelFeed)
    78. Omid e Iran TV
    79. PKTV (480p)
    80. Peer TV Sudtirol (1080p)
    81. RCTV (Indonesia) (720p) [Not 24/7]
    82. Radar Lampung TV (480p)
    83. Radio 51 TV
    84. Rajawali TV
    85. Riau TV (1080p) [Not 24/7]
    86. Rinjani TV
    87. SCTV HD
    88. SMTV (720p)
    89. STV (Indonesia) (720p) [Not 24/7]
    90. Salam TV (720p)
    91. Sangaji TV (720p)
    92. SindoNews
    93. SindoNews (V+)
    94. Sriwijaya TV (720p) [Not 24/7]
    95. Stara TV Bojonegoro (720p)
    96. Stara TV Jakarta (1080p)
    97. Stara TV Parahyangan (720p)
    98. TLC HD
    99. TVE Internacional America (576p) [Geo-blocked]
    100. TVE Star (576p)
    101. TVE Star HD (1080p)
    102. TVRI
    103. TVRI (1080i)
    104. TVRI Aceh (720p)
    105. TVRI Bali (480p)
    106. TVRI Bangka Belitung (480p)
    107. TVRI Bengkulu (480p)
    108. TVRI Gorontalo (480p)
    109. TVRI Jakarta (576i) [Not 24/7]
    110. TVRI Jambi (720p) [Not 24/7]
    111. TVRI Jawa Tengah (720p)
    112. TVRI Jawa Timur (720p)
    113. TVRI Kalimantan Barat (480p)
    114. TVRI Kalimantan Selatan (720p)
    115. TVRI Kalimantan Tengah (480p)
    116. TVRI Kalimantan Timur (720p)
    117. TVRI Lampung (720p)
    118. TVRI Maluku (480p)
    119. TVRI North Sulawesi (1080p)
    120. TVRI North Sumatra (1080p)
    121. TVRI Nusa Tenggara Barat (720p)
    122. TVRI Nusa Tenggara Timur (480p)
    123. TVRI Papua (480p)
    124. TVRI Riau
    125. TVRI Riau (720p) [Not 24/7]
    126. TVRI Sulawesi Barat (720p)
    127. TVRI Sulawesi Selatan (480p)
    128. TVRI Sulawesi Tengah (720p)
    129. TVRI Sulawesi Tenggara (480p)
    130. TVRI Sumatera Barat (720p)
    131. TVRI Sumatera Selatan (480p)
    132. TVRI West Papua (1080p)
    133. TVRI Yogyakarta (720p)
    134. The Indonesia Channel (1080p)
    135. Trans7 (Transcorp)
    136. Trans7 HD
    137. TransTV (Transcorp)
    138. TransTV HD
    139. Tropical Moon Urban TV [Not 24/7]
    140. U Channel
    141. UGTV (720p)
    142. VTV
    143. Vision Prime (V+)
    144. Warner TV
    145. Warner TV Asia (720p)
    146. iNews HD
    147. Хузур ТВ (1080p) [Not 24/7]

  📁 Grup: [Radio] (3 Channel)
  ----------------------------------------
    1. Prambors fm
    2. Rodja fm
    3. The rockin life (indirect)

  📁 Grup: [Travels] (4 Channel)
  ----------------------------------------
    1. Dronetv (1080p)
    2. Intravel (1080p)
    3. Travel escapes (1080p)
    4. Travel tv (576p)

  📁 Grup: [Youtube Music] (1 Channel)
  ----------------------------------------
    1. YouTube Stream (DNL6Wy6IstE)

=============================================
```
<!-- END_PROGRAM_LIST -->
