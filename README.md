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

  📁 Grup: [Lokal] (33 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banyumas tv (720p) [not 24/7]
    3. Caruban tv (1080p)
    4. Dens tv learning
    5. Duta tv (360p) [not 24/7]
    6. Efarina tv (720p)
    7. Indonesiana tv
    8. Izzah tv (480p)
    9. Jawa pos tv jakarta (720p)
    10. Jowo
    11. Kawanua tv (720p)
    12. Kompas tv
    13. Madu tv (576p)
    14. Moji tv
    15. Mqtv (720p) [not 24/7]
    16. Nhk world japan
    17. Pontv (720p)
    18. R tv
    19. Radar tasikmalaya tv (720p) [not 24/7]
    20. Radio kita tv (1080p)
    21. Rodja tv (720p)
    22. Salira tv (720p)
    23. Smtv (720p) [not 24/7]
    24. Stara tv (720p)
    25. Stara tv bandung (1080p)
    26. Stara tv cianjur (720p)
    27. Stara tv malang (1080p)
    28. Tatv (720p) [not 24/7]
    29. Tv one
    30. Tv tabalong (720p) [not 24/7]
    31. Tv9 nusantara (720p)
    32. Tvri jawa barat (480p)
    33. Tvri world

  📁 Grup: [Lokal (auto)] (163 Channel)
  ----------------------------------------
    1. !nsert
    2. 24 Horas (720p)
    3. 24 Канал (1080p)
    4. A Spor SD (1080p)
    5. ABC Australia
    6. ANTV HD
    7. Aathavan TV (720p)
    8. Abadan
    9. Ahsan TV
    10. Ajman TV (1080p)
    11. Al Qamar TV (1080p)
    12. An Ninh TV HD (1080p)
    13. Anadolu Net TV (1080p)
    14. Angel TV Indonesia (720p)
    15. Ashiil TV (480p)
    16. Astro Blitar TV (720p)
    17. Atomic Academy TV (480p)
    18. Atomic TV (360p)
    19. Azan TV
    20. BBC LIFESTYLE
    21. BN Channel (ChannelFeed)
    22. BRTV (720p)
    23. BTV (Channel Feed)
    24. BTV (V+)
    25. Baan Baan TV 73
    26. Balapan HD (1080p)
    27. Balapan International (1080p)
    28. Balikpapan TV (720p)
    29. Banjar TV (720p) [Not 24/7]
    30. Banten TV
    31. Batam TV (480p) [Not 24/7]
    32. Berita Satu
    33. Berita Satu (DensTV)
    34. Bir TV (720p)
    35. Bungo TV
    36. CNBC Indonesia
    37. CNBC Indonesia (ChannelFeed)
    38. CNN Indonesia
    39. CTV Dla Ciebie TV
    40. Cao Bằng TV (720p)
    41. Clan Internacional Americas (1080p) [Geo-blocked]
    42. DAAI TV
    43. DAAI TV (Dens)
    44. DMI TV (576i)
    45. Dhoho TV
    46. Dunia Lain
    47. Eat N Go
    48. Fashion TV
    49. Ficom Channel
    50. GTV
    51. Garuda TV (Flashcon)
    52. Hmong Star TV (720p) [Not 24/7]
    53. Hyder TV (720p)
    54. I Am Channel (576p)
    55. Indonesia Movie Channel (Vision+)
    56. Indosiar (Vidio)
    57. Indosiar HD
    58. Inter TV (1080p)
    59. Iunior TV (1080p)
    60. JTV (720p)
    61. JTV Kediri (1080p) [Not 24/7]
    62. JTV Madiun
    63. JTV Malang (480p)
    64. Jagantara TV
    65. Jawa Pos TV Jakarta (720p)
    66. Jogja TV (720p) [Not 24/7]
    67. Kordia TV (1080p)
    68. La 2
    69. Lingkar TV
    70. Love the Planet (1080p)
    71. MAGNA Channel (DensTV)
    72. MAGNA TV (ChannelFeed)
    73. MBG TV (1080p)
    74. MDTV
    75. MDTV (DensTV)
    76. MDTV (Vidio)
    77. MOJI TV HD (Alt 3 - DensTV flashcon)
    78. MTV Ridiculousness
    79. MTV Ridiculousness (United States) LatAm (720p)
    80. Madani TV (720p)
    81. Magna Channel (1080p)
    82. Metro TV
    83. MetroTV (DensTV)
    84. MetroTV (Flashcon)
    85. Myanmar International TV
    86. Nusantara TV (ChannelFeed)
    87. Omid e Iran TV
    88. PKTV (480p)
    89. Peer TV Sudtirol (1080p)
    90. RCTV (Indonesia) (720p) [Not 24/7]
    91. Radio 51 TV
    92. Rajawali TV
    93. Rede Impacto Gospel TV (720p)
    94. SCTV (Vidio)
    95. SCTV HD
    96. SIN PO TV
    97. SMTV (720p)
    98. Salam TV (720p)
    99. Sangaji TV (720p)
    100. SindoNews
    101. SindoNews (V+)
    102. Sriwijaya TV (720p) [Not 24/7]
    103. Stara TV Bojonegoro (720p)
    104. Stara TV Jakarta (1080p)
    105. Stara TV Parahyangan (720p)
    106. Szlagier TV
    107. TLC HD
    108. TV Mu (720p) [Not 24/7]
    109. TVE Internacional America (576p) [Geo-blocked]
    110. TVE Star (576p)
    111. TVE Star HD (1080p)
    112. TVOne (V+)
    113. TVRI
    114. TVRI (1080i)
    115. TVRI (1080p)
    116. TVRI Aceh (720p)
    117. TVRI Bali (480p)
    118. TVRI Bangka Belitung (480p)
    119. TVRI Bengkulu (480p)
    120. TVRI Gorontalo (480p)
    121. TVRI Jakarta (576i) [Not 24/7]
    122. TVRI Jambi (720p) [Not 24/7]
    123. TVRI Jawa Tengah (720p)
    124. TVRI Jawa Timur (720p)
    125. TVRI Kalimantan Barat (480p)
    126. TVRI Kalimantan Selatan (720p)
    127. TVRI Kalimantan Tengah (480p)
    128. TVRI Kalimantan Timur (720p)
    129. TVRI Lampung (720p)
    130. TVRI Maluku (480p)
    131. TVRI North Sulawesi (1080p)
    132. TVRI North Sumatra (1080p)
    133. TVRI Nusa Tenggara Barat (720p)
    134. TVRI Nusa Tenggara Timur (480p)
    135. TVRI Papua (480p)
    136. TVRI Riau
    137. TVRI Riau (720p) [Not 24/7]
    138. TVRI Sulawesi Barat (720p)
    139. TVRI Sulawesi Selatan (480p)
    140. TVRI Sulawesi Tengah (720p)
    141. TVRI Sulawesi Tenggara (480p)
    142. TVRI Sumatera Barat (720p)
    143. TVRI Sumatera Selatan (480p)
    144. TVRI West Papua (1080p)
    145. TVRI Yogyakarta (720p)
    146. The Indonesia Channel (1080p)
    147. Trans TV HD (720p)
    148. Trans7 (Transcorp)
    149. Trans7 HD
    150. Trans7 HD (720p)
    151. Trans7 HD (Detik)
    152. TransTV (Detik)
    153. TransTV (Transcorp)
    154. TransTV HD
    155. Tropical Moon Urban TV [Not 24/7]
    156. U Channel
    157. UGTV (720p)
    158. VTV
    159. VTV (Indonesia) HD (1080p)
    160. Warner TV
    161. Warner TV Asia (720p)
    162. iNews HD
    163. Хузур ТВ (1080p) [Not 24/7]

  📁 Grup: [Radio] (4 Channel)
  ----------------------------------------
    1. Prambors fm
    2. Rodja fm
    3. The rockin life
    4. The rockin life (indirect)

  📁 Grup: [Travels] (4 Channel)
  ----------------------------------------
    1. Dronetv (1080p)
    2. Intravel (1080p)
    3. Travel escapes (1080p)
    4. Travel tv (576p)

=============================================
```
<!-- END_PROGRAM_LIST -->
