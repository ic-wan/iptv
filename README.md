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

  📁 Grup: [Lokal] (36 Channel)
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
    10. Jawa pos tv jakarta (720p)
    11. Jogja istimewa tv (720p)
    12. Jowo
    13. Kawanua tv (720p)
    14. Kompas tv
    15. Madu tv (576p)
    16. Moji tv
    17. Mqtv (720p) [not 24/7]
    18. Nhk world japan
    19. Padang tv (720p) [not 24/7]
    20. Pontv (720p)
    21. R tv
    22. Radar tasikmalaya tv (720p) [not 24/7]
    23. Radio kita tv (1080p)
    24. Rodja tv (720p)
    25. Salira tv (720p)
    26. Smtv (720p) [not 24/7]
    27. Stara tv (720p)
    28. Stara tv bandung (1080p)
    29. Stara tv cianjur (720p)
    30. Stara tv malang (1080p)
    31. Tatv (720p) [not 24/7]
    32. Tv one
    33. Tv tabalong (720p) [not 24/7]
    34. Tv9 nusantara (720p)
    35. Tvri jawa barat (480p)
    36. Tvri world

  📁 Grup: [Lokal (auto)] (146 Channel)
  ----------------------------------------
    1. 24 Horas (720p)
    2. 24 Канал (1080p)
    3. A Spor SD (1080p)
    4. ABC Australia
    5. ANTV HD
    6. AXN Asia Indonesia
    7. Aathavan TV (720p)
    8. Abadan
    9. Ahsan TV
    10. Ajman TV (1080p)
    11. Al Qamar TV (1080p)
    12. An Ninh TV HD (1080p)
    13. Anadolu Net TV (1080p)
    14. Angel TV Indonesia (720p)
    15. Ashiil TV (480p)
    16. Atomic Academy TV (480p)
    17. Atomic TV (360p)
    18. BBC LIFESTYLE
    19. BN Channel (ChannelFeed)
    20. BRTV (720p)
    21. BTV (Channel Feed)
    22. BTV (V+)
    23. Baan Baan TV 73
    24. Balapan HD (1080p)
    25. Balapan International (1080p)
    26. Balikpapan TV (720p)
    27. Banjar TV (720p) [Not 24/7]
    28. Banten TV
    29. Batam TV (480p) [Not 24/7]
    30. Berita Satu
    31. Berita Satu (DensTV)
    32. CNBC Indonesia
    33. CNBC Indonesia (ChannelFeed)
    34. CTV Dla Ciebie TV
    35. Cao Bằng TV (720p)
    36. Clan Internacional Americas (1080p) [Geo-blocked]
    37. DAAI TV
    38. DAAI TV (Dens)
    39. DMI TV (576i)
    40. Dhoho TV
    41. EmanTv (1080p)
    42. Fashion TV
    43. Ficom Channel
    44. GTV
    45. Garuda TV (1080p)
    46. Garuda TV (Flashcon)
    47. Hmong Star TV (720p) [Not 24/7]
    48. Hyder TV (720p)
    49. I Am Channel (576p)
    50. IDX (V+)
    51. Indosiar HD
    52. Inter TV (1080p)
    53. Iunior TV (1080p)
    54. JTV (720p)
    55. JTV Kediri (1080p) [Not 24/7]
    56. JTV Madiun
    57. JTV Malang
    58. Jagantara TV
    59. Kordia TV (1080p)
    60. La 2
    61. Love the Planet (1080p)
    62. MAGNA Channel (DensTV)
    63. MBG TV (1080p)
    64. MDTV
    65. MDTV (DensTV)
    66. MOJI TV HD (Alt 3 - DensTV flashcon)
    67. MTV Ridiculousness
    68. MTV Ridiculousness (United States) LatAm (720p)
    69. Madani TV (720p)
    70. Magna Channel (1080p)
    71. Metro TV
    72. MetroTV (DensTV)
    73. MetroTV (Flashcon)
    74. Nusantara TV (ChannelFeed)
    75. Omid e Iran TV
    76. Outdoor Channel (1080p)
    77. PKTV (480p)
    78. Peer TV Sudtirol (1080p)
    79. RCTV (Indonesia) (720p) [Not 24/7]
    80. Radio 51 TV
    81. Rajawali TV
    82. Riau TV (1080p) [Not 24/7]
    83. SCTV HD
    84. SMTV (720p)
    85. STV (Indonesia) (720p) [Not 24/7]
    86. Salam TV (720p)
    87. Sangaji TV (720p)
    88. SindoNews
    89. SindoNews (V+)
    90. Sriwijaya TV (720p) [Not 24/7]
    91. Stara TV Bojonegoro (720p)
    92. Stara TV Jakarta (1080p)
    93. Stara TV Parahyangan (720p)
    94. TLC HD
    95. TVE Internacional America (576p) [Geo-blocked]
    96. TVE Star (576p)
    97. TVE Star HD (1080p)
    98. TVOne (V+)
    99. TVRI
    100. TVRI (1080i)
    101. TVRI Aceh (720p)
    102. TVRI Bali (480p)
    103. TVRI Bangka Belitung (480p)
    104. TVRI Bengkulu (480p)
    105. TVRI Gorontalo (480p)
    106. TVRI Jakarta (576i) [Not 24/7]
    107. TVRI Jambi (720p) [Not 24/7]
    108. TVRI Jawa Tengah (720p)
    109. TVRI Jawa Timur (720p)
    110. TVRI Kalimantan Barat (480p)
    111. TVRI Kalimantan Selatan (720p)
    112. TVRI Kalimantan Tengah (480p)
    113. TVRI Kalimantan Timur (720p)
    114. TVRI Lampung (720p)
    115. TVRI Maluku (480p)
    116. TVRI North Sulawesi (1080p)
    117. TVRI North Sumatra (1080p)
    118. TVRI Nusa Tenggara Barat (720p)
    119. TVRI Nusa Tenggara Timur (480p)
    120. TVRI Papua (480p)
    121. TVRI Riau
    122. TVRI Riau (720p) [Not 24/7]
    123. TVRI Sulawesi Barat (720p)
    124. TVRI Sulawesi Selatan (480p)
    125. TVRI Sulawesi Tengah (720p)
    126. TVRI Sulawesi Tenggara (480p)
    127. TVRI Sumatera Barat (720p)
    128. TVRI Sumatera Selatan (480p)
    129. TVRI West Papua (1080p)
    130. TVRI Yogyakarta (720p)
    131. The Indonesia Channel (1080p)
    132. Trans7 (Transcorp)
    133. Trans7 HD
    134. Trans7 HD (Detik)
    135. TransTV (Detik)
    136. TransTV (Transcorp)
    137. TransTV HD
    138. Tropical Moon Urban TV [Not 24/7]
    139. U Channel
    140. UGTV (720p)
    141. VTV
    142. Vision Prime (V+)
    143. Warner TV
    144. Warner TV Asia (720p)
    145. iNews HD
    146. Хузур ТВ (1080p) [Not 24/7]

  📁 Grup: [Radio] (4 Channel)
  ----------------------------------------
    1. Prambors fm
    2. Rodja fm
    3. The rockin life
    4. The rockin life (indirect)

  📁 Grup: [Travels] (4 Channel)
  ----------------------------------------
    1. Dronetv (1080p)
    2. Intravel (1080p)
    3. Travel escapes (1080p)
    4. Travel tv (576p)

  📁 Grup: [Youtube Music] (1 Channel)
  ----------------------------------------
    1. YouTube Stream (DNL6Wy6IstE)

=============================================
```
<!-- END_PROGRAM_LIST -->
