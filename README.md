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
    2. Banyumas tv (720p) [not 24/7]
    3. Bn channel (720p)
    4. Caruban tv (1080p)
    5. Dens tv learning
    6. Dhamma tv (720p) [not 24/7]
    7. Dhoho tv (720p)
    8. Duta tv (360p) [not 24/7]
    9. Efarina tv (720p)
    10. Indonesiana tv
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
    26. Radio kita tv (1080p)
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
    5. Aathavan TV (720p)
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
    16. Azan TV
    17. BBC LIFESTYLE
    18. BN Channel (ChannelFeed)
    19. BRTV (720p)
    20. BTV (Channel Feed)
    21. BTV (V+)
    22. Baan Baan TV 73
    23. Balapan HD (1080p)
    24. Balapan International (1080p)
    25. Bali TV
    26. Balikpapan TV (720p)
    27. Bandung TV
    28. Banjar TV (720p) [Not 24/7]
    29. Banten TV
    30. Batam TV (480p) [Not 24/7]
    31. Berita Satu
    32. Berita Satu (DensTV)
    33. Bungo TV
    34. CNBC Indonesia (ChannelFeed)
    35. CNN Indonesia
    36. Canal 24 Horas (720p)
    37. Cao Bằng TV (720p)
    38. CelebritiesTV (V+)
    39. Clan Internacional Americas (1080p) [Geo-blocked]
    40. DAAI TV
    41. DAAI TV (Dens)
    42. DMI TV (576i)
    43. Davika TV (480p)
    44. EmanTv (1080p)
    45. Entertainment (V+)
    46. Fajar TV (720p) [Not 24/7]
    47. Fashion TV
    48. Food Travel (V+)
    49. GTV
    50. Garuda TV (1080p)
    51. Garuda TV (Flashcon)
    52. Hanacaraka TV (V+)
    53. Hmong Star TV (720p) [Not 24/7]
    54. Hyder TV (720p)
    55. I Am Channel (576p)
    56. IDX (V+)
    57. Indonesia Movie Channel (V+)
    58. Indosiar HD
    59. Inter TV (1080p)
    60. Iunior TV (1080p)
    61. JTV (720p)
    62. JTV (V+)
    63. JTV Kediri (1080p) [Not 24/7]
    64. JTV Madiun
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
    83. Nusantara TV (ChannelFeed)
    84. Omid e Iran TV
    85. Outdoor Channel (1080p)
    86. PKTV (480p)
    87. Peer TV Sudtirol (1080p)
    88. RCTV (Indonesia) (720p) [Not 24/7]
    89. RRI Net (1080p)
    90. Radio 51 TV
    91. Rajawali TV
    92. Riau TV (1080p) [Not 24/7]
    93. Rinjani TV
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
    108. TVE Internacional America (576p) [Geo-blocked]
    109. TVE Star (576p)
    110. TVE Star HD (1080p)
    111. TVOne (V+)
    112. TVRI
    113. TVRI (1080i)
    114. TVRI Aceh (720p)
    115. TVRI Bali (480p)
    116. TVRI Bangka Belitung (480p)
    117. TVRI Bengkulu (480p)
    118. TVRI Gorontalo (480p)
    119. TVRI Jakarta (576i) [Not 24/7]
    120. TVRI Jambi (720p) [Not 24/7]
    121. TVRI Jawa Tengah (720p)
    122. TVRI Jawa Timur (720p)
    123. TVRI Kalimantan Barat (480p)
    124. TVRI Kalimantan Selatan (720p)
    125. TVRI Kalimantan Tengah (480p)
    126. TVRI Kalimantan Timur (720p)
    127. TVRI Lampung (720p)
    128. TVRI Maluku (480p)
    129. TVRI North Sulawesi (1080p)
    130. TVRI North Sumatra (1080p)
    131. TVRI Nusa Tenggara Barat (720p)
    132. TVRI Nusa Tenggara Timur (480p)
    133. TVRI Papua (480p)
    134. TVRI Riau
    135. TVRI Riau (720p) [Not 24/7]
    136. TVRI Sulawesi Barat (720p)
    137. TVRI Sulawesi Selatan (480p)
    138. TVRI Sulawesi Tengah (720p)
    139. TVRI Sulawesi Tenggara (480p)
    140. TVRI Sumatera Barat (720p)
    141. TVRI Sumatera Selatan (480p)
    142. TVRI West Papua (1080p)
    143. TVRI Yogyakarta (720p)
    144. The Indonesia Channel (1080p)
    145. Timor TV
    146. Trans7 (Transcorp)
    147. Trans7 HD
    148. TransTV (Transcorp)
    149. TransTV HD
    150. Tropical Moon Urban TV [Not 24/7]
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
