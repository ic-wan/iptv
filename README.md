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

  📁 Grup: [Indihome] (7 Channel)
  ----------------------------------------
    1. Berita satu
    2. I news
    3. Jtv
    4. Kompas tv
    5. Max sport
    6. Rtv
    7. Sctv

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
    6. Daai tv
    7. Dens tv learning
    8. Dhamma tv (720p) [not 24/7]
    9. Dhoho tv (720p)
    10. Duta tv (360p) [not 24/7]
    11. Efarina tv (720p)
    12. Indonesiana tv
    13. Jawa pos tv jakarta (720p)
    14. Jogja istimewa tv (720p)
    15. Jogja tv (720p) [not 24/7]
    16. Jowo
    17. Kawanua tv (720p)
    18. Kompas tv
    19. Madu tv (576p)
    20. Magna channel (1080p) [not 24/7]
    21. Metro tv
    22. Moji tv
    23. Mqtv (720p) [not 24/7]
    24. Nhk world japan
    25. Padang tv (720p) [not 24/7]
    26. Pontv (720p)
    27. R tv
    28. Radar tasikmalaya tv (720p) [not 24/7]
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

  📁 Grup: [Lokal (auto)] (165 Channel)
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
    29. Berita Satu (Maxstream)
    30. Bungo TV
    31. CNBC Indonesia (ChannelFeed)
    32. CNN Indonesia (ChannelFeed)
    33. Canal 24 Horas (720p)
    34. Cao Bằng TV (720p)
    35. CelebritiesTV (V+)
    36. Clan Internacional Americas (1080p) [Geo-blocked]
    37. DAAI TV
    38. DAAI TV (Dens)
    39. DMI TV (576i)
    40. EmanTv (1080p)
    41. Entertainment (V+)
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
    52. IDX (Maxstream)
    53. IDX (V+)
    54. Indonesia Movie Channel (V+)
    55. Indosiar
    56. Indosiar (Maxstream)
    57. Indosiar HD
    58. Inter TV (1080p)
    59. Iunior TV (1080p)
    60. JAKTV
    61. JTV (720p)
    62. JTV (V+)
    63. JTV Kediri (1080p) [Not 24/7]
    64. JTV Madiun
    65. JTV Madura (480p) [Not 24/7]
    66. JTV Malang
    67. Jagantara TV
    68. Kompas TV HD (Maxstream)
    69. Kordia TV (1080p)
    70. La 2
    71. Lingkar TV
    72. Love the Planet (1080p)
    73. MAGNA Channel (DensTV)
    74. MAGNA TV (ChannelFeed)
    75. MBG TV (1080p)
    76. MDTV
    77. MDTV (DensTV)
    78. MOJI TV HD (Alt 3 - DensTV flashcon)
    79. Madani TV (720p)
    80. Matrix TV Yogyakarta (720p)
    81. MetroTV (DensTV)
    82. MetroTV (Flashcon)
    83. Nusantara TV (ChannelFeed)
    84. Nusantara TV (Maxstream)
    85. Omid e Iran TV
    86. Outdoor Channel (1080p)
    87. PKTV (480p)
    88. Peer TV Sudtirol (1080p)
    89. RCTV (Indonesia) (720p) [Not 24/7]
    90. RTV (Maxstream)
    91. Radio 51 TV
    92. Rajawali TV
    93. Regio TV (406p)
    94. Riau TV (1080p) [Not 24/7]
    95. Rinjani TV
    96. SCTV (DASH/MPD)
    97. SCTV (Maxstream)
    98. SCTV HD
    99. SIN PO TV (Maxstream)
    100. SMTV (720p)
    101. STV (Indonesia) (720p) [Not 24/7]
    102. Salam TV (720p)
    103. Sangaji TV (720p)
    104. SindoNews
    105. SindoNews (Maxstream)
    106. SindoNews (V+)
    107. Sooriyan TV (1080p)
    108. Sriwijaya TV (720p) [Not 24/7]
    109. Stara TV Bojonegoro (720p)
    110. Stara TV Jakarta (1080p)
    111. Stara TV Parahyangan (720p)
    112. Szlagier TV
    113. TLC HD
    114. TV Mu (720p) [Not 24/7]
    115. TVE Internacional America (576p) [Geo-blocked]
    116. TVE Star (576p)
    117. TVE Star HD (1080p)
    118. TVOne (V+)
    119. TVRI
    120. TVRI (1080i)
    121. TVRI Aceh (720p)
    122. TVRI Bali (480p)
    123. TVRI Bangka Belitung (480p)
    124. TVRI Bengkulu (480p)
    125. TVRI Gorontalo (480p)
    126. TVRI Jakarta (576i) [Not 24/7]
    127. TVRI Jambi (720p) [Not 24/7]
    128. TVRI Jawa Tengah (720p)
    129. TVRI Jawa Timur (720p)
    130. TVRI Kalimantan Barat (480p)
    131. TVRI Kalimantan Selatan (720p)
    132. TVRI Kalimantan Tengah (480p)
    133. TVRI Kalimantan Timur (720p)
    134. TVRI Lampung (720p)
    135. TVRI Maluku (480p)
    136. TVRI North Sulawesi (1080p)
    137. TVRI North Sumatra (1080p)
    138. TVRI Nusa Tenggara Barat (720p)
    139. TVRI Nusa Tenggara Timur (480p)
    140. TVRI Papua (480p)
    141. TVRI Riau
    142. TVRI Riau (720p) [Not 24/7]
    143. TVRI Sulawesi Barat (720p)
    144. TVRI Sulawesi Selatan (480p)
    145. TVRI Sulawesi Tengah (720p)
    146. TVRI Sulawesi Tenggara (480p)
    147. TVRI Sumatera Barat (720p)
    148. TVRI Sumatera Selatan (480p)
    149. TVRI WORLD
    150. TVRI West Papua (1080p)
    151. TVRI World (Maxstream)
    152. TVRI Yogyakarta (720p)
    153. The Indonesia Channel (1080p)
    154. Timor TV
    155. Trans7 (Transcorp)
    156. Trans7 HD
    157. TransTV (Transcorp)
    158. U Channel
    159. UCL (1080p)
    160. UCL (720p)
    161. VTV
    162. Vision Prime (V+)
    163. iNews (Maxstream)
    164. iNews HD
    165. Хузур ТВ (1080p) [Not 24/7]

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
