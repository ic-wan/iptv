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
    42. Tvri jawa timur (720p)
    43. Tvri world
    44. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (177 Channel)
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
    13. Atambua TV (720p)
    14. Atomic Academy TV (480p)
    15. Atomic TV (360p)
    16. Azan TV
    17. BALI TV
    18. BBC LIFESTYLE
    19. BIOSKOP INDONESIA (Transcorp)
    20. BN Channel (ChannelFeed)
    21. BRTV (720p)
    22. BTV (Channel Feed)
    23. BTV (V+)
    24. Baan Baan TV 73
    25. Balapan HD (1080p)
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
    47. Flik
    48. Food Travel (V+)
    49. GTV
    50. Garuda TV (Flashcon)
    51. Global TV (Transcorp)
    52. Hanacaraka TV (V+)
    53. Hmong Star TV (720p) [Not 24/7]
    54. Hyder TV (720p)
    55. I Am Channel (576p)
    56. IDX (Maxstream)
    57. IDX (V+)
    58. Indonesia Movie Channel (V+)
    59. Indosiar
    60. Indosiar (Transcorp)
    61. Indosiar HD
    62. Inter TV (1080p)
    63. Iunior TV (1080p)
    64. JAKTV
    65. JTV (720p)
    66. JTV (V+)
    67. JTV Kediri (1080p) [Not 24/7]
    68. JTV Madiun
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
    89. Metro TV
    90. Metro TV (Transcorp)
    91. MetroTV (DensTV)
    92. MetroTV (Flashcon)
    93. Myanmar International TV
    94. Nusantara TV (ChannelFeed)
    95. Nusantara TV (Maxstream)
    96. Omid e Iran TV
    97. Outdoor Channel (1080p)
    98. PKTV (480p)
    99. Peer TV Sudtirol (1080p)
    100. RCTI (Transcorp)
    101. RCTV (Indonesia) (720p) [Not 24/7]
    102. RRI Net (1080p)
    103. RTV (Maxstream)
    104. RTV (Transcorp)
    105. Radio 51 TV
    106. Rajawali TV
    107. Regio TV (406p)
    108. Riau TV (1080p) [Not 24/7]
    109. Rinjani TV
    110. SCTV (DASH/MPD)
    111. SCTV (Transcorp)
    112. SCTV HD
    113. SIN PO TV (Maxstream)
    114. SMTV (720p)
    115. STV (Indonesia) (720p) [Not 24/7]
    116. Salam TV (720p)
    117. Sangaji TV (720p)
    118. SindoNews
    119. SindoNews (Maxstream)
    120. SindoNews (V+)
    121. Sooriyan TV (1080p)
    122. Sriwijaya TV (720p) [Not 24/7]
    123. Stara TV Bojonegoro (720p)
    124. Stara TV Jakarta (1080p)
    125. Stara TV Parahyangan (720p)
    126. TV Mu (720p) [Not 24/7]
    127. TVE Star (576p)
    128. TVE Star HD (1080p)
    129. TVOne (Transcorp)
    130. TVOne (V+)
    131. TVRI (1080i)
    132. TVRI Aceh (720p)
    133. TVRI Bali (480p)
    134. TVRI Bangka Belitung (480p)
    135. TVRI Bengkulu (480p)
    136. TVRI Gorontalo (480p)
    137. TVRI Jakarta (576i) [Not 24/7]
    138. TVRI Jambi (720p) [Not 24/7]
    139. TVRI Jawa Tengah (720p)
    140. TVRI Jawa Timur (720p)
    141. TVRI Kalimantan Barat (480p)
    142. TVRI Kalimantan Selatan (720p)
    143. TVRI Kalimantan Tengah (480p)
    144. TVRI Kalimantan Timur (720p)
    145. TVRI Lampung (720p)
    146. TVRI Maluku (480p)
    147. TVRI North Sulawesi (1080p)
    148. TVRI North Sumatra (1080p)
    149. TVRI Nusa Tenggara Barat (720p)
    150. TVRI Nusa Tenggara Timur (480p)
    151. TVRI Papua (480p)
    152. TVRI Riau
    153. TVRI Riau (720p) [Not 24/7]
    154. TVRI Sulawesi Barat (720p)
    155. TVRI Sulawesi Selatan (480p)
    156. TVRI Sulawesi Tengah (720p)
    157. TVRI Sulawesi Tenggara (480p)
    158. TVRI Sumatera Barat (720p)
    159. TVRI Sumatera Selatan (480p)
    160. TVRI WORLD
    161. TVRI West Papua (1080p)
    162. TVRI World (Maxstream)
    163. TVRI Yogyakarta (720p)
    164. The Indonesia Channel (1080p)
    165. Timor TV
    166. Trans7 (Transcorp)
    167. Trans7 HD
    168. TransTV (Transcorp)
    169. TransTV HD
    170. U Channel
    171. UCL (720p)
    172. VTV
    173. Vision Prime (V+)
    174. Warner TV (Transcorp)
    175. iNews (Maxstream)
    176. iNews HD
    177. Хузур ТВ (1080p) [Not 24/7]

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
