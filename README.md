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

  📁 Grup: [Lokal (auto)] (159 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV HD
    5. ATV (Turkiye) (1080p)
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
    50. I Am Channel (576p)
    51. IDX (V+)
    52. Indonesia Movie Channel (V+)
    53. Indosiar HD
    54. Indosiar HD (1080p)
    55. Inter TV (1080p)
    56. Iunior TV (1080p)
    57. JTV (720p)
    58. JTV (V+)
    59. JTV Kediri (1080p) [Not 24/7]
    60. JTV Madiun
    61. JTV Madura (480p) [Not 24/7]
    62. JTV Malang
    63. Jagantara TV
    64. Kordia TV (1080p)
    65. La 2
    66. Love the Planet (1080p)
    67. MAGNA Channel (DensTV)
    68. MAGNA TV (ChannelFeed)
    69. MBG TV (1080p)
    70. MDTV
    71. MDTV (DensTV)
    72. MNCTV HD
    73. MOJI TV HD (Alt 3 - DensTV flashcon)
    74. Madani TV (720p)
    75. Matrix TV Yogyakarta (720p)
    76. MetroTV (DensTV)
    77. MetroTV (Flashcon)
    78. Nusantara TV (ChannelFeed)
    79. Omid e Iran TV
    80. Outdoor Channel (1080p)
    81. PKTV (480p)
    82. Peer TV Sudtirol (1080p)
    83. RCTI HD (1080p)
    84. RCTV (Indonesia) (720p) [Not 24/7]
    85. RRI Net (1080p)
    86. Radio 51 TV
    87. Rajawali TV
    88. Regio TV (406p)
    89. Riau TV (1080p) [Not 24/7]
    90. Rinjani TV
    91. SCTV
    92. SCTV (DASH/MPD)
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
    107. TV Mu (720p) [Not 24/7]
    108. TVE Internacional America (576p) [Geo-blocked]
    109. TVE Star (576p)
    110. TVE Star HD (1080p)
    111. TVOne (V+)
    112. TVRI
    113. TVRI (1080i)
    114. TVRI (1080p)
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
    147. Timor TV
    148. Trans7 (Transcorp)
    149. Trans7 HD
    150. TransTV (Transcorp)
    151. TransTV HD
    152. U Channel
    153. UCL (1080p)
    154. UCL (720p)
    155. VTV
    156. Vision Prime (V+)
    157. iNews HD
    158. iNews HD (1080p)
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
