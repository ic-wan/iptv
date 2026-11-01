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

  📁 Grup: [Lokal] (37 Channel)
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
    10. Jawa pos tv jakarta (720p)
    11. Jogja istimewa tv (720p)
    12. Jowo
    13. Kawanua tv (720p)
    14. Kompas tv
    15. Madu tv (576p)
    16. Magna channel (1080p) [not 24/7]
    17. Metro tv
    18. Moji tv
    19. Mqtv (720p) [not 24/7]
    20. Nhk world japan
    21. Padang tv (720p) [not 24/7]
    22. Pontv (720p)
    23. R tv
    24. Radar tasikmalaya tv (720p) [not 24/7]
    25. Radio kita tv (1080p)
    26. Rodja tv (720p)
    27. Salira tv (720p)
    28. Smtv (720p) [not 24/7]
    29. Stara tv (720p)
    30. Stara tv bandung (1080p)
    31. Stara tv cianjur (720p)
    32. Stara tv malang (1080p)
    33. Tv one
    34. Tv tabalong (720p) [not 24/7]
    35. Tv9 nusantara (720p)
    36. Tvri jawa barat (480p)
    37. Tvri world

  📁 Grup: [Lokal (auto)] (162 Channel)
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
    13. Animal Planet (United Kingdom)
    14. Ashiil TV (480p)
    15. Atomic Academy TV (480p)
    16. Atomic TV (360p)
    17. Azan TV
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
    29. Banten TV
    30. Batam TV (480p) [Not 24/7]
    31. Berita Satu
    32. Berita Satu (DensTV)
    33. Bir TV (720p)
    34. Bungo TV
    35. CNBC Indonesia
    36. CNBC Indonesia (ChannelFeed)
    37. CNN Indonesia
    38. Cao Bằng TV (720p)
    39. CelebritiesTV (V+)
    40. Clan Internacional Americas (1080p) [Geo-blocked]
    41. DAAI TV
    42. DAAI TV (Dens)
    43. DMI TV (576i)
    44. Davika TV (480p)
    45. Dhoho TV
    46. Entertainment (V+)
    47. Fashion TV
    48. Ficom Channel
    49. Food Travel (V+)
    50. GTV
    51. Garuda TV (1080p)
    52. Garuda TV (Flashcon)
    53. Hanacaraka TV (V+)
    54. Hmong Star TV (720p) [Not 24/7]
    55. Hyder TV (720p)
    56. IDX (V+)
    57. Indonesia Movie Channel (V+)
    58. Indosiar HD
    59. Inter TV (1080p)
    60. Iunior TV (1080p)
    61. JTV (720p)
    62. JTV (V+)
    63. JTV Kediri (1080p) [Not 24/7]
    64. JTV Madiun
    65. JTV Malang
    66. Jagantara TV
    67. Jogja TV (720p) [Not 24/7]
    68. Kordia TV (1080p)
    69. La 2
    70. Lingkar TV
    71. Love the Planet (1080p)
    72. MAGNA Channel (DensTV)
    73. MAGNA TV (ChannelFeed)
    74. MBG TV (1080p)
    75. MDTV
    76. MDTV (DensTV)
    77. MOJI TV HD (Alt 3 - DensTV flashcon)
    78. MTV Ridiculousness
    79. MTV Ridiculousness (United States) LatAm (720p)
    80. Madani TV (720p)
    81. MetroTV (DensTV)
    82. MetroTV (Flashcon)
    83. Myanmar International TV
    84. Nusantara TV (ChannelFeed)
    85. Omid e Iran TV
    86. Outdoor Channel (1080p)
    87. PKTV (480p)
    88. Peer TV Sudtirol (1080p)
    89. RCTV (Indonesia) (720p) [Not 24/7]
    90. RRI Net (1080p)
    91. Radar Lampung TV (480p)
    92. Radio 51 TV
    93. Rajawali TV
    94. Riau TV (1080p) [Not 24/7]
    95. Rinjani TV
    96. SCTV HD
    97. SMTV (720p)
    98. STV (Indonesia) (720p) [Not 24/7]
    99. Salam TV (720p)
    100. Sangaji TV (720p)
    101. SindoNews
    102. SindoNews (V+)
    103. Sooriyan TV (1080p)
    104. Sriwijaya TV (720p) [Not 24/7]
    105. Stara TV Bojonegoro (720p)
    106. Stara TV Jakarta (1080p)
    107. Stara TV Parahyangan (720p)
    108. Szlagier TV
    109. TLC HD
    110. TVE Internacional America (576p) [Geo-blocked]
    111. TVE Star (576p)
    112. TVE Star HD (1080p)
    113. TVOne (V+)
    114. TVRI
    115. TVRI (1080i)
    116. TVRI (1080p)
    117. TVRI Aceh (720p)
    118. TVRI Bali (480p)
    119. TVRI Bangka Belitung (480p)
    120. TVRI Bengkulu (480p)
    121. TVRI Gorontalo (480p)
    122. TVRI Jakarta (576i) [Not 24/7]
    123. TVRI Jambi (720p) [Not 24/7]
    124. TVRI Jawa Tengah (720p)
    125. TVRI Jawa Timur (720p)
    126. TVRI Kalimantan Barat (480p)
    127. TVRI Kalimantan Selatan (720p)
    128. TVRI Kalimantan Tengah (480p)
    129. TVRI Kalimantan Timur (720p)
    130. TVRI Lampung (720p)
    131. TVRI Maluku (480p)
    132. TVRI North Sulawesi (1080p)
    133. TVRI North Sumatra (1080p)
    134. TVRI Nusa Tenggara Barat (720p)
    135. TVRI Nusa Tenggara Timur (480p)
    136. TVRI Papua (480p)
    137. TVRI Riau
    138. TVRI Riau (720p) [Not 24/7]
    139. TVRI Sulawesi Barat (720p)
    140. TVRI Sulawesi Selatan (480p)
    141. TVRI Sulawesi Tengah (720p)
    142. TVRI Sulawesi Tenggara (480p)
    143. TVRI Sumatera Barat (720p)
    144. TVRI Sumatera Selatan (480p)
    145. TVRI West Papua (1080p)
    146. TVRI Yogyakarta (720p)
    147. The Indonesia Channel (1080p)
    148. Timor TV
    149. Trans7 (Transcorp)
    150. Trans7 HD
    151. Trans7 HD (Detik)
    152. TransTV (Detik)
    153. TransTV (Transcorp)
    154. TransTV HD
    155. Tropical Moon Urban TV [Not 24/7]
    156. U Channel
    157. UGTV (720p)
    158. VTV
    159. Vision Prime (V+)
    160. Warner TV Asia (720p)
    161. iNews HD
    162. Хузур ТВ (1080p) [Not 24/7]

  📁 Grup: [Radio] (3 Channel)
  ----------------------------------------
    1. Rodja fm
    2. The rockin life
    3. The rockin life (indirect)

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
