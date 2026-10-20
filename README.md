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

  📁 Grup: [Lokal] (41 Channel)
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
    11. Izzah tv (480p)
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
    27. Radio kita tv (1080p)
    28. Rodja tv (720p)
    29. Salira tv (720p)
    30. Smtv (720p) [not 24/7]
    31. Stara tv (720p)
    32. Stara tv bandung (1080p)
    33. Stara tv cianjur (720p)
    34. Stara tv malang (1080p)
    35. Tatv (720p) [not 24/7]
    36. Tv one
    37. Tv tabalong (720p) [not 24/7]
    38. Tv9 nusantara (720p)
    39. Tvri jawa barat (480p)
    40. Tvri world
    41. Ugtv (720p)

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
    22. Balapan International (1080p)
    23. Bali TV
    24. Balikpapan TV (720p)
    25. Bandung TV
    26. Banjar TV (720p) [Not 24/7]
    27. Batam TV (480p) [Not 24/7]
    28. Berita Satu
    29. Berita Satu (DensTV)
    30. Bungo TV
    31. CNBC Indonesia (ChannelFeed)
    32. CNN Indonesia
    33. Canal 24 Horas (720p)
    34. Cao Bằng TV (720p)
    35. CelebritiesTV (V+)
    36. Clan Internacional Americas (1080p) [Geo-blocked]
    37. DAAI TV
    38. DAAI TV (Dens)
    39. DMI TV (576i)
    40. Davika TV (480p)
    41. EmanTv (1080p)
    42. Entertainment (V+)
    43. Fajar TV (720p) [Not 24/7]
    44. Fashion TV
    45. Ficom Channel
    46. Food Travel (V+)
    47. GTV
    48. Garuda TV (1080p)
    49. Garuda TV (Flashcon)
    50. Hanacaraka TV (V+)
    51. Hmong Star TV (720p) [Not 24/7]
    52. Hyder TV (720p)
    53. IDX (V+)
    54. Indonesia Movie Channel (V+)
    55. Indosiar HD
    56. Inter TV (1080p)
    57. Iunior TV (1080p)
    58. JTV (720p)
    59. JTV (V+)
    60. JTV Kediri (1080p) [Not 24/7]
    61. JTV Madiun
    62. JTV Malang
    63. Jagantara TV
    64. Jogja TV (720p) [Not 24/7]
    65. Kordia TV (1080p)
    66. La 2
    67. Lingkar TV
    68. Love the Planet (1080p)
    69. MAGNA Channel (DensTV)
    70. MAGNA TV (ChannelFeed)
    71. MBG TV (1080p)
    72. MDTV
    73. MDTV (DensTV)
    74. MOJI TV HD (Alt 3 - DensTV flashcon)
    75. MTV Ridiculousness
    76. MTV Ridiculousness (United States) LatAm (720p)
    77. Madani TV (720p)
    78. MetroTV (DensTV)
    79. MetroTV (Flashcon)
    80. Nusantara TV (ChannelFeed)
    81. Omid e Iran TV
    82. Outdoor Channel (1080p)
    83. PKTV (480p)
    84. Peer TV Sudtirol (1080p)
    85. RCTV (Indonesia) (720p) [Not 24/7]
    86. RRI Net (1080p)
    87. Radio 51 TV
    88. Rajawali TV
    89. Riau TV (1080p) [Not 24/7]
    90. Rinjani TV
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
    111. TVRI Aceh (720p)
    112. TVRI Bali (480p)
    113. TVRI Bangka Belitung (480p)
    114. TVRI Bengkulu (480p)
    115. TVRI Gorontalo (480p)
    116. TVRI Jakarta (576i) [Not 24/7]
    117. TVRI Jambi (720p) [Not 24/7]
    118. TVRI Jawa Tengah (720p)
    119. TVRI Jawa Timur (720p)
    120. TVRI Kalimantan Barat (480p)
    121. TVRI Kalimantan Selatan (720p)
    122. TVRI Kalimantan Tengah (480p)
    123. TVRI Kalimantan Timur (720p)
    124. TVRI Lampung (720p)
    125. TVRI Maluku (480p)
    126. TVRI North Sulawesi (1080p)
    127. TVRI North Sumatra (1080p)
    128. TVRI Nusa Tenggara Barat (720p)
    129. TVRI Nusa Tenggara Timur (480p)
    130. TVRI Papua (480p)
    131. TVRI Riau
    132. TVRI Riau (720p) [Not 24/7]
    133. TVRI Sulawesi Barat (720p)
    134. TVRI Sulawesi Selatan (480p)
    135. TVRI Sulawesi Tengah (720p)
    136. TVRI Sulawesi Tenggara (480p)
    137. TVRI Sumatera Barat (720p)
    138. TVRI Sumatera Selatan (480p)
    139. TVRI West Papua (1080p)
    140. TVRI Yogyakarta (720p)
    141. The Indonesia Channel (1080p)
    142. Timor TV
    143. Trans7 (Transcorp)
    144. Trans7 HD
    145. TransTV (Transcorp)
    146. TransTV HD
    147. Tropical Moon Urban TV [Not 24/7]
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
