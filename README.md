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

  📁 Grup: [Kids] (5 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Kidsflix (1080p) [not 24/7]
    4. Moonbug kids (1080p)
    5. Pbs kids

  📁 Grup: [Lokal] (40 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banten tv (720p) [not 24/7]
    3. Banyumas tv (720p) [not 24/7]
    4. Bn channel (720p)
    5. Caruban tv (1080p)
    6. Dens tv learning
    7. Dhamma tv (720p) [not 24/7]
    8. Dhoho tv (720p)
    9. Duta tv (360p) [not 24/7]
    10. Indonesiana tv
    11. Izzah tv (480p)
    12. Jawa pos tv jakarta (720p)
    13. Jogja istimewa tv (720p)
    14. Jogja tv (720p) [not 24/7]
    15. Jowo
    16. Kawanua tv (720p)
    17. Kompas tv
    18. Madu tv (576p)
    19. Magna channel (1080p) [not 24/7]
    20. Metro tv
    21. Moji tv
    22. Mqtv (720p) [not 24/7]
    23. Nhk world japan
    24. Padang tv (720p) [not 24/7]
    25. Pontv (720p)
    26. R tv
    27. Radar tasikmalaya tv (720p) [not 24/7]
    28. Salira tv (720p)
    29. Smtv (720p) [not 24/7]
    30. Stara tv (720p)
    31. Stara tv bandung (1080p)
    32. Stara tv cianjur (720p)
    33. Stara tv malang (1080p)
    34. Tatv (720p) [not 24/7]
    35. Tv one
    36. Tv tabalong (720p) [not 24/7]
    37. Tv9 nusantara (720p)
    38. Tvri jawa barat (480p)
    39. Tvri world
    40. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (155 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV (720p)
    5. ANTV HD
    6. Abadan
    7. Ahsan TV
    8. Ajman TV (1080p)
    9. Al Qamar TV (1080p)
    10. Anadolu Net TV (1080p)
    11. Angel TV Indonesia (720p)
    12. Ashiil TV (480p)
    13. Astro Blitar TV (720p)
    14. Atomic Academy TV (480p)
    15. Atomic TV (360p)
    16. BBC LIFESTYLE
    17. BN Channel (ChannelFeed)
    18. BRTV (720p)
    19. BTV (Channel Feed)
    20. BTV (V+)
    21. Baan Baan TV 73
    22. Balapan HD (1080p)
    23. Balapan International (1080p)
    24. Bali TV
    25. Balikpapan TV (720p)
    26. Bandung TV
    27. Banjar TV (720p) [Not 24/7]
    28. Batam TV (480p) [Not 24/7]
    29. Berita Satu
    30. Bungo TV
    31. CNBC Indonesia (ChannelFeed)
    32. CNN Indonesia (ChannelFeed)
    33. Canal 24 Horas (720p)
    34. Cao Bằng TV (720p)
    35. CelebritiesTV (V+)
    36. Clan Internacional Americas (1080p) [Geo-blocked]
    37. DAAI TV
    38. DAAI TV (Dens)
    39. DMI TV (576i)
    40. EmanTv (1080p)
    41. Entertainment (V+)
    42. Fashion TV
    43. Food Travel (V+)
    44. GTV
    45. GTV (Indonesia) HD (1080p)
    46. Garuda TV (1080p)
    47. Garuda TV (Flashcon)
    48. Hanacaraka TV (V+)
    49. Hmong Star TV (720p) [Not 24/7]
    50. Hyder TV (720p)
    51. I Am Channel (576p)
    52. IDX (V+)
    53. Indonesia Movie Channel (V+)
    54. Indosiar HD
    55. Indosiar HD (1080p)
    56. Inter TV (1080p)
    57. Iunior TV (1080p)
    58. JTV (720p)
    59. JTV (V+)
    60. JTV Kediri (1080p) [Not 24/7]
    61. JTV Madiun
    62. JTV Madura (480p) [Not 24/7]
    63. JTV Malang
    64. Jagantara TV
    65. Kordia TV (1080p)
    66. La 2
    67. Love the Planet (1080p)
    68. MAGNA Channel (DensTV)
    69. MAGNA TV (ChannelFeed)
    70. MBG TV (1080p)
    71. MDTV
    72. MDTV (DensTV)
    73. MNCTV HD
    74. MOJI TV HD (Alt 3 - DensTV flashcon)
    75. Madani TV (720p)
    76. Matrix TV Yogyakarta (720p)
    77. MetroTV (DensTV)
    78. MetroTV (Flashcon)
    79. Nusantara TV (ChannelFeed)
    80. Omid e Iran TV
    81. Outdoor Channel (1080p)
    82. PKTV (480p)
    83. Peer TV Sudtirol (1080p)
    84. RCTI HD (1080p)
    85. RCTV (Indonesia) (720p) [Not 24/7]
    86. RRI Net (1080p)
    87. Radio 51 TV
    88. Rajawali TV
    89. Regio TV (406p)
    90. Riau TV (1080p) [Not 24/7]
    91. Rinjani TV
    92. SCTV
    93. SCTV HD
    94. SMTV (720p)
    95. STV (Indonesia) (720p) [Not 24/7]
    96. Salam TV (720p)
    97. Sangaji TV (720p)
    98. SindoNews
    99. SindoNews (V+)
    100. Sriwijaya TV (720p) [Not 24/7]
    101. Stara TV Bojonegoro (720p)
    102. Stara TV Jakarta (1080p)
    103. Stara TV Parahyangan (720p)
    104. Szlagier TV
    105. TLC HD
    106. TV Mu (720p) [Not 24/7]
    107. TVE Internacional America (576p) [Geo-blocked]
    108. TVE Star (576p)
    109. TVE Star HD (1080p)
    110. TVOne (V+)
    111. TVRI
    112. TVRI (1080i)
    113. TVRI (1080p)
    114. TVRI Aceh (720p)
    115. TVRI Bali (480p)
    116. TVRI Bangka Belitung (480p)
    117. TVRI Bengkulu (480p)
    118. TVRI Jakarta (576i) [Not 24/7]
    119. TVRI Jambi (720p) [Not 24/7]
    120. TVRI Jawa Tengah (720p)
    121. TVRI Jawa Timur (720p)
    122. TVRI Kalimantan Barat (480p)
    123. TVRI Kalimantan Selatan (720p)
    124. TVRI Kalimantan Tengah (480p)
    125. TVRI Kalimantan Timur (720p)
    126. TVRI Lampung (720p)
    127. TVRI Maluku (480p)
    128. TVRI North Sulawesi (1080p)
    129. TVRI North Sumatra (1080p)
    130. TVRI Nusa Tenggara Barat (720p)
    131. TVRI Nusa Tenggara Timur (480p)
    132. TVRI Papua (480p)
    133. TVRI Riau
    134. TVRI Riau (720p) [Not 24/7]
    135. TVRI Sport (1080p)
    136. TVRI Sulawesi Barat (720p)
    137. TVRI Sulawesi Selatan (480p)
    138. TVRI Sulawesi Tengah (720p)
    139. TVRI Sulawesi Tenggara (480p)
    140. TVRI Sumatera Barat (720p)
    141. TVRI West Papua (1080p)
    142. TVRI Yogyakarta (720p)
    143. The Indonesia Channel (1080p)
    144. Timor TV
    145. Trans7 (Transcorp)
    146. Trans7 HD
    147. TransTV (Transcorp)
    148. U Channel
    149. UCL (1080p)
    150. UCL (720p)
    151. VTV
    152. Vision Prime (V+)
    153. iNews HD
    154. iNews HD (1080p)
    155. Хузур ТВ (1080p) [Not 24/7]

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
