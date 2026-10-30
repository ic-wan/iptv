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

  📁 Grup: [Lokal] (38 Channel)
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
    10. Izzah tv (480p)
    11. Jawa pos tv jakarta (720p)
    12. Jogja istimewa tv (720p)
    13. Jowo
    14. Kawanua tv (720p)
    15. Kompas tv
    16. Madu tv (576p)
    17. Magna channel (1080p) [not 24/7]
    18. Metro tv
    19. Moji tv
    20. Mqtv (720p) [not 24/7]
    21. Nhk world japan
    22. Padang tv (720p) [not 24/7]
    23. Pontv (720p)
    24. R tv
    25. Radar tasikmalaya tv (720p) [not 24/7]
    26. Rodja tv (720p)
    27. Salira tv (720p)
    28. Smtv (720p) [not 24/7]
    29. Stara tv (720p)
    30. Stara tv bandung (1080p)
    31. Stara tv cianjur (720p)
    32. Stara tv malang (1080p)
    33. Tatv (720p) [not 24/7]
    34. Tv one
    35. Tv tabalong (720p) [not 24/7]
    36. Tv9 nusantara (720p)
    37. Tvri jawa barat (480p)
    38. Tvri world

  📁 Grup: [Lokal (auto)] (159 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV HD
    5. Aathavan TV (720p)
    6. Abadan
    7. Ajman TV (1080p)
    8. Al Qamar TV (1080p)
    9. Anadolu Net TV (1080p)
    10. Angel TV Indonesia (720p)
    11. Ashiil TV (480p)
    12. Atomic Academy TV (480p)
    13. Atomic TV (360p)
    14. Azan TV
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
    26. Banten TV
    27. Batam TV (480p) [Not 24/7]
    28. Berita Satu
    29. Berita Satu (DensTV)
    30. Bir TV (720p)
    31. Bungo TV
    32. CNBC Indonesia
    33. CNBC Indonesia (ChannelFeed)
    34. CNN Indonesia
    35. Canal 24 Horas (720p)
    36. Cao Bằng TV (720p)
    37. CelebritiesTV (V+)
    38. Clan Internacional Americas (1080p) [Geo-blocked]
    39. DAAI TV
    40. DAAI TV (Dens)
    41. DMI TV (576i)
    42. EmanTv (1080p)
    43. Entertainment (V+)
    44. Fajar TV (720p) [Not 24/7]
    45. Fashion TV
    46. Ficom Channel
    47. Food Travel (V+)
    48. GTV
    49. Garuda TV (1080p)
    50. Garuda TV (Flashcon)
    51. Hanacaraka TV (V+)
    52. Hmong Star TV (720p) [Not 24/7]
    53. Hyder TV (720p)
    54. I Am Channel (576p)
    55. IDX (V+)
    56. Indonesia Movie Channel (V+)
    57. Indosiar HD
    58. Inter TV (1080p)
    59. Iunior TV (1080p)
    60. JTV (720p)
    61. JTV (V+)
    62. JTV Kediri (1080p) [Not 24/7]
    63. JTV Madiun
    64. JTV Madura (480p) [Not 24/7]
    65. JTV Malang
    66. Jagantara TV
    67. Jogja TV (720p) [Not 24/7]
    68. Kordia TV (1080p)
    69. La 2
    70. Lingkar TV
    71. Love the Planet (1080p)
    72. MAGNA Channel (DensTV)
    73. MAGNA TV (ChannelFeed)
    74. MBG TV (1080p)
    75. MDTV
    76. MDTV (DensTV)
    77. MOJI TV HD (Alt 3 - DensTV flashcon)
    78. MTV Ridiculousness
    79. MTV Ridiculousness (United States) LatAm (720p)
    80. Madani TV (720p)
    81. MetroTV (DensTV)
    82. MetroTV (Flashcon)
    83. Myanmar International TV
    84. Nusantara TV (ChannelFeed)
    85. Omid e Iran TV
    86. Outdoor Channel (1080p)
    87. PKTV (480p)
    88. Peer TV Sudtirol (1080p)
    89. RCTV (Indonesia) (720p) [Not 24/7]
    90. RRI Net (1080p)
    91. Radar Lampung TV (480p)
    92. Radio 51 TV
    93. Rajawali TV
    94. Riau TV (1080p) [Not 24/7]
    95. Rinjani TV
    96. SCTV HD
    97. SMTV (720p)
    98. STV (Indonesia) (720p) [Not 24/7]
    99. Salam TV (720p)
    100. Sangaji TV (720p)
    101. SindoNews
    102. SindoNews (V+)
    103. Sriwijaya TV (720p) [Not 24/7]
    104. Stara TV Bojonegoro (720p)
    105. Stara TV Jakarta (1080p)
    106. Stara TV Parahyangan (720p)
    107. Szlagier TV
    108. TLC HD
    109. TVE Internacional America (576p) [Geo-blocked]
    110. TVE Star (576p)
    111. TVE Star HD (1080p)
    112. TVOne (V+)
    113. TVRI
    114. TVRI (1080i)
    115. TVRI Aceh (720p)
    116. TVRI Bali (480p)
    117. TVRI Bangka Belitung (480p)
    118. TVRI Bengkulu (480p)
    119. TVRI Gorontalo (480p)
    120. TVRI Jakarta (576i) [Not 24/7]
    121. TVRI Jambi (720p) [Not 24/7]
    122. TVRI Jawa Tengah (720p)
    123. TVRI Jawa Timur (720p)
    124. TVRI Kalimantan Barat (480p)
    125. TVRI Kalimantan Selatan (720p)
    126. TVRI Kalimantan Tengah (480p)
    127. TVRI Kalimantan Timur (720p)
    128. TVRI Lampung (720p)
    129. TVRI Maluku (480p)
    130. TVRI North Sulawesi (1080p)
    131. TVRI North Sumatra (1080p)
    132. TVRI Nusa Tenggara Barat (720p)
    133. TVRI Nusa Tenggara Timur (480p)
    134. TVRI Papua (480p)
    135. TVRI Riau
    136. TVRI Riau (720p) [Not 24/7]
    137. TVRI Sulawesi Barat (720p)
    138. TVRI Sulawesi Selatan (480p)
    139. TVRI Sulawesi Tengah (720p)
    140. TVRI Sulawesi Tenggara (480p)
    141. TVRI Sumatera Barat (720p)
    142. TVRI Sumatera Selatan (480p)
    143. TVRI West Papua (1080p)
    144. TVRI Yogyakarta (720p)
    145. The Indonesia Channel (1080p)
    146. Timor TV
    147. Trans7 (Transcorp)
    148. Trans7 HD
    149. TransTV (Detik)
    150. TransTV (Transcorp)
    151. TransTV HD
    152. Tropical Moon Urban TV [Not 24/7]
    153. U Channel
    154. UGTV (720p)
    155. VTV
    156. Vision Prime (V+)
    157. Warner TV Asia (720p)
    158. iNews HD
    159. Хузур ТВ (1080p) [Not 24/7]

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
