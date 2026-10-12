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

  📁 Grup: [Lokal (auto)] (170 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV
    5. ANTV HD
    6. Abadan
    7. Ajman TV (1080p)
    8. Al Qamar TV (1080p)
    9. Anadolu Net TV (1080p)
    10. Angel TV Indonesia (720p)
    11. Ashiil TV (480p)
    12. Astro Blitar TV (720p)
    13. Atambua TV (720p)
    14. Atomic Academy TV (480p)
    15. Atomic TV (360p)
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
    27. Berita Satu
    28. Bioskop Indonesia
    29. Bungo TV
    30. CNBC Indonesia
    31. CNBC Indonesia (ChannelFeed)
    32. CNN Indonesia
    33. CNN Indonesia (ChannelFeed)
    34. Canal 24 Horas (720p)
    35. Cao Bằng TV (720p)
    36. CelebritiesTV (V+)
    37. Clan Internacional Americas (1080p) [Geo-blocked]
    38. DAAI TV
    39. DAAI TV (Dens)
    40. DMI TV (576i)
    41. EmanTv (1080p)
    42. Entertainment (V+)
    43. Fashion TV
    44. Ficom Channel
    45. Food Travel (V+)
    46. GTV
    47. GTV (Indonesia) HD (1080p)
    48. Garuda TV (1080p)
    49. Garuda TV (Flashcon)
    50. Hanacaraka TV (V+)
    51. Hmong Star TV (720p) [Not 24/7]
    52. Hyder TV (720p)
    53. I Am Channel (576p)
    54. IDX (V+)
    55. Indonesia Movie Channel (V+)
    56. Indosiar
    57. Indosiar HD
    58. Indosiar HD (1080p)
    59. Inter TV (1080p)
    60. Iunior TV (1080p)
    61. JTV (V+)
    62. JTV Kediri (1080p) [Not 24/7]
    63. JTV Madiun
    64. JTV Madura (480p) [Not 24/7]
    65. JTV Malang
    66. Jagantara TV
    67. Kompas TV
    68. Kordia TV (1080p)
    69. La 2
    70. Lingkar TV
    71. Love the Planet (1080p)
    72. MAGNA Channel (DensTV)
    73. MAGNA TV (ChannelFeed)
    74. MBG TV (1080p)
    75. MDTV
    76. MDTV (DensTV)
    77. MNCTV
    78. MNCTV HD
    79. MOJI TV HD (Alt 3 - DensTV flashcon)
    80. Madani TV (720p)
    81. Metro TV
    82. MetroTV (DensTV)
    83. MetroTV (Flashcon)
    84. Nusantara TV (ChannelFeed)
    85. Omid e Iran TV
    86. Outdoor Channel (1080p)
    87. PKTV (480p)
    88. Peer TV Sudtirol (1080p)
    89. RCTI
    90. RCTI HD (1080p)
    91. RCTV (Indonesia) (720p) [Not 24/7]
    92. RRI Net (1080p)
    93. RTV
    94. Radar Lampung TV (480p)
    95. Radio 51 TV
    96. Rajawali TV
    97. Regio TV (406p)
    98. Riau TV (1080p) [Not 24/7]
    99. Rinjani TV
    100. SCTV
    101. SCTV (DASH/MPD)
    102. SCTV HD
    103. SMTV (720p)
    104. STV (Indonesia) (720p) [Not 24/7]
    105. Salam TV (720p)
    106. Sangaji TV (720p)
    107. SindoNews
    108. SindoNews (V+)
    109. Sooriyan TV (1080p)
    110. Sriwijaya TV (720p) [Not 24/7]
    111. Stara TV Bojonegoro (720p)
    112. Stara TV Jakarta (1080p)
    113. Stara TV Parahyangan (720p)
    114. Szlagier TV
    115. TLC HD
    116. TVE Internacional America (576p) [Geo-blocked]
    117. TVE Star (576p)
    118. TVE Star HD (1080p)
    119. TVOne
    120. TVOne (V+)
    121. TVRI
    122. TVRI (1080i)
    123. TVRI (1080p)
    124. TVRI Aceh (720p)
    125. TVRI Bali (480p)
    126. TVRI Bangka Belitung (480p)
    127. TVRI Bengkulu (480p)
    128. TVRI Gorontalo (480p)
    129. TVRI Jakarta (576i) [Not 24/7]
    130. TVRI Jambi (720p) [Not 24/7]
    131. TVRI Jawa Tengah (720p)
    132. TVRI Jawa Timur (720p)
    133. TVRI Kalimantan Barat (480p)
    134. TVRI Kalimantan Selatan (720p)
    135. TVRI Kalimantan Tengah (480p)
    136. TVRI Kalimantan Timur (720p)
    137. TVRI Lampung (720p)
    138. TVRI Maluku (480p)
    139. TVRI North Sulawesi (1080p)
    140. TVRI North Sumatra (1080p)
    141. TVRI Nusa Tenggara Barat (720p)
    142. TVRI Nusa Tenggara Timur (480p)
    143. TVRI Papua (480p)
    144. TVRI Riau
    145. TVRI Riau (720p) [Not 24/7]
    146. TVRI Sport
    147. TVRI Sport (1080p)
    148. TVRI Sulawesi Barat (720p)
    149. TVRI Sulawesi Selatan (480p)
    150. TVRI Sulawesi Tengah (720p)
    151. TVRI Sulawesi Tenggara (480p)
    152. TVRI Sumatera Barat (720p)
    153. TVRI Sumatera Selatan (480p)
    154. TVRI West Papua (1080p)
    155. TVRI Yogyakarta (720p)
    156. The Indonesia Channel (1080p)
    157. Timor TV
    158. Trans7 (Transcorp)
    159. Trans7 HD
    160. TransTV (Transcorp)
    161. TransTV HD
    162. U Channel
    163. UCL (1080p)
    164. UCL (720p)
    165. VTV
    166. Vision Prime (V+)
    167. Warner TV Asia (720p)
    168. iNews HD
    169. iNews HD (1080p)
    170. Хузур ТВ (1080p) [Not 24/7]

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
