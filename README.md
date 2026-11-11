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

  📁 Grup: [Lokal] (37 Channel)
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
    17. Moji tv
    18. Mqtv (720p) [not 24/7]
    19. Nhk world japan
    20. Padang tv (720p) [not 24/7]
    21. Pontv (720p)
    22. R tv
    23. Radar tasikmalaya tv (720p) [not 24/7]
    24. Radio kita tv (1080p)
    25. Rodja tv (720p)
    26. Salira tv (720p)
    27. Smtv (720p) [not 24/7]
    28. Stara tv (720p)
    29. Stara tv bandung (1080p)
    30. Stara tv cianjur (720p)
    31. Stara tv malang (1080p)
    32. Tatv (720p) [not 24/7]
    33. Tv one
    34. Tv tabalong (720p) [not 24/7]
    35. Tv9 nusantara (720p)
    36. Tvri jawa barat (480p)
    37. Tvri world

  📁 Grup: [Lokal (auto)] (152 Channel)
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
    16. Astro Blitar TV (720p)
    17. Atomic Academy TV (480p)
    18. Atomic TV (360p)
    19. Azan TV
    20. BBC LIFESTYLE
    21. BN Channel (ChannelFeed)
    22. BRTV (720p)
    23. BTV (Channel Feed)
    24. BTV (V+)
    25. Baan Baan TV 73
    26. Balapan HD (1080p)
    27. Balikpapan TV (720p)
    28. Banjar TV (720p) [Not 24/7]
    29. Banten TV
    30. Batam TV (480p) [Not 24/7]
    31. Berita Satu
    32. Berita Satu (DensTV)
    33. Bungo TV
    34. CNBC Indonesia (ChannelFeed)
    35. CTV Dla Ciebie TV
    36. Cao Bằng TV (720p)
    37. Clan Internacional Americas (1080p) [Geo-blocked]
    38. DAAI TV
    39. DAAI TV (Dens)
    40. DMI TV (576i)
    41. Dhoho TV
    42. EmanTv (1080p)
    43. Fajar TV (720p) [Not 24/7]
    44. Fashion TV
    45. Ficom Channel
    46. GTV
    47. Garuda TV (1080p)
    48. Garuda TV (Flashcon)
    49. Hmong Star TV (720p) [Not 24/7]
    50. Hyder TV (720p)
    51. I Am Channel (576p)
    52. IDX (V+)
    53. Indosiar HD
    54. Inter TV (1080p)
    55. Iunior TV (1080p)
    56. JTV (720p)
    57. JTV Kediri (1080p) [Not 24/7]
    58. JTV Madiun
    59. JTV Madura (480p) [Not 24/7]
    60. JTV Malang
    61. Jagantara TV
    62. Kordia TV (1080p)
    63. La 2
    64. Lingkar TV
    65. Love the Planet (1080p)
    66. MAGNA Channel (DensTV)
    67. MAGNA TV (ChannelFeed)
    68. MBG TV (1080p)
    69. MDTV
    70. MDTV (DensTV)
    71. MOJI TV HD (Alt 3 - DensTV flashcon)
    72. MTV Ridiculousness
    73. MTV Ridiculousness (United States) LatAm (720p)
    74. Madani TV (720p)
    75. Magna Channel (1080p)
    76. Metro TV
    77. MetroTV (DensTV)
    78. MetroTV (Flashcon)
    79. Myanmar International TV
    80. Nusantara TV (ChannelFeed)
    81. Omid e Iran TV
    82. Outdoor Channel (1080p)
    83. PKTV (480p)
    84. Peer TV Sudtirol (1080p)
    85. RCTV (Indonesia) (720p) [Not 24/7]
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
    97. Sriwijaya TV (720p) [Not 24/7]
    98. Stara TV Bojonegoro (720p)
    99. Stara TV Jakarta (1080p)
    100. Stara TV Parahyangan (720p)
    101. TLC HD
    102. TVE Internacional America (576p) [Geo-blocked]
    103. TVE Star (576p)
    104. TVE Star HD (1080p)
    105. TVOne (V+)
    106. TVRI
    107. TVRI (1080i)
    108. TVRI Aceh (720p)
    109. TVRI Bali (480p)
    110. TVRI Bangka Belitung (480p)
    111. TVRI Bengkulu (480p)
    112. TVRI Gorontalo (480p)
    113. TVRI Jakarta (576i) [Not 24/7]
    114. TVRI Jambi (720p) [Not 24/7]
    115. TVRI Jawa Tengah (720p)
    116. TVRI Jawa Timur (720p)
    117. TVRI Kalimantan Barat (480p)
    118. TVRI Kalimantan Selatan (720p)
    119. TVRI Kalimantan Tengah (480p)
    120. TVRI Kalimantan Timur (720p)
    121. TVRI Lampung (720p)
    122. TVRI Maluku (480p)
    123. TVRI North Sulawesi (1080p)
    124. TVRI North Sumatra (1080p)
    125. TVRI Nusa Tenggara Barat (720p)
    126. TVRI Nusa Tenggara Timur (480p)
    127. TVRI Papua (480p)
    128. TVRI Riau
    129. TVRI Riau (720p) [Not 24/7]
    130. TVRI Sulawesi Barat (720p)
    131. TVRI Sulawesi Selatan (480p)
    132. TVRI Sulawesi Tengah (720p)
    133. TVRI Sulawesi Tenggara (480p)
    134. TVRI Sumatera Barat (720p)
    135. TVRI Sumatera Selatan (480p)
    136. TVRI West Papua (1080p)
    137. TVRI Yogyakarta (720p)
    138. The Indonesia Channel (1080p)
    139. Timor TV
    140. Trans7 (Transcorp)
    141. Trans7 HD
    142. TransTV (Transcorp)
    143. TransTV HD
    144. Tropical Moon Urban TV [Not 24/7]
    145. U Channel
    146. UGTV (720p)
    147. VTV
    148. Vision Prime (V+)
    149. Warner TV
    150. Warner TV Asia (720p)
    151. iNews HD
    152. Хузур ТВ (1080p) [Not 24/7]

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
