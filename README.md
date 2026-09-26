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

  📁 Grup: [Lokal] (46 Channel)
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
    31. Radio kita tv (1080p)
    32. Rodja tv (720p)
    33. Salira tv (720p)
    34. Smtv (720p) [not 24/7]
    35. Stara tv (720p)
    36. Stara tv bandung (1080p)
    37. Stara tv cianjur (720p)
    38. Stara tv malang (1080p)
    39. Tatv (720p) [not 24/7]
    40. Tv one
    41. Tv tabalong (720p) [not 24/7]
    42. Tv9 nusantara (720p)
    43. Tvri jawa barat (480p)
    44. Tvri jawa timur (720p)
    45. Tvri world
    46. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (163 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ANTV HD
    4. ATV (Turkiye) (1080p)
    5. Abadan
    6. Ahsan TV
    7. Ajman TV (1080p)
    8. Al Qamar TV (1080p)
    9. Anadolu Net TV (1080p)
    10. Angel TV Indonesia (720p)
    11. Ashiil TV (480p)
    12. Atomic Academy TV (480p)
    13. Atomic TV (360p)
    14. Azan TV
    15. BALI TV
    16. BBC LIFESTYLE
    17. BIOSKOP INDONESIA (Transcorp)
    18. BN Channel (ChannelFeed)
    19. BRTV (720p)
    20. BTV (Channel Feed)
    21. BTV (V+)
    22. Baan Baan TV 73
    23. Balapan HD (1080p)
    24. Bali TV
    25. Balikpapan TV (720p)
    26. Bandung TV
    27. Banjar TV (720p) [Not 24/7]
    28. Batam TV (480p) [Not 24/7]
    29. Berita Satu
    30. Berita Satu (Transcorp)
    31. Bungo TV
    32. CNBC Indonesia (ChannelFeed)
    33. CNBC Indonesia (Transcorp)
    34. CNN Indonesia (ChannelFeed)
    35. CNN Indonesia (Transcorp)
    36. Canal 24 Horas (720p)
    37. Cao Bằng TV (720p)
    38. CelebritiesTV (V+)
    39. Clan Internacional Americas (1080p) [Geo-blocked]
    40. DAAI TV (Dens)
    41. DMI TV (576i)
    42. EmanTv (1080p)
    43. Entertainment (V+)
    44. Fajar TV (720p) [Not 24/7]
    45. Ficom Channel
    46. Food Travel (V+)
    47. GTV
    48. GTV (Transcorp)
    49. Garuda TV (Flashcon)
    50. Hanacaraka TV (V+)
    51. Hmong Star TV (720p) [Not 24/7]
    52. Hyder TV (720p)
    53. I Am Channel (576p)
    54. IDX (V+)
    55. Indonesia Movie Channel (V+)
    56. Indosiar
    57. Indosiar (Transcorp)
    58. Indosiar HD
    59. Inter TV (1080p)
    60. Iunior TV (1080p)
    61. JAKTV
    62. JTV (720p)
    63. JTV (V+)
    64. JTV Madiun
    65. JTV Malang
    66. Jagantara TV
    67. Kompas TV HD (Transcorp)
    68. Kordia TV (1080p)
    69. La 2
    70. Love the Planet (1080p)
    71. MAGNA Channel (DensTV)
    72. MAGNA TV (ChannelFeed)
    73. MBG TV (1080p)
    74. MDTV
    75. MDTV (DensTV)
    76. MDTV (Transcorp)
    77. MNC TV (Transcorp)
    78. MOJI TV HD (Alt 3 - DensTV flashcon)
    79. MTV Ridiculousness
    80. MTV Ridiculousness (720p)
    81. Madani TV (720p)
    82. Matrix TV Yogyakarta (720p)
    83. Metro TV
    84. Metro TV (Transcorp)
    85. MetroTV (Flashcon)
    86. Nusantara TV (ChannelFeed)
    87. Omid e Iran TV
    88. Outdoor Channel (1080p)
    89. PKTV (480p)
    90. Peer TV Sudtirol (1080p)
    91. RCTI (Transcorp)
    92. RCTV (Indonesia) (720p) [Not 24/7]
    93. RRI Net (1080p)
    94. RTV (Transcorp)
    95. Radio 51 TV
    96. Rajawali TV
    97. Regio TV (406p)
    98. Riau TV (1080p) [Not 24/7]
    99. Rinjani TV
    100. SCTV (DASH/MPD)
    101. SCTV (Transcorp)
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
    114. TV Mu (720p) [Not 24/7]
    115. TVE Star (576p)
    116. TVE Star HD (1080p)
    117. TVOne (Transcorp)
    118. TVOne (V+)
    119. TVRI (1080i)
    120. TVRI Aceh (720p)
    121. TVRI Bali (480p)
    122. TVRI Bangka Belitung (480p)
    123. TVRI Bengkulu (480p)
    124. TVRI Gorontalo (480p)
    125. TVRI Jakarta (576i) [Not 24/7]
    126. TVRI Jambi (720p) [Not 24/7]
    127. TVRI Jawa Tengah (720p)
    128. TVRI Kalimantan Barat (480p)
    129. TVRI Kalimantan Selatan (720p)
    130. TVRI Kalimantan Tengah (480p)
    131. TVRI Kalimantan Timur (720p)
    132. TVRI Lampung (720p)
    133. TVRI Maluku (480p)
    134. TVRI North Sulawesi (1080p)
    135. TVRI North Sumatra (1080p)
    136. TVRI Nusa Tenggara Barat (720p)
    137. TVRI Nusa Tenggara Timur (480p)
    138. TVRI Papua (480p)
    139. TVRI Riau
    140. TVRI Riau (720p) [Not 24/7]
    141. TVRI Sulawesi Barat (720p)
    142. TVRI Sulawesi Selatan (480p)
    143. TVRI Sulawesi Tengah (720p)
    144. TVRI Sulawesi Tenggara (480p)
    145. TVRI Sumatera Barat (720p)
    146. TVRI Sumatera Selatan (480p)
    147. TVRI WORLD
    148. TVRI West Papua (1080p)
    149. TVRI Yogyakarta (720p)
    150. The Indonesia Channel (1080p)
    151. Timor TV
    152. Trans7 (Transcorp)
    153. Trans7 HD
    154. TransTV (Transcorp)
    155. TransTV HD
    156. U Channel
    157. UCL (720p)
    158. VTV
    159. Vision Prime (V+)
    160. Warner TV (Transcorp)
    161. dTVi
    162. iNews HD
    163. Хузур ТВ (1080p) [Not 24/7]

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
