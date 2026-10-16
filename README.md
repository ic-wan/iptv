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

  📁 Grup: [Lokal] (41 Channel)
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
    27. Radio kita tv (1080p)
    28. Rodja tv (720p)
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

  📁 Grup: [Lokal (auto)] (168 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV
    5. ANTV HD
    6. ATV (Turkiye) (1080p)
    7. Abadan
    8. Ahsan TV
    9. Ajman TV (1080p)
    10. Al Qamar TV (1080p)
    11. Anadolu Net TV (1080p)
    12. Angel TV Indonesia (720p)
    13. Ashiil TV (480p)
    14. Astro Blitar TV (720p)
    15. Atambua TV (720p)
    16. Atomic Academy TV (480p)
    17. Atomic TV (360p)
    18. BBC LIFESTYLE
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
    31. Berita Satu (DensTV)
    32. Bioskop Indonesia
    33. Bungo TV
    34. CNBC Indonesia
    35. CNBC Indonesia (ChannelFeed)
    36. CNN Indonesia
    37. Canal 24 Horas (720p)
    38. Cao Bằng TV (720p)
    39. CelebritiesTV (V+)
    40. Clan Internacional Americas (1080p) [Geo-blocked]
    41. DAAI TV
    42. DAAI TV (Dens)
    43. DMI TV (576i)
    44. Davika TV (480p)
    45. EmanTv (1080p)
    46. Entertainment (V+)
    47. Fajar TV (720p) [Not 24/7]
    48. Fashion TV
    49. Ficom Channel
    50. Food Travel (V+)
    51. GTV
    52. Garuda TV (1080p)
    53. Garuda TV (Flashcon)
    54. Hanacaraka TV (V+)
    55. Hmong Star TV (720p) [Not 24/7]
    56. Hyder TV (720p)
    57. I Am Channel (576p)
    58. IDX (V+)
    59. Indonesia Movie Channel (V+)
    60. Indosiar
    61. Indosiar HD
    62. Inter TV (1080p)
    63. Iunior TV (1080p)
    64. JTV (720p)
    65. JTV (V+)
    66. JTV Kediri (1080p) [Not 24/7]
    67. JTV Madiun
    68. JTV Madura (480p) [Not 24/7]
    69. JTV Malang
    70. Jagantara TV
    71. Jogja TV (720p) [Not 24/7]
    72. Kompas TV
    73. Kordia TV (1080p)
    74. La 2
    75. Lingkar TV
    76. Love the Planet (1080p)
    77. MAGNA Channel (DensTV)
    78. MAGNA TV (ChannelFeed)
    79. MBG TV (1080p)
    80. MDTV
    81. MDTV (DensTV)
    82. MNCTV
    83. MOJI TV HD (Alt 3 - DensTV flashcon)
    84. MTV Ridiculousness
    85. MTV Ridiculousness (United States) LatAm (720p)
    86. Madani TV (720p)
    87. Metro TV
    88. MetroTV (DensTV)
    89. MetroTV (Flashcon)
    90. Nusantara TV (ChannelFeed)
    91. Omid e Iran TV
    92. Outdoor Channel (1080p)
    93. PKTV (480p)
    94. Peer TV Sudtirol (1080p)
    95. RCTI
    96. RRI Net (1080p)
    97. RTV
    98. Radio 51 TV
    99. Rajawali TV
    100. Riau TV (1080p) [Not 24/7]
    101. Rinjani TV
    102. SCTV (DASH/MPD)
    103. SCTV HD
    104. SMTV (720p)
    105. STV (Indonesia) (720p) [Not 24/7]
    106. Salam TV (720p)
    107. Sangaji TV (720p)
    108. SindoNews
    109. SindoNews (V+)
    110. Sooriyan TV (1080p)
    111. Sriwijaya TV (720p) [Not 24/7]
    112. Stara TV Bojonegoro (720p)
    113. Stara TV Jakarta (1080p)
    114. Stara TV Parahyangan (720p)
    115. Szlagier TV
    116. TLC HD
    117. TVE Internacional America (576p) [Geo-blocked]
    118. TVE Star (576p)
    119. TVE Star HD (1080p)
    120. TVOne
    121. TVOne (V+)
    122. TVRI (1080i)
    123. TVRI Aceh (720p)
    124. TVRI Bali (480p)
    125. TVRI Bangka Belitung (480p)
    126. TVRI Bengkulu (480p)
    127. TVRI Gorontalo (480p)
    128. TVRI Jakarta (576i) [Not 24/7]
    129. TVRI Jambi (720p) [Not 24/7]
    130. TVRI Jawa Tengah (720p)
    131. TVRI Jawa Timur (720p)
    132. TVRI Kalimantan Barat (480p)
    133. TVRI Kalimantan Selatan (720p)
    134. TVRI Kalimantan Tengah (480p)
    135. TVRI Kalimantan Timur (720p)
    136. TVRI Lampung (720p)
    137. TVRI Maluku (480p)
    138. TVRI North Sulawesi (1080p)
    139. TVRI North Sumatra (1080p)
    140. TVRI Nusa Tenggara Barat (720p)
    141. TVRI Nusa Tenggara Timur (480p)
    142. TVRI Papua (480p)
    143. TVRI Riau
    144. TVRI Riau (720p) [Not 24/7]
    145. TVRI Sport
    146. TVRI Sulawesi Barat (720p)
    147. TVRI Sulawesi Selatan (480p)
    148. TVRI Sulawesi Tengah (720p)
    149. TVRI Sulawesi Tenggara (480p)
    150. TVRI Sumatera Barat (720p)
    151. TVRI Sumatera Selatan (480p)
    152. TVRI West Papua (1080p)
    153. TVRI Yogyakarta (720p)
    154. The Indonesia Channel (1080p)
    155. Timor TV
    156. Trans7 (Transcorp)
    157. Trans7 HD
    158. TransTV (Transcorp)
    159. TransTV HD
    160. Tropical Moon Urban TV [Not 24/7]
    161. U Channel
    162. UCL (1080p)
    163. UCL (720p)
    164. VTV
    165. Vision Prime (V+)
    166. Warner TV Asia (720p)
    167. iNews HD
    168. Хузур ТВ (1080p) [Not 24/7]

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

=============================================
```
<!-- END_PROGRAM_LIST -->
