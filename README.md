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
    12. Jawa pos tv jakarta (720p)
    13. Jogja istimewa tv (720p)
    14. Jowo
    15. Kawanua tv (720p)
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

  📁 Grup: [Lokal (auto)] (154 Channel)
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
    13. Atomic Academy TV (480p)
    14. Atomic TV (360p)
    15. BBC LIFESTYLE
    16. BN Channel (ChannelFeed)
    17. BRTV (720p)
    18. BTV (Channel Feed)
    19. BTV (V+)
    20. Baan Baan TV 73
    21. Balapan HD (1080p)
    22. Bali TV
    23. Balikpapan TV (720p)
    24. Bandung TV
    25. Banjar TV (720p) [Not 24/7]
    26. Batam TV (480p) [Not 24/7]
    27. Berita Satu
    28. Berita Satu (DensTV)
    29. Bungo TV
    30. CNBC Indonesia (ChannelFeed)
    31. CNN Indonesia
    32. Canal 24 Horas (720p)
    33. Cao Bằng TV (720p)
    34. CelebritiesTV (V+)
    35. Clan Internacional Americas (1080p) [Geo-blocked]
    36. DAAI TV
    37. DAAI TV (Dens)
    38. DMI TV (576i)
    39. Davika TV (480p)
    40. Entertainment (V+)
    41. Fajar TV (720p) [Not 24/7]
    42. Fashion TV
    43. Ficom Channel
    44. Food Travel (V+)
    45. GTV
    46. Garuda TV (1080p)
    47. Garuda TV (Flashcon)
    48. Hanacaraka TV (V+)
    49. Hmong Star TV (720p) [Not 24/7]
    50. Hyder TV (720p)
    51. I Am Channel (576p)
    52. IDX (V+)
    53. Indonesia Movie Channel (V+)
    54. Indosiar HD
    55. Inter TV (1080p)
    56. Iunior TV (1080p)
    57. JTV (720p)
    58. JTV (V+)
    59. JTV Kediri (1080p) [Not 24/7]
    60. JTV Madiun
    61. JTV Malang
    62. Jagantara TV
    63. Jogja TV (720p) [Not 24/7]
    64. Kordia TV (1080p)
    65. La 2
    66. Lingkar TV
    67. Love the Planet (1080p)
    68. MAGNA Channel (DensTV)
    69. MAGNA TV (ChannelFeed)
    70. MBG TV (1080p)
    71. MDTV
    72. MDTV (DensTV)
    73. MOJI TV HD (Alt 3 - DensTV flashcon)
    74. MTV Ridiculousness
    75. MTV Ridiculousness (United States) LatAm (720p)
    76. Madani TV (720p)
    77. MetroTV (DensTV)
    78. MetroTV (Flashcon)
    79. Nusantara TV (ChannelFeed)
    80. Omid e Iran TV
    81. Outdoor Channel (1080p)
    82. PKTV (480p)
    83. Peer TV Sudtirol (1080p)
    84. RCTV (Indonesia) (720p) [Not 24/7]
    85. RRI Net (1080p)
    86. Radio 51 TV
    87. Rajawali TV
    88. Riau TV (1080p) [Not 24/7]
    89. Rinjani TV
    90. SCTV HD
    91. SMTV (720p)
    92. STV (Indonesia) (720p) [Not 24/7]
    93. Salam TV (720p)
    94. Sangaji TV (720p)
    95. SindoNews
    96. SindoNews (V+)
    97. Sooriyan TV (1080p)
    98. Sriwijaya TV (720p) [Not 24/7]
    99. Stara TV Bojonegoro (720p)
    100. Stara TV Jakarta (1080p)
    101. Stara TV Parahyangan (720p)
    102. Szlagier TV
    103. TLC HD
    104. TVE Internacional America (576p) [Geo-blocked]
    105. TVE Star (576p)
    106. TVE Star HD (1080p)
    107. TVOne (V+)
    108. TVRI
    109. TVRI (1080i)
    110. TVRI Aceh (720p)
    111. TVRI Bali (480p)
    112. TVRI Bangka Belitung (480p)
    113. TVRI Bengkulu (480p)
    114. TVRI Gorontalo (480p)
    115. TVRI Jakarta (576i) [Not 24/7]
    116. TVRI Jambi (720p) [Not 24/7]
    117. TVRI Jawa Tengah (720p)
    118. TVRI Jawa Timur (720p)
    119. TVRI Kalimantan Barat (480p)
    120. TVRI Kalimantan Selatan (720p)
    121. TVRI Kalimantan Tengah (480p)
    122. TVRI Kalimantan Timur (720p)
    123. TVRI Lampung (720p)
    124. TVRI Maluku (480p)
    125. TVRI North Sulawesi (1080p)
    126. TVRI North Sumatra (1080p)
    127. TVRI Nusa Tenggara Barat (720p)
    128. TVRI Nusa Tenggara Timur (480p)
    129. TVRI Papua (480p)
    130. TVRI Riau
    131. TVRI Riau (720p) [Not 24/7]
    132. TVRI Sulawesi Barat (720p)
    133. TVRI Sulawesi Selatan (480p)
    134. TVRI Sulawesi Tengah (720p)
    135. TVRI Sulawesi Tenggara (480p)
    136. TVRI Sumatera Barat (720p)
    137. TVRI Sumatera Selatan (480p)
    138. TVRI West Papua (1080p)
    139. TVRI Yogyakarta (720p)
    140. The Indonesia Channel (1080p)
    141. Timor TV
    142. Trans7 (Transcorp)
    143. Trans7 HD
    144. TransTV (Transcorp)
    145. TransTV HD
    146. Tropical Moon Urban TV [Not 24/7]
    147. U Channel
    148. UCL (1080p)
    149. UCL (720p)
    150. VTV
    151. Vision Prime (V+)
    152. Warner TV Asia (720p)
    153. iNews HD
    154. Хузур ТВ (1080p) [Not 24/7]

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
