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

  📁 Grup: [Lokal (auto)] (154 Channel)
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
    12. Anadolu Net TV (1080p)
    13. Angel TV Indonesia (720p)
    14. Ashiil TV (480p)
    15. Atomic Academy TV (480p)
    16. Atomic TV (360p)
    17. Azan TV
    18. BBC LIFESTYLE
    19. BN Channel (ChannelFeed)
    20. BRTV (720p)
    21. BTV (Channel Feed)
    22. BTV (V+)
    23. Baan Baan TV 73
    24. Balapan HD (1080p)
    25. Balikpapan TV (720p)
    26. Banjar TV (720p) [Not 24/7]
    27. Banten TV
    28. Batam TV (480p) [Not 24/7]
    29. Berita Satu
    30. Berita Satu (DensTV)
    31. Bir TV (720p)
    32. CNBC Indonesia
    33. CNBC Indonesia (ChannelFeed)
    34. CNN Indonesia
    35. Cao Bằng TV (720p)
    36. CelebritiesTV (V+)
    37. Clan Internacional Americas (1080p) [Geo-blocked]
    38. DAAI TV
    39. DAAI TV (Dens)
    40. DMI TV (576i)
    41. Dhoho TV
    42. Fashion TV
    43. Ficom Channel
    44. Food Travel (V+)
    45. GTV
    46. Garuda TV (1080p)
    47. Garuda TV (Flashcon)
    48. Hmong Star TV (720p) [Not 24/7]
    49. Hyder TV (720p)
    50. IDX (V+)
    51. Indonesia Movie Channel (V+)
    52. Indosiar HD
    53. Inter TV (1080p)
    54. Iunior TV (1080p)
    55. JTV (720p)
    56. JTV Kediri (1080p) [Not 24/7]
    57. JTV Madiun
    58. JTV Madura (480p) [Not 24/7]
    59. JTV Malang
    60. Jagantara TV
    61. Kordia TV (1080p)
    62. La 2
    63. Lingkar TV
    64. Love the Planet (1080p)
    65. MAGNA Channel (DensTV)
    66. MAGNA TV (ChannelFeed)
    67. MBG TV (1080p)
    68. MDTV
    69. MDTV (DensTV)
    70. MOJI TV HD (Alt 3 - DensTV flashcon)
    71. MTV Ridiculousness
    72. MTV Ridiculousness (United States) LatAm (720p)
    73. Madani TV (720p)
    74. MetroTV (DensTV)
    75. MetroTV (Flashcon)
    76. Myanmar International TV
    77. Nusantara TV (ChannelFeed)
    78. Omid e Iran TV
    79. Outdoor Channel (1080p)
    80. PKTV (480p)
    81. Peer TV Sudtirol (1080p)
    82. RCTV (Indonesia) (720p) [Not 24/7]
    83. Radar Lampung TV (480p)
    84. Radio 51 TV
    85. Rajawali TV
    86. Riau TV (1080p) [Not 24/7]
    87. Rinjani TV
    88. SCTV HD
    89. SMTV (720p)
    90. STV (Indonesia) (720p) [Not 24/7]
    91. Salam TV (720p)
    92. Sangaji TV (720p)
    93. SindoNews
    94. SindoNews (V+)
    95. Sooriyan TV (1080p)
    96. Sriwijaya TV (720p) [Not 24/7]
    97. Stara TV Bojonegoro (720p)
    98. Stara TV Jakarta (1080p)
    99. Stara TV Parahyangan (720p)
    100. Szlagier TV
    101. TLC HD
    102. TVE Internacional America (576p) [Geo-blocked]
    103. TVE Star (576p)
    104. TVE Star HD (1080p)
    105. TVOne (V+)
    106. TVRI
    107. TVRI (1080i)
    108. TVRI (1080p)
    109. TVRI Aceh (720p)
    110. TVRI Bali (480p)
    111. TVRI Bangka Belitung (480p)
    112. TVRI Bengkulu (480p)
    113. TVRI Gorontalo (480p)
    114. TVRI Jakarta (576i) [Not 24/7]
    115. TVRI Jambi (720p) [Not 24/7]
    116. TVRI Jawa Tengah (720p)
    117. TVRI Jawa Timur (720p)
    118. TVRI Kalimantan Barat (480p)
    119. TVRI Kalimantan Selatan (720p)
    120. TVRI Kalimantan Tengah (480p)
    121. TVRI Kalimantan Timur (720p)
    122. TVRI Lampung (720p)
    123. TVRI Maluku (480p)
    124. TVRI North Sulawesi (1080p)
    125. TVRI North Sumatra (1080p)
    126. TVRI Nusa Tenggara Barat (720p)
    127. TVRI Nusa Tenggara Timur (480p)
    128. TVRI Papua (480p)
    129. TVRI Riau
    130. TVRI Riau (720p) [Not 24/7]
    131. TVRI Sulawesi Barat (720p)
    132. TVRI Sulawesi Selatan (480p)
    133. TVRI Sulawesi Tengah (720p)
    134. TVRI Sulawesi Tenggara (480p)
    135. TVRI Sumatera Barat (720p)
    136. TVRI Sumatera Selatan (480p)
    137. TVRI West Papua (1080p)
    138. TVRI Yogyakarta (720p)
    139. The Indonesia Channel (1080p)
    140. Timor TV
    141. Trans7 (Transcorp)
    142. Trans7 HD
    143. Trans7 HD (Detik)
    144. TransTV (Detik)
    145. TransTV (Transcorp)
    146. TransTV HD
    147. Tropical Moon Urban TV [Not 24/7]
    148. U Channel
    149. UGTV (720p)
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
