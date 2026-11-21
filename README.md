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

  📁 Grup: [Lokal] (30 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banyumas tv (720p) [not 24/7]
    3. Caruban tv (1080p)
    4. Dens tv learning
    5. Efarina tv (720p)
    6. Indonesiana tv
    7. Izzah tv (480p)
    8. Jawa pos tv jakarta (720p)
    9. Jowo
    10. Kawanua tv (720p)
    11. Kompas tv
    12. Moji tv
    13. Mqtv (720p) [not 24/7]
    14. Nhk world japan
    15. Padang tv (720p) [not 24/7]
    16. Pontv (720p)
    17. R tv
    18. Radio kita tv (1080p)
    19. Rodja tv (720p)
    20. Salira tv (720p)
    21. Smtv (720p) [not 24/7]
    22. Stara tv (720p)
    23. Stara tv bandung (1080p)
    24. Stara tv cianjur (720p)
    25. Stara tv malang (1080p)
    26. Tv one
    27. Tv tabalong (720p) [not 24/7]
    28. Tv9 nusantara (720p)
    29. Tvri jawa barat (480p)
    30. Tvri world

  📁 Grup: [Lokal (auto)] (153 Channel)
  ----------------------------------------
    1. !nsert
    2. 24 Horas (720p)
    3. 24 Канал (1080p)
    4. A Spor SD (1080p)
    5. ABC Australia
    6. ANTV HD
    7. ATV (Turkiye) (1080p)
    8. Aathavan TV (720p)
    9. Abadan
    10. Ahsan TV
    11. Ajman TV (1080p)
    12. Al Qamar TV (1080p)
    13. An Ninh TV HD (1080p)
    14. Anadolu Net TV (1080p)
    15. Angel TV Indonesia (720p)
    16. Ashiil TV (480p)
    17. Astro Blitar TV (720p)
    18. Atomic Academy TV (480p)
    19. Atomic TV (360p)
    20. Azan TV
    21. BBC LIFESTYLE
    22. BN Channel (ChannelFeed)
    23. BRTV (720p)
    24. BTV (Channel Feed)
    25. BTV (V+)
    26. Baan Baan TV 73
    27. Balapan HD (1080p)
    28. Balikpapan TV (720p)
    29. Banjar TV (720p) [Not 24/7]
    30. Banten TV
    31. Batam TV (480p) [Not 24/7]
    32. Berita Satu
    33. Berita Satu (DensTV)
    34. Bir TV (720p)
    35. Bungo TV
    36. CNBC Indonesia (ChannelFeed)
    37. CNN Indonesia
    38. CTV Dla Ciebie TV
    39. Cao Bằng TV (720p)
    40. Clan Internacional Americas (1080p) [Geo-blocked]
    41. DAAI TV
    42. DAAI TV (Dens)
    43. DMI TV (576i)
    44. Dhamma TV (720p) [Not 24/7]
    45. Dunia Lain
    46. Eat N Go
    47. Fajar TV (720p) [Not 24/7]
    48. Fashion TV
    49. GTV
    50. Garuda TV (1080p)
    51. Garuda TV (Flashcon)
    52. Hmong Star TV (720p) [Not 24/7]
    53. Hyder TV (720p)
    54. I Am Channel (576p)
    55. Indonesia Movie Channel (Vision+)
    56. Indosiar HD
    57. Inter TV (1080p)
    58. Iunior TV (1080p)
    59. JTV (720p)
    60. JTV Kediri (1080p) [Not 24/7]
    61. JTV Madiun
    62. JTV Malang (480p)
    63. Jagantara TV
    64. Kordia TV (1080p)
    65. La 2
    66. Lingkar TV
    67. Love the Planet (1080p)
    68. MAGNA Channel (DensTV)
    69. MAGNA TV (ChannelFeed)
    70. MBG TV (1080p)
    71. MDTV
    72. MDTV (DensTV)
    73. MOJI TV HD (Alt 3 - DensTV flashcon)
    74. MTV Ridiculousness
    75. MTV Ridiculousness (United States) LatAm (720p)
    76. Madani TV (720p)
    77. Magna Channel (1080p)
    78. Metro TV
    79. MetroTV (DensTV)
    80. MetroTV (Flashcon)
    81. Omid e Iran TV
    82. Outdoor Channel (1080p)
    83. PKTV (480p)
    84. Peer TV Sudtirol (1080p)
    85. RCTV (Indonesia) (720p) [Not 24/7]
    86. Radar Lampung TV (480p)
    87. Radio 51 TV
    88. Rajawali TV
    89. Rede Impacto Gospel TV (720p)
    90. Rinjani TV
    91. SCTV HD
    92. SMTV (720p)
    93. STV (Indonesia) (720p) [Not 24/7]
    94. Salam TV (720p)
    95. Sangaji TV (720p)
    96. SindoNews
    97. SindoNews (V+)
    98. Sriwijaya TV (720p) [Not 24/7]
    99. Stara TV Bojonegoro (720p)
    100. Stara TV Jakarta (1080p)
    101. Stara TV Parahyangan (720p)
    102. TLC HD
    103. TVE Internacional America (576p) [Geo-blocked]
    104. TVE Star (576p)
    105. TVE Star HD (1080p)
    106. TVOne (V+)
    107. TVRI
    108. TVRI (1080i)
    109. TVRI Aceh (720p)
    110. TVRI Bali (480p)
    111. TVRI Bangka Belitung (480p)
    112. TVRI Bengkulu (480p)
    113. TVRI Gorontalo (480p)
    114. TVRI Jakarta (576i) [Not 24/7]
    115. TVRI Jambi (720p) [Not 24/7]
    116. TVRI Jawa Tengah (720p)
    117. TVRI Jawa Timur (720p)
    118. TVRI Kalimantan Barat (480p)
    119. TVRI Kalimantan Selatan (720p)
    120. TVRI Kalimantan Tengah (480p)
    121. TVRI Kalimantan Timur (720p)
    122. TVRI Lampung (720p)
    123. TVRI Maluku (480p)
    124. TVRI North Sulawesi (1080p)
    125. TVRI North Sumatra (1080p)
    126. TVRI Nusa Tenggara Barat (720p)
    127. TVRI Nusa Tenggara Timur (480p)
    128. TVRI Papua (480p)
    129. TVRI Riau
    130. TVRI Riau (720p) [Not 24/7]
    131. TVRI Sulawesi Barat (720p)
    132. TVRI Sulawesi Selatan (480p)
    133. TVRI Sulawesi Tengah (720p)
    134. TVRI Sulawesi Tenggara (480p)
    135. TVRI Sumatera Barat (720p)
    136. TVRI Sumatera Selatan (480p)
    137. TVRI West Papua (1080p)
    138. TVRI Yogyakarta (720p)
    139. The Indonesia Channel (1080p)
    140. Timor TV
    141. Trans7 (Transcorp)
    142. Trans7 HD
    143. TransTV (Detik)
    144. TransTV (Transcorp)
    145. TransTV HD
    146. Tropical Moon Urban TV [Not 24/7]
    147. U Channel
    148. UGTV (720p)
    149. VTV
    150. Warner TV
    151. Warner TV Asia (720p)
    152. iNews HD
    153. Хузур ТВ (1080p) [Not 24/7]

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

  📁 Grup: [Youtube Music] (1 Channel)
  ----------------------------------------
    1. YouTube Stream (DNL6Wy6IstE)

=============================================
```
<!-- END_PROGRAM_LIST -->
