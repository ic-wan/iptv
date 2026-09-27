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

  📁 Grup: [Lokal (auto)] (162 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ANTV HD
    4. ANTV HD (Transcorp)
    5. ATV (Turkiye) (1080p)
    6. Abadan
    7. Ahsan TV
    8. Ajman TV (1080p)
    9. Al Qamar TV (1080p)
    10. Anadolu Net TV (1080p)
    11. Angel TV Indonesia (720p)
    12. Ashiil TV (480p)
    13. Astro Blitar TV (720p)
    14. Atomic Academy TV (480p)
    15. Atomic TV (360p)
    16. Azan TV
    17. BALI TV
    18. BBC LIFESTYLE
    19. BIOSKOP INDONESIA (Transcorp)
    20. BN Channel (ChannelFeed)
    21. BRTV (720p)
    22. BTV (Channel Feed)
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
    43. EmanTv (1080p)
    44. Entertainment (V+)
    45. Ficom Channel
    46. Flik
    47. Food Travel (V+)
    48. GTV
    49. GTV (Transcorp)
    50. Hanacaraka TV (V+)
    51. Hmong Star TV (720p) [Not 24/7]
    52. Hyder TV (720p)
    53. I Am Channel (576p)
    54. IDX (V+)
    55. Indonesia Movie Channel (V+)
    56. Indosiar (Transcorp)
    57. Indosiar HD
    58. Inter TV (1080p)
    59. Iunior TV (1080p)
    60. JAKTV
    61. JTV (720p)
    62. JTV (V+)
    63. JTV Madiun
    64. JTV Malang
    65. Jagantara TV
    66. Kompas TV HD (Transcorp)
    67. Kordia TV (1080p)
    68. La 2
    69. Lingkar TV
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
    109. Sriwijaya TV (720p) [Not 24/7]
    110. Stara TV Bojonegoro (720p)
    111. Stara TV Jakarta (1080p)
    112. Stara TV Parahyangan (720p)
    113. TV Mu (720p) [Not 24/7]
    114. TVE Star (576p)
    115. TVE Star HD (1080p)
    116. TVOne (Transcorp)
    117. TVOne (V+)
    118. TVRI (1080i)
    119. TVRI Aceh (720p)
    120. TVRI Bali (480p)
    121. TVRI Bangka Belitung (480p)
    122. TVRI Bengkulu (480p)
    123. TVRI Gorontalo (480p)
    124. TVRI Jakarta (576i) [Not 24/7]
    125. TVRI Jambi (720p) [Not 24/7]
    126. TVRI Jawa Tengah (720p)
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
    146. TVRI WORLD
    147. TVRI West Papua (1080p)
    148. TVRI Yogyakarta (720p)
    149. The Indonesia Channel (1080p)
    150. Timor TV
    151. Trans7 (Transcorp)
    152. Trans7 HD
    153. TransTV (Transcorp)
    154. TransTV HD
    155. U Channel
    156. UCL (720p)
    157. VTV
    158. Vision Prime (V+)
    159. Warner TV (Transcorp)
    160. dTVi
    161. iNews HD
    162. Хузур ТВ (1080p) [Not 24/7]

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
