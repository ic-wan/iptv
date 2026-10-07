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

  📁 Grup: [Lokal] (43 Channel)
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
    17. Kawanua tv (720p)
    18. Kompas tv
    19. Madu tv (576p)
    20. Magna channel (1080p) [not 24/7]
    21. Metro tv
    22. Moji tv
    23. Mqtv (720p) [not 24/7]
    24. Nhk world japan
    25. Padang tv (720p) [not 24/7]
    26. Pontv (720p)
    27. R tv
    28. Radar tasikmalaya tv (720p) [not 24/7]
    29. Radio kita tv (1080p)
    30. Rodja tv (720p)
    31. Salira tv (720p)
    32. Smtv (720p) [not 24/7]
    33. Stara tv (720p)
    34. Stara tv bandung (1080p)
    35. Stara tv cianjur (720p)
    36. Stara tv malang (1080p)
    37. Tatv (720p) [not 24/7]
    38. Tv one
    39. Tv tabalong (720p) [not 24/7]
    40. Tv9 nusantara (720p)
    41. Tvri jawa barat (480p)
    42. Tvri world
    43. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (157 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV HD
    5. Abadan
    6. Ahsan TV
    7. Ajman TV (1080p)
    8. Al Qamar TV (1080p)
    9. Anadolu Net TV (1080p)
    10. Angel TV Indonesia (720p)
    11. Ashiil TV (480p)
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
    42. First Lifestyle
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
    67. Lingkar TV
    68. Love the Planet (1080p)
    69. MAGNA Channel (DensTV)
    70. MAGNA TV (ChannelFeed)
    71. MBG TV (1080p)
    72. MDTV
    73. MDTV (DensTV)
    74. MNCTV HD
    75. MOJI TV HD (Alt 3 - DensTV flashcon)
    76. Madani TV (720p)
    77. Matrix TV Yogyakarta (720p)
    78. MetroTV (DensTV)
    79. MetroTV (Flashcon)
    80. Nusantara TV (ChannelFeed)
    81. Omid e Iran TV
    82. Outdoor Channel (1080p)
    83. PKTV (480p)
    84. Peer TV Sudtirol (1080p)
    85. RCTI HD (1080p)
    86. RCTV (Indonesia) (720p) [Not 24/7]
    87. RRI Net (1080p)
    88. Radio 51 TV
    89. Rajawali TV
    90. Regio TV (406p)
    91. Riau TV (1080p) [Not 24/7]
    92. Rinjani TV
    93. SCTV
    94. SCTV HD
    95. SMTV (720p)
    96. STV (Indonesia) (720p) [Not 24/7]
    97. Salam TV (720p)
    98. Sangaji TV (720p)
    99. SindoNews
    100. SindoNews (V+)
    101. Sooriyan TV (1080p)
    102. Sriwijaya TV (720p) [Not 24/7]
    103. Stara TV Bojonegoro (720p)
    104. Stara TV Jakarta (1080p)
    105. Stara TV Parahyangan (720p)
    106. Szlagier TV
    107. TLC HD
    108. TV Mu (720p) [Not 24/7]
    109. TVE Internacional America (576p) [Geo-blocked]
    110. TVE Star (576p)
    111. TVE Star HD (1080p)
    112. TVOne (V+)
    113. TVRI
    114. TVRI (1080i)
    115. TVRI (1080p)
    116. TVRI Aceh (720p)
    117. TVRI Bali (480p)
    118. TVRI Bangka Belitung (480p)
    119. TVRI Bengkulu (480p)
    120. TVRI Gorontalo (480p)
    121. TVRI Jakarta (576i) [Not 24/7]
    122. TVRI Jambi (720p) [Not 24/7]
    123. TVRI Jawa Tengah (720p)
    124. TVRI Jawa Timur (720p)
    125. TVRI Kalimantan Barat (480p)
    126. TVRI Kalimantan Selatan (720p)
    127. TVRI Kalimantan Tengah (480p)
    128. TVRI Kalimantan Timur (720p)
    129. TVRI Maluku (480p)
    130. TVRI North Sulawesi (1080p)
    131. TVRI North Sumatra (1080p)
    132. TVRI Nusa Tenggara Barat (720p)
    133. TVRI Nusa Tenggara Timur (480p)
    134. TVRI Papua (480p)
    135. TVRI Riau
    136. TVRI Riau (720p) [Not 24/7]
    137. TVRI Sport (1080p)
    138. TVRI Sulawesi Barat (720p)
    139. TVRI Sulawesi Selatan (480p)
    140. TVRI Sulawesi Tengah (720p)
    141. TVRI Sulawesi Tenggara (480p)
    142. TVRI Sumatera Barat (720p)
    143. TVRI Sumatera Selatan (480p)
    144. TVRI West Papua (1080p)
    145. TVRI Yogyakarta (720p)
    146. The Indonesia Channel (1080p)
    147. Trans7 (Transcorp)
    148. Trans7 HD
    149. TransTV (Transcorp)
    150. U Channel
    151. UCL (1080p)
    152. UCL (720p)
    153. VTV
    154. Vision Prime (V+)
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
