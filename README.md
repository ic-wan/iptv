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
    10. Efarina tv (720p)
    11. Indonesiana tv
    12. Izzah tv (480p)
    13. Jawa pos tv jakarta (720p)
    14. Jogja istimewa tv (720p)
    15. Jowo
    16. Kompas tv
    17. Madu tv (576p)
    18. Magna channel (1080p) [not 24/7]
    19. Metro tv
    20. Moji tv
    21. Mqtv (720p) [not 24/7]
    22. Nhk world japan
    23. Padang tv (720p) [not 24/7]
    24. Pontv (720p)
    25. R tv
    26. Radar tasikmalaya tv (720p) [not 24/7]
    27. Rodja tv (720p)
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
    12. Astro Blitar TV (720p)
    13. Atambua TV (720p)
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
    30. Berita Satu (DensTV)
    31. Bungo TV
    32. CNBC Indonesia (ChannelFeed)
    33. CNN Indonesia
    34. CNN Indonesia (ChannelFeed)
    35. Canal 24 Horas (720p)
    36. Cao Bằng TV (720p)
    37. CelebritiesTV (V+)
    38. Clan Internacional Americas (1080p) [Geo-blocked]
    39. DAAI TV
    40. DAAI TV (Dens)
    41. DMI TV (576i)
    42. EmanTv (1080p)
    43. Entertainment (V+)
    44. Fashion TV
    45. Ficom Channel
    46. Food Travel (V+)
    47. GTV
    48. Garuda TV (1080p)
    49. Garuda TV (Flashcon)
    50. Hanacaraka TV (V+)
    51. Hmong Star TV (720p) [Not 24/7]
    52. Hyder TV (720p)
    53. I Am Channel (576p)
    54. IDX (V+)
    55. Indonesia Movie Channel (V+)
    56. Indosiar HD
    57. Inter TV (1080p)
    58. Iunior TV (1080p)
    59. JTV (720p)
    60. JTV (V+)
    61. JTV Kediri (1080p) [Not 24/7]
    62. JTV Madiun
    63. JTV Madura (480p) [Not 24/7]
    64. JTV Malang
    65. Jagantara TV
    66. Jogja TV (720p) [Not 24/7]
    67. Kordia TV (1080p)
    68. La 2
    69. Lingkar TV
    70. Love the Planet (1080p)
    71. MAGNA Channel (DensTV)
    72. MAGNA TV (ChannelFeed)
    73. MBG TV (1080p)
    74. MDTV
    75. MDTV (DensTV)
    76. MOJI TV HD (Alt 3 - DensTV flashcon)
    77. MTV Ridiculousness
    78. MTV Ridiculousness (United States) LatAm (720p)
    79. Madani TV (720p)
    80. MetroTV (DensTV)
    81. MetroTV (Flashcon)
    82. Myanmar International TV
    83. Nusantara TV (ChannelFeed)
    84. Omid e Iran TV
    85. Outdoor Channel (1080p)
    86. PKTV (480p)
    87. Peer TV Sudtirol (1080p)
    88. RRI Net (1080p)
    89. Radar Lampung TV (480p)
    90. Radio 51 TV
    91. Rajawali TV
    92. Rinjani TV
    93. SCTV HD
    94. SMTV (720p)
    95. STV (Indonesia) (720p) [Not 24/7]
    96. Salam TV (720p)
    97. Sangaji TV (720p)
    98. SindoNews
    99. SindoNews (V+)
    100. Sooriyan TV (1080p)
    101. Sriwijaya TV (720p) [Not 24/7]
    102. Stara TV Bojonegoro (720p)
    103. Stara TV Jakarta (1080p)
    104. Stara TV Parahyangan (720p)
    105. Szlagier TV
    106. TLC HD
    107. TVE Internacional America (576p) [Geo-blocked]
    108. TVE Star (576p)
    109. TVE Star HD (1080p)
    110. TVOne (V+)
    111. TVRI
    112. TVRI (1080i)
    113. TVRI Aceh (720p)
    114. TVRI Bali (480p)
    115. TVRI Bangka Belitung (480p)
    116. TVRI Bengkulu (480p)
    117. TVRI Gorontalo (480p)
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
    149. Tropical Moon Urban TV [Not 24/7]
    150. U Channel
    151. UCL (1080p)
    152. UCL (720p)
    153. VTV
    154. Vision Prime (V+)
    155. Warner TV Asia (720p)
    156. iNews HD
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
