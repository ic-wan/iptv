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

  📁 Grup: [Lokal] (44 Channel)
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
    27. Padang tv (720p) [not 24/7]
    28. Pontv (720p)
    29. R tv
    30. Radar tasikmalaya tv (720p) [not 24/7]
    31. Rodja tv (720p)
    32. Salira tv (720p)
    33. Smtv (720p) [not 24/7]
    34. Stara tv (720p)
    35. Stara tv bandung (1080p)
    36. Stara tv cianjur (720p)
    37. Stara tv malang (1080p)
    38. Tatv (720p) [not 24/7]
    39. Tv one
    40. Tv tabalong (720p) [not 24/7]
    41. Tv9 nusantara (720p)
    42. Tvri jawa barat (480p)
    43. Tvri world
    44. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (176 Channel)
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
    25. Balapan International (1080p)
    26. Bali TV
    27. Balikpapan TV (720p)
    28. Bandung TV
    29. Banjar TV (720p) [Not 24/7]
    30. Batam TV (480p) [Not 24/7]
    31. Berita Satu
    32. Berita Satu (Maxstream)
    33. Berita Satu (Transcorp)
    34. Bungo TV
    35. CNBC Indonesia (ChannelFeed)
    36. CNBC Indonesia (Transcorp)
    37. CNN Indonesia (ChannelFeed)
    38. CNN Indonesia (Transcorp)
    39. Canal 24 Horas (720p)
    40. Cao Bằng TV (720p)
    41. CelebritiesTV (V+)
    42. Clan Internacional Americas (1080p) [Geo-blocked]
    43. DAAI TV (Dens)
    44. DMI TV (576i)
    45. EmanTv (1080p)
    46. Entertainment (V+)
    47. Food Travel (V+)
    48. GTV
    49. Garuda TV (Flashcon)
    50. Global TV (Transcorp)
    51. Hanacaraka TV (V+)
    52. Hmong Star TV (720p) [Not 24/7]
    53. Hyder TV (720p)
    54. I Am Channel (576p)
    55. IDX (Maxstream)
    56. IDX (V+)
    57. Indonesia Movie Channel (V+)
    58. Indosiar
    59. Indosiar (Maxstream)
    60. Indosiar (Transcorp)
    61. Indosiar HD
    62. Inter TV (1080p)
    63. Iunior TV (1080p)
    64. JAKTV
    65. JTV (720p)
    66. JTV (V+)
    67. JTV Madiun
    68. JTV Malang
    69. Jagantara TV
    70. Kompas TV HD (Maxstream)
    71. Kompas TV HD (Transcorp)
    72. Kordia TV (1080p)
    73. La 2
    74. Lingkar TV
    75. Love the Planet (1080p)
    76. MAGNA Channel (DensTV)
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
    88. Metro TV (Transcorp)
    89. MetroTV (DensTV)
    90. MetroTV (Flashcon)
    91. Myanmar International TV
    92. Nusantara TV (ChannelFeed)
    93. Nusantara TV (Maxstream)
    94. Omid e Iran TV
    95. Outdoor Channel (1080p)
    96. PKTV (480p)
    97. Peer TV Sudtirol (1080p)
    98. RCTI (Transcorp)
    99. RCTV (Indonesia) (720p) [Not 24/7]
    100. RRI Net (1080p)
    101. RTV (Maxstream)
    102. RTV (Transcorp)
    103. Radar Lampung TV (480p)
    104. Radio 51 TV
    105. Rajawali TV
    106. Regio TV (406p)
    107. Riau TV (1080p) [Not 24/7]
    108. Rinjani TV
    109. SCTV (Maxstream)
    110. SCTV (Transcorp)
    111. SCTV HD
    112. SIN PO TV (Maxstream)
    113. SMTV (720p)
    114. STV (Indonesia) (720p) [Not 24/7]
    115. Salam TV (720p)
    116. Sangaji TV (720p)
    117. SindoNews
    118. SindoNews (Maxstream)
    119. SindoNews (V+)
    120. Sooriyan TV (1080p)
    121. Sriwijaya TV (720p) [Not 24/7]
    122. Stara TV Bojonegoro (720p)
    123. Stara TV Jakarta (1080p)
    124. Stara TV Parahyangan (720p)
    125. TV Mu (720p) [Not 24/7]
    126. TVE Star (576p)
    127. TVE Star HD (1080p)
    128. TVOne (Transcorp)
    129. TVOne (V+)
    130. TVRI (1080i)
    131. TVRI Aceh (720p)
    132. TVRI Bali (480p)
    133. TVRI Bangka Belitung (480p)
    134. TVRI Bengkulu (480p)
    135. TVRI Gorontalo (480p)
    136. TVRI Jakarta (576i) [Not 24/7]
    137. TVRI Jambi (720p) [Not 24/7]
    138. TVRI Jawa Tengah (720p)
    139. TVRI Jawa Timur (720p)
    140. TVRI Kalimantan Barat (480p)
    141. TVRI Kalimantan Selatan (720p)
    142. TVRI Kalimantan Tengah (480p)
    143. TVRI Kalimantan Timur (720p)
    144. TVRI Lampung (720p)
    145. TVRI Maluku (480p)
    146. TVRI North Sulawesi (1080p)
    147. TVRI North Sumatra (1080p)
    148. TVRI Nusa Tenggara Barat (720p)
    149. TVRI Nusa Tenggara Timur (480p)
    150. TVRI Papua (480p)
    151. TVRI Riau
    152. TVRI Riau (720p) [Not 24/7]
    153. TVRI Sulawesi Barat (720p)
    154. TVRI Sulawesi Selatan (480p)
    155. TVRI Sulawesi Tengah (720p)
    156. TVRI Sulawesi Tenggara (480p)
    157. TVRI Sumatera Barat (720p)
    158. TVRI Sumatera Selatan (480p)
    159. TVRI WORLD
    160. TVRI West Papua (1080p)
    161. TVRI World (Maxstream)
    162. TVRI Yogyakarta (720p)
    163. The Indonesia Channel (1080p)
    164. Timor TV
    165. Trans7 (Transcorp)
    166. Trans7 HD
    167. TransTV (Transcorp)
    168. TransTV HD
    169. U Channel
    170. UCL (720p)
    171. VTV
    172. Vision Prime (V+)
    173. dTVi
    174. iNews (Maxstream)
    175. iNews HD
    176. Хузур ТВ (1080p) [Not 24/7]

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
