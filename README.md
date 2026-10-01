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
    14. Jawa pos tv jakarta (720p)
    15. Jogja istimewa tv (720p)
    16. Jogja tv (720p) [not 24/7]
    17. Jowo
    18. Kawanua tv (720p)
    19. Kompas tv
    20. Madu tv (576p)
    21. Magna channel (1080p) [not 24/7]
    22. Metro tv
    23. Moji tv
    24. Mqtv (720p) [not 24/7]
    25. Nhk world japan
    26. Pontv (720p)
    27. R tv
    28. Radar tasikmalaya tv (720p) [not 24/7]
    29. Radio kita tv (1080p)
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

  📁 Grup: [Lokal (auto)] (174 Channel)
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
    31. Berita Satu (Maxstream)
    32. Berita Satu (Transcorp)
    33. Bungo TV
    34. CNBC Indonesia (ChannelFeed)
    35. CNBC Indonesia (Transcorp)
    36. CNN Indonesia (ChannelFeed)
    37. CNN Indonesia (Transcorp)
    38. Canal 24 Horas (720p)
    39. Cao Bằng TV (720p)
    40. CelebritiesTV (V+)
    41. Clan Internacional Americas (1080p) [Geo-blocked]
    42. DAAI TV (Dens)
    43. DMI TV (576i)
    44. EmanTv (1080p)
    45. Entertainment (V+)
    46. Ficom Channel
    47. Food Travel (V+)
    48. GTV
    49. Global TV (Transcorp)
    50. Hanacaraka TV (V+)
    51. Hmong Star TV (720p) [Not 24/7]
    52. Hyder TV (720p)
    53. I Am Channel (576p)
    54. IDX (Maxstream)
    55. IDX (V+)
    56. Indonesia Movie Channel (V+)
    57. Indosiar
    58. Indosiar (Maxstream)
    59. Indosiar (Transcorp)
    60. Indosiar HD
    61. Inter TV (1080p)
    62. Iunior TV (1080p)
    63. JAKTV
    64. JTV (720p)
    65. JTV (V+)
    66. JTV Kediri (1080p) [Not 24/7]
    67. JTV Madiun
    68. JTV Madura (480p) [Not 24/7]
    69. JTV Malang
    70. Jagantara TV
    71. Kompas TV HD (Maxstream)
    72. Kompas TV HD (Transcorp)
    73. Kordia TV (1080p)
    74. La 2
    75. Lingkar TV
    76. Love the Planet (1080p)
    77. MAGNA Channel (DensTV)
    78. MAGNA TV (ChannelFeed)
    79. MBG TV (1080p)
    80. MDTV
    81. MDTV (DensTV)
    82. MDTV (Transcorp)
    83. MNC TV (Transcorp)
    84. MOJI TV HD (Alt 3 - DensTV flashcon)
    85. MTV Ridiculousness
    86. MTV Ridiculousness (720p)
    87. Madani TV (720p)
    88. Matrix TV Yogyakarta (720p)
    89. Metro TV (Transcorp)
    90. MetroTV (DensTV)
    91. MetroTV (Flashcon)
    92. Myanmar International TV
    93. Nusantara TV (ChannelFeed)
    94. Nusantara TV (Maxstream)
    95. Omid e Iran TV
    96. Outdoor Channel (1080p)
    97. PKTV (480p)
    98. Peer TV Sudtirol (1080p)
    99. RCTI (Transcorp)
    100. RCTV (Indonesia) (720p) [Not 24/7]
    101. RRI Net (1080p)
    102. RTV (Maxstream)
    103. RTV (Transcorp)
    104. Radio 51 TV
    105. Regio TV (406p)
    106. Riau TV (1080p) [Not 24/7]
    107. Rinjani TV
    108. SCTV (DASH/MPD)
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
    151. TVRI Riau (720p) [Not 24/7]
    152. TVRI Sulawesi Barat (720p)
    153. TVRI Sulawesi Selatan (480p)
    154. TVRI Sulawesi Tengah (720p)
    155. TVRI Sulawesi Tenggara (480p)
    156. TVRI Sumatera Barat (720p)
    157. TVRI Sumatera Selatan (480p)
    158. TVRI WORLD
    159. TVRI West Papua (1080p)
    160. TVRI World (Maxstream)
    161. TVRI Yogyakarta (720p)
    162. The Indonesia Channel (1080p)
    163. Trans7 (Transcorp)
    164. Trans7 HD
    165. TransTV (Transcorp)
    166. TransTV HD
    167. U Channel
    168. UCL (720p)
    169. VTV
    170. Vision Prime (V+)
    171. dTVi
    172. iNews (Maxstream)
    173. iNews HD
    174. Хузур ТВ (1080p) [Not 24/7]

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
