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
    26. Radio kita tv (1080p)
    27. Rodja tv (720p)
    28. Salira tv (720p)
    29. Smtv (720p) [not 24/7]
    30. Stara tv (720p)
    31. Stara tv bandung (1080p)
    32. Stara tv cianjur (720p)
    33. Stara tv malang (1080p)
    34. Tv one
    35. Tv tabalong (720p) [not 24/7]
    36. Tv9 nusantara (720p)
    37. Tvri jawa barat (480p)
    38. Tvri world

  📁 Grup: [Lokal (auto)] (161 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV HD
    5. AXN Asia Indonesia
    6. Aathavan TV (720p)
    7. Abadan
    8. Ahsan TV
    9. Ajman TV (1080p)
    10. Al Qamar TV (1080p)
    11. Anadolu Net TV (1080p)
    12. Angel TV Indonesia (720p)
    13. Ashiil TV (480p)
    14. Atomic Academy TV (480p)
    15. Atomic TV (360p)
    16. Azan TV
    17. BBC LIFESTYLE
    18. BN Channel (ChannelFeed)
    19. BRTV (720p)
    20. BTV (Channel Feed)
    21. BTV (V+)
    22. Baan Baan TV 73
    23. Balapan HD (1080p)
    24. Balapan International (1080p)
    25. Bali TV
    26. Balikpapan TV (720p)
    27. Bandung TV
    28. Banjar TV (720p) [Not 24/7]
    29. Banten TV
    30. Batam TV (480p) [Not 24/7]
    31. Berita Satu
    32. Berita Satu (DensTV)
    33. Bir TV (720p)
    34. Bungo TV
    35. CNBC Indonesia (ChannelFeed)
    36. CNN Indonesia
    37. Canal 24 Horas (720p)
    38. Cao Bằng TV (720p)
    39. CelebritiesTV (V+)
    40. Clan Internacional Americas (1080p) [Geo-blocked]
    41. DAAI TV
    42. DAAI TV (Dens)
    43. DMI TV (576i)
    44. Dhoho TV
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
    60. Indosiar HD
    61. Inter TV (1080p)
    62. Iunior TV (1080p)
    63. JTV (720p)
    64. JTV (V+)
    65. JTV Kediri (1080p) [Not 24/7]
    66. JTV Madiun
    67. JTV Madura (480p) [Not 24/7]
    68. JTV Malang
    69. Jagantara TV
    70. Jogja TV (720p) [Not 24/7]
    71. Kordia TV (1080p)
    72. La 2
    73. Lingkar TV
    74. Love the Planet (1080p)
    75. MAGNA Channel (DensTV)
    76. MAGNA TV (ChannelFeed)
    77. MBG TV (1080p)
    78. MDTV
    79. MDTV (DensTV)
    80. MOJI TV HD (Alt 3 - DensTV flashcon)
    81. MTV Ridiculousness
    82. MTV Ridiculousness (United States) LatAm (720p)
    83. Madani TV (720p)
    84. MetroTV (DensTV)
    85. MetroTV (Flashcon)
    86. Myanmar International TV
    87. Nusantara TV (ChannelFeed)
    88. Omid e Iran TV
    89. Outdoor Channel (1080p)
    90. PKTV (480p)
    91. Peer TV Sudtirol (1080p)
    92. RCTV (Indonesia) (720p) [Not 24/7]
    93. RRI Net (1080p)
    94. Radio 51 TV
    95. Rajawali TV
    96. Riau TV (1080p) [Not 24/7]
    97. Rinjani TV
    98. SCTV HD
    99. SMTV (720p)
    100. STV (Indonesia) (720p) [Not 24/7]
    101. Salam TV (720p)
    102. Sangaji TV (720p)
    103. SindoNews
    104. SindoNews (V+)
    105. Sooriyan TV (1080p)
    106. Sriwijaya TV (720p) [Not 24/7]
    107. Stara TV Bojonegoro (720p)
    108. Stara TV Jakarta (1080p)
    109. Stara TV Parahyangan (720p)
    110. Szlagier TV
    111. TLC HD
    112. TVE Internacional America (576p) [Geo-blocked]
    113. TVE Star (576p)
    114. TVE Star HD (1080p)
    115. TVOne (V+)
    116. TVRI
    117. TVRI (1080i)
    118. TVRI Aceh (720p)
    119. TVRI Bali (480p)
    120. TVRI Bangka Belitung (480p)
    121. TVRI Bengkulu (480p)
    122. TVRI Gorontalo (480p)
    123. TVRI Jakarta (576i) [Not 24/7]
    124. TVRI Jambi (720p) [Not 24/7]
    125. TVRI Jawa Tengah (720p)
    126. TVRI Jawa Timur (720p)
    127. TVRI Kalimantan Barat (480p)
    128. TVRI Kalimantan Selatan (720p)
    129. TVRI Kalimantan Tengah (480p)
    130. TVRI Kalimantan Timur (720p)
    131. TVRI Lampung (720p)
    132. TVRI Maluku (480p)
    133. TVRI North Sulawesi (1080p)
    134. TVRI North Sumatra (1080p)
    135. TVRI Nusa Tenggara Barat (720p)
    136. TVRI Nusa Tenggara Timur (480p)
    137. TVRI Papua (480p)
    138. TVRI Riau
    139. TVRI Riau (720p) [Not 24/7]
    140. TVRI Sulawesi Barat (720p)
    141. TVRI Sulawesi Selatan (480p)
    142. TVRI Sulawesi Tengah (720p)
    143. TVRI Sulawesi Tenggara (480p)
    144. TVRI Sumatera Barat (720p)
    145. TVRI Sumatera Selatan (480p)
    146. TVRI West Papua (1080p)
    147. TVRI Yogyakarta (720p)
    148. The Indonesia Channel (1080p)
    149. Trans7 (Transcorp)
    150. Trans7 HD
    151. TransTV (Detik)
    152. TransTV (Transcorp)
    153. TransTV HD
    154. Tropical Moon Urban TV [Not 24/7]
    155. U Channel
    156. UGTV (720p)
    157. VTV
    158. Vision Prime (V+)
    159. Warner TV Asia (720p)
    160. iNews HD
    161. Хузур ТВ (1080p) [Not 24/7]

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
