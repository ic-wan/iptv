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

  📁 Grup: [Indihome] (8 Channel)
  ----------------------------------------
    1. Berita satu
    2. I news
    3. Jtv
    4. Kompas tv
    5. Max sport
    6. Prambors tv
    7. Rtv
    8. Sctv

  📁 Grup: [Kids] (5 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Kidsflix (1080p) [not 24/7]
    4. Moonbug kids (1080p)
    5. Pbs kids

  📁 Grup: [Lokal] (43 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banten tv (720p) [not 24/7]
    3. Banyumas tv (720p) [not 24/7]
    4. Bn channel (720p)
    5. Caruban tv (1080p)
    6. Daai tv
    7. Dens tv learning
    8. Dhamma tv (720p) [not 24/7]
    9. Dhoho tv (720p)
    10. Duta tv (360p) [not 24/7]
    11. Efarina tv (720p)
    12. Garuda tv (1080p)
    13. Indonesiana tv
    14. Izzah tv (480p)
    15. Jawa pos tv jakarta (720p)
    16. Jogja istimewa tv (720p)
    17. Jogja tv (720p) [not 24/7]
    18. Jowo
    19. Kawanua tv (720p)
    20. Kompas tv
    21. Madu tv (576p)
    22. Magna channel (1080p) [not 24/7]
    23. Metro tv
    24. Moji tv
    25. Mqtv (720p) [not 24/7]
    26. Nhk world japan
    27. Pontv (720p)
    28. R tv
    29. Radar tasikmalaya tv (720p) [not 24/7]
    30. Rodja tv (720p)
    31. Salira tv (720p)
    32. Smtv (720p) [not 24/7]
    33. Stara tv (720p)
    34. Stara tv bandung (1080p)
    35. Stara tv cianjur (720p)
    36. Stara tv malang (1080p)
    37. Tatv (720p) [not 24/7]
    38. Tv one
    39. Tv tabalong (720p) [not 24/7]
    40. Tv9 nusantara (720p)
    41. Tvri jawa barat (480p)
    42. Tvri world
    43. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (150 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ANTV HD
    4. Abadan
    5. Ahsan TV
    6. Ajman TV (1080p)
    7. Al Qamar TV (1080p)
    8. Anadolu Net TV (1080p)
    9. Angel TV Indonesia (720p)
    10. Ashiil TV (480p)
    11. Astro Blitar TV (720p)
    12. Atomic Academy TV (480p)
    13. Atomic TV (360p)
    14. Azan TV
    15. BALI TV
    16. BBC LIFESTYLE
    17. BN Channel (ChannelFeed)
    18. BRTV (720p)
    19. BTV (Channel Feed)
    20. BTV (V+)
    21. Baan Baan TV 73
    22. Balapan HD (1080p)
    23. Bali TV
    24. Balikpapan TV (720p)
    25. Bandung TV
    26. Banjar TV (720p) [Not 24/7]
    27. Batam TV (480p) [Not 24/7]
    28. Berita Satu
    29. Bungo TV
    30. CNBC Indonesia (ChannelFeed)
    31. CNN Indonesia (ChannelFeed)
    32. Canal 24 Horas (720p)
    33. Cao Bằng TV (720p)
    34. CelebritiesTV (V+)
    35. Clan Internacional Americas (1080p) [Geo-blocked]
    36. DAAI TV (Dens)
    37. DMI TV (576i)
    38. Davika TV (480p)
    39. EmanTv (1080p)
    40. Entertainment (V+)
    41. Fajar TV (720p) [Not 24/7]
    42. Ficom Channel
    43. Flik
    44. Food Travel (V+)
    45. GTV
    46. Garuda TV (Flashcon)
    47. Hanacaraka TV (V+)
    48. Hmong Star TV (720p) [Not 24/7]
    49. Hyder TV (720p)
    50. I Am Channel (576p)
    51. IDX (V+)
    52. Indonesia Movie Channel (V+)
    53. Indosiar
    54. Indosiar HD
    55. Inter TV (1080p)
    56. Iunior TV (1080p)
    57. JAKTV
    58. JTV (720p)
    59. JTV (V+)
    60. JTV Kediri (1080p) [Not 24/7]
    61. JTV Madiun
    62. JTV Madura (480p) [Not 24/7]
    63. JTV Malang
    64. Jagantara TV
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
    76. MTV Ridiculousness (720p)
    77. Madani TV (720p)
    78. Matrix TV Yogyakarta (720p)
    79. MetroTV (Flashcon)
    80. Myanmar International TV
    81. Nusantara TV (ChannelFeed)
    82. Omid e Iran TV
    83. Outdoor Channel (1080p)
    84. PKTV (480p)
    85. Peer TV Sudtirol (1080p)
    86. RCTV (Indonesia) (720p) [Not 24/7]
    87. RRI Net (1080p)
    88. Radio 51 TV
    89. Rajawali TV
    90. Regio TV (406p)
    91. Riau TV (1080p) [Not 24/7]
    92. Rinjani TV
    93. SCTV (DASH/MPD)
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
    106. TV Mu (720p) [Not 24/7]
    107. TVE Star (576p)
    108. TVE Star HD (1080p)
    109. TVOne (V+)
    110. TVRI (1080i)
    111. TVRI Aceh (720p)
    112. TVRI Bali (480p)
    113. TVRI Bangka Belitung (480p)
    114. TVRI Bengkulu (480p)
    115. TVRI Gorontalo (480p)
    116. TVRI Jakarta (576i) [Not 24/7]
    117. TVRI Jambi (720p) [Not 24/7]
    118. TVRI Jawa Tengah (720p)
    119. TVRI Kalimantan Barat (480p)
    120. TVRI Kalimantan Selatan (720p)
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
    137. TVRI WORLD
    138. TVRI West Papua (1080p)
    139. TVRI Yogyakarta (720p)
    140. The Indonesia Channel (1080p)
    141. Timor TV
    142. Trans7 HD
    143. TransTV HD
    144. U Channel
    145. UCL (720p)
    146. VTV
    147. Vision Prime (V+)
    148. dTVi
    149. iNews HD
    150. Хузур ТВ (1080p) [Not 24/7]

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
