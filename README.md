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

  📁 Grup: [Lokal (auto)] (156 Channel)
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
    14. Atambua TV (720p)
    15. Atomic Academy TV (480p)
    16. Atomic TV (360p)
    17. BBC LIFESTYLE
    18. BN Channel (ChannelFeed)
    19. BRTV (720p)
    20. BTV (Channel Feed)
    21. BTV (V+)
    22. Baan Baan TV 73
    23. Balapan HD (1080p)
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
    34. Canal 24 Horas (720p)
    35. Cao Bằng TV (720p)
    36. CelebritiesTV (V+)
    37. Clan Internacional Americas (1080p) [Geo-blocked]
    38. DAAI TV
    39. DAAI TV (Dens)
    40. DMI TV (576i)
    41. Davika TV (480p)
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
    82. Nusantara TV (ChannelFeed)
    83. Omid e Iran TV
    84. Outdoor Channel (1080p)
    85. PKTV (480p)
    86. Peer TV Sudtirol (1080p)
    87. RRI Net (1080p)
    88. Radio 51 TV
    89. Rajawali TV
    90. Riau TV (1080p) [Not 24/7]
    91. Rinjani TV
    92. SCTV HD
    93. SMTV (720p)
    94. STV (Indonesia) (720p) [Not 24/7]
    95. Salam TV (720p)
    96. Sangaji TV (720p)
    97. SindoNews
    98. SindoNews (V+)
    99. Sooriyan TV (1080p)
    100. Sriwijaya TV (720p) [Not 24/7]
    101. Stara TV Bojonegoro (720p)
    102. Stara TV Jakarta (1080p)
    103. Stara TV Parahyangan (720p)
    104. Szlagier TV
    105. TLC HD
    106. TVE Internacional America (576p) [Geo-blocked]
    107. TVE Star (576p)
    108. TVE Star HD (1080p)
    109. TVOne (V+)
    110. TVRI
    111. TVRI (1080i)
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
    134. TVRI Sulawesi Barat (720p)
    135. TVRI Sulawesi Selatan (480p)
    136. TVRI Sulawesi Tengah (720p)
    137. TVRI Sulawesi Tenggara (480p)
    138. TVRI Sumatera Barat (720p)
    139. TVRI Sumatera Selatan (480p)
    140. TVRI West Papua (1080p)
    141. TVRI Yogyakarta (720p)
    142. The Indonesia Channel (1080p)
    143. Timor TV
    144. Trans7 (Transcorp)
    145. Trans7 HD
    146. TransTV (Transcorp)
    147. TransTV HD
    148. Tropical Moon Urban TV [Not 24/7]
    149. U Channel
    150. UCL (1080p)
    151. UCL (720p)
    152. VTV
    153. Vision Prime (V+)
    154. Warner TV Asia (720p)
    155. iNews HD
    156. Хузур ТВ (1080p) [Not 24/7]

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
