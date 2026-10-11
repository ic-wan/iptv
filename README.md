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

  📁 Grup: [Lokal] (42 Channel)
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
    10. Efarina tv (720p)
    11. Indonesiana tv
    12. Izzah tv (480p)
    13. Jawa pos tv jakarta (720p)
    14. Jogja istimewa tv (720p)
    15. Jogja tv (720p) [not 24/7]
    16. Jowo
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
    28. Radio kita tv (1080p)
    29. Rodja tv (720p)
    30. Salira tv (720p)
    31. Smtv (720p) [not 24/7]
    32. Stara tv (720p)
    33. Stara tv bandung (1080p)
    34. Stara tv cianjur (720p)
    35. Stara tv malang (1080p)
    36. Tatv (720p) [not 24/7]
    37. Tv one
    38. Tv tabalong (720p) [not 24/7]
    39. Tv9 nusantara (720p)
    40. Tvri jawa barat (480p)
    41. Tvri world
    42. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (157 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV HD
    5. Abadan
    6. Ajman TV (1080p)
    7. Al Qamar TV (1080p)
    8. Anadolu Net TV (1080p)
    9. Angel TV Indonesia (720p)
    10. Ashiil TV (480p)
    11. Astro Blitar TV (720p)
    12. Atomic Academy TV (480p)
    13. Atomic TV (360p)
    14. BBC LIFESTYLE
    15. BN Channel (ChannelFeed)
    16. BRTV (720p)
    17. BTV (Channel Feed)
    18. BTV (V+)
    19. Baan Baan TV 73
    20. Balapan HD (1080p)
    21. Balapan International (1080p)
    22. Bali TV
    23. Balikpapan TV (720p)
    24. Bandung TV
    25. Banjar TV (720p) [Not 24/7]
    26. Batam TV (480p) [Not 24/7]
    27. Berita Satu
    28. Bungo TV
    29. CNBC Indonesia (ChannelFeed)
    30. CNN Indonesia (ChannelFeed)
    31. Canal 24 Horas (720p)
    32. Cao Bằng TV (720p)
    33. CelebritiesTV (V+)
    34. Clan Internacional Americas (1080p) [Geo-blocked]
    35. DAAI TV
    36. DAAI TV (Dens)
    37. DMI TV (576i)
    38. EmanTv (1080p)
    39. Entertainment (V+)
    40. Fashion TV
    41. Ficom Channel
    42. Food Travel (V+)
    43. GTV
    44. GTV (Indonesia) HD (1080p)
    45. Garuda TV (1080p)
    46. Garuda TV (Flashcon)
    47. Hanacaraka TV (V+)
    48. Hmong Star TV (720p) [Not 24/7]
    49. Hyder TV (720p)
    50. IDX (V+)
    51. Indonesia Movie Channel (V+)
    52. Indosiar HD
    53. Indosiar HD (1080p)
    54. Inter TV (1080p)
    55. Iunior TV (1080p)
    56. JTV (720p)
    57. JTV (V+)
    58. JTV Kediri (1080p) [Not 24/7]
    59. JTV Madiun
    60. JTV Malang
    61. Jagantara TV
    62. Kordia TV (1080p)
    63. La 2
    64. Lingkar TV
    65. Love the Planet (1080p)
    66. MAGNA Channel (DensTV)
    67. MAGNA TV (ChannelFeed)
    68. MBG TV (1080p)
    69. MDTV
    70. MDTV (DensTV)
    71. MNCTV HD
    72. MOJI TV HD (Alt 3 - DensTV flashcon)
    73. Madani TV (720p)
    74. MetroTV (DensTV)
    75. MetroTV (Flashcon)
    76. Nusantara TV (ChannelFeed)
    77. Omid e Iran TV
    78. Outdoor Channel (1080p)
    79. PKTV (480p)
    80. Peer TV Sudtirol (1080p)
    81. RCTI HD (1080p)
    82. RCTV (Indonesia) (720p) [Not 24/7]
    83. RRI Net (1080p)
    84. Radio 51 TV
    85. Rajawali TV
    86. Regio TV (406p)
    87. Riau TV (1080p) [Not 24/7]
    88. Rinjani TV
    89. SCTV
    90. SCTV (DASH/MPD)
    91. SCTV HD
    92. SMTV (720p)
    93. STV (Indonesia) (720p) [Not 24/7]
    94. Salam TV (720p)
    95. Sangaji TV (720p)
    96. SindoNews
    97. SindoNews (V+)
    98. Sooriyan TV (1080p)
    99. Sriwijaya TV (720p) [Not 24/7]
    100. Stara TV Bojonegoro (720p)
    101. Stara TV Jakarta (1080p)
    102. Stara TV Parahyangan (720p)
    103. Szlagier TV
    104. TLC HD
    105. TVE Internacional America (576p) [Geo-blocked]
    106. TVE Star (576p)
    107. TVE Star HD (1080p)
    108. TVOne (V+)
    109. TVRI
    110. TVRI (1080i)
    111. TVRI (1080p)
    112. TVRI Aceh (720p)
    113. TVRI Bali (480p)
    114. TVRI Bangka Belitung (480p)
    115. TVRI Bengkulu (480p)
    116. TVRI Gorontalo (480p)
    117. TVRI Jakarta (576i) [Not 24/7]
    118. TVRI Jambi (720p) [Not 24/7]
    119. TVRI Jawa Tengah (720p)
    120. TVRI Jawa Timur (720p)
    121. TVRI Kalimantan Barat (480p)
    122. TVRI Kalimantan Selatan (720p)
    123. TVRI Kalimantan Tengah (480p)
    124. TVRI Kalimantan Timur (720p)
    125. TVRI Lampung (720p)
    126. TVRI Maluku (480p)
    127. TVRI North Sulawesi (1080p)
    128. TVRI North Sumatra (1080p)
    129. TVRI Nusa Tenggara Barat (720p)
    130. TVRI Nusa Tenggara Timur (480p)
    131. TVRI Papua (480p)
    132. TVRI Riau
    133. TVRI Riau (720p) [Not 24/7]
    134. TVRI Sport (1080p)
    135. TVRI Sulawesi Barat (720p)
    136. TVRI Sulawesi Selatan (480p)
    137. TVRI Sulawesi Tengah (720p)
    138. TVRI Sulawesi Tenggara (480p)
    139. TVRI Sumatera Barat (720p)
    140. TVRI Sumatera Selatan (480p)
    141. TVRI West Papua (1080p)
    142. TVRI Yogyakarta (720p)
    143. The Indonesia Channel (1080p)
    144. Timor TV
    145. Trans7 (Transcorp)
    146. Trans7 HD
    147. TransTV (Transcorp)
    148. TransTV HD
    149. U Channel
    150. UCL (1080p)
    151. UCL (720p)
    152. VTV
    153. Vision Prime (V+)
    154. Warner TV Asia (720p)
    155. iNews HD
    156. iNews HD (1080p)
    157. Хузур ТВ (1080p) [Not 24/7]

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
