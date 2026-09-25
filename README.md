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

  📁 Grup: [Kids] (6 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Kidsflix (1080p) [not 24/7]
    4. Moonbug kids (1080p)
    5. Pbs kids
    6. Vtv (720p)

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
    14. Jawa pos tv jakarta (720p)
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
    29. Radio kita tv (1080p)
    30. Salira tv (720p)
    31. Smtv (720p) [not 24/7]
    32. Stara tv (720p)
    33. Stara tv bandung (1080p)
    34. Stara tv cianjur (720p)
    35. Stara tv malang (1080p)
    36. Tatv (720p) [not 24/7]
    37. Tv one
    38. Tv tabalong (720p) [not 24/7]
    39. Tv9 nusantara (720p)
    40. Tvri jawa barat (480p)
    41. Tvri jawa timur (720p)
    42. Tvri world
    43. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (167 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ANTV HD
    4. ANTV HD (Transcorp)
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
    15. Azan TV
    16. BALI TV
    17. BBC LIFESTYLE
    18. BIOSKOP INDONESIA (Transcorp)
    19. BN Channel (ChannelFeed)
    20. BRTV (720p)
    21. BTV (Channel Feed)
    22. BTV (V+)
    23. Baan Baan TV 73
    24. Balapan HD (1080p)
    25. Bali TV
    26. Balikpapan TV (720p)
    27. Bandung TV
    28. Banjar TV (720p) [Not 24/7]
    29. Batam TV (480p) [Not 24/7]
    30. Berita Satu
    31. Berita Satu (Transcorp)
    32. Bungo TV
    33. CNBC Indonesia (ChannelFeed)
    34. CNBC Indonesia (Transcorp)
    35. CNN Indonesia (ChannelFeed)
    36. CNN Indonesia (Transcorp)
    37. Canal 24 Horas (720p)
    38. Cao Bằng TV (720p)
    39. CelebritiesTV (V+)
    40. Clan Internacional Americas (1080p) [Geo-blocked]
    41. DAAI TV (Dens)
    42. DMI TV (576i)
    43. Davika TV (480p)
    44. EmanTv (1080p)
    45. Entertainment (V+)
    46. Fajar TV (720p) [Not 24/7]
    47. Ficom Channel
    48. Food Travel (V+)
    49. GTV
    50. GTV (Transcorp)
    51. Garuda TV (Flashcon)
    52. Hanacaraka TV (V+)
    53. Hmong Star TV (720p) [Not 24/7]
    54. Hyder TV (720p)
    55. I Am Channel (576p)
    56. IDX (V+)
    57. Indonesia Movie Channel (V+)
    58. Indosiar
    59. Indosiar (Transcorp)
    60. Indosiar HD
    61. Inter TV (1080p)
    62. Iunior TV (1080p)
    63. JAKTV
    64. JTV (720p)
    65. JTV (V+)
    66. JTV Kediri (1080p) [Not 24/7]
    67. JTV Madiun
    68. JTV Malang
    69. Jagantara TV
    70. Kompas TV HD (Transcorp)
    71. Kordia TV (1080p)
    72. La 2
    73. Lingkar TV
    74. Love the Planet (1080p)
    75. MAGNA Channel (DensTV)
    76. MAGNA Channel (Flashcon)
    77. MAGNA TV (ChannelFeed)
    78. MBG TV (1080p)
    79. MDTV
    80. MDTV (DensTV)
    81. MDTV (Transcorp)
    82. MNC TV (Transcorp)
    83. MOJI TV HD (Alt 3 - DensTV flashcon)
    84. MTV Ridiculousness
    85. MTV Ridiculousness (720p)
    86. Madani TV (720p)
    87. Matrix TV Yogyakarta (720p)
    88. Metro TV
    89. Metro TV (Transcorp)
    90. MetroTV (Flashcon)
    91. Myanmar International TV
    92. Nusantara TV (ChannelFeed)
    93. Omid e Iran TV
    94. Outdoor Channel (1080p)
    95. PKTV (480p)
    96. Peer TV Sudtirol (1080p)
    97. RCTI (Transcorp)
    98. RCTV (Indonesia) (720p) [Not 24/7]
    99. RRI Net (1080p)
    100. RTV (Transcorp)
    101. Radio 51 TV
    102. Rajawali TV
    103. Regio TV (406p)
    104. Riau TV (1080p) [Not 24/7]
    105. SCTV (DASH/MPD)
    106. SCTV (Transcorp)
    107. SCTV HD
    108. SMTV (720p)
    109. STV (Indonesia) (720p) [Not 24/7]
    110. Salam TV (720p)
    111. Sangaji TV (720p)
    112. SindoNews
    113. SindoNews (V+)
    114. Sooriyan TV (1080p)
    115. Sriwijaya TV (720p) [Not 24/7]
    116. Stara TV Bojonegoro (720p)
    117. Stara TV Jakarta (1080p)
    118. Stara TV Parahyangan (720p)
    119. TV Mu (720p) [Not 24/7]
    120. TVE Star (576p)
    121. TVE Star HD (1080p)
    122. TVOne (Transcorp)
    123. TVOne (V+)
    124. TVRI (1080i)
    125. TVRI Aceh (720p)
    126. TVRI Bali (480p)
    127. TVRI Bangka Belitung (480p)
    128. TVRI Bengkulu (480p)
    129. TVRI Gorontalo (480p)
    130. TVRI Jakarta (576i) [Not 24/7]
    131. TVRI Jambi (720p) [Not 24/7]
    132. TVRI Jawa Tengah (720p)
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
    146. TVRI Sulawesi Barat (720p)
    147. TVRI Sulawesi Selatan (480p)
    148. TVRI Sulawesi Tengah (720p)
    149. TVRI Sulawesi Tenggara (480p)
    150. TVRI Sumatera Barat (720p)
    151. TVRI Sumatera Selatan (480p)
    152. TVRI WORLD
    153. TVRI West Papua (1080p)
    154. TVRI Yogyakarta (720p)
    155. The Indonesia Channel (1080p)
    156. Timor TV
    157. Trans7 (Transcorp)
    158. Trans7 HD
    159. TransTV (Transcorp)
    160. TransTV HD
    161. U Channel
    162. UCL (720p)
    163. VTV
    164. Vision Prime (V+)
    165. Warner TV (Transcorp)
    166. iNews HD
    167. Хузур ТВ (1080p) [Not 24/7]

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
