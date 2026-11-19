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

  📁 Grup: [Lokal] (34 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banyumas tv (720p) [not 24/7]
    3. Bn channel (720p)
    4. Caruban tv (1080p)
    5. Dens tv learning
    6. Duta tv (360p) [not 24/7]
    7. Efarina tv (720p)
    8. Indonesiana tv
    9. Izzah tv (480p)
    10. Jawa pos tv jakarta (720p)
    11. Jowo
    12. Kawanua tv (720p)
    13. Kompas tv
    14. Madu tv (576p)
    15. Moji tv
    16. Mqtv (720p) [not 24/7]
    17. Nhk world japan
    18. Pontv (720p)
    19. R tv
    20. Radar tasikmalaya tv (720p) [not 24/7]
    21. Radio kita tv (1080p)
    22. Rodja tv (720p)
    23. Salira tv (720p)
    24. Smtv (720p) [not 24/7]
    25. Stara tv (720p)
    26. Stara tv bandung (1080p)
    27. Stara tv cianjur (720p)
    28. Stara tv malang (1080p)
    29. Tatv (720p) [not 24/7]
    30. Tv one
    31. Tv tabalong (720p) [not 24/7]
    32. Tv9 nusantara (720p)
    33. Tvri jawa barat (480p)
    34. Tvri world

  📁 Grup: [Lokal (auto)] (152 Channel)
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
    38. CTV Dla Ciebie TV
    39. Cao Bằng TV (720p)
    40. Clan Internacional Americas (1080p) [Geo-blocked]
    41. DAAI TV
    42. DAAI TV (Dens)
    43. DMI TV (576i)
    44. Dhamma TV (720p) [Not 24/7]
    45. Dhoho TV
    46. Dunia Lain
    47. Eat N Go
    48. Fashion TV
    49. Ficom Channel
    50. GTV
    51. Garuda TV (1080p)
    52. Garuda TV (Flashcon)
    53. Hmong Star TV (720p) [Not 24/7]
    54. Hyder TV (720p)
    55. I Am Channel (576p)
    56. Indosiar HD
    57. Inter TV (1080p)
    58. Iunior TV (1080p)
    59. JTV (720p)
    60. JTV Madiun
    61. JTV Malang
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
    81. Myanmar International TV
    82. Nusantara TV (ChannelFeed)
    83. Omid e Iran TV
    84. Outdoor Channel (1080p)
    85. PKTV (480p)
    86. Peer TV Sudtirol (1080p)
    87. RCTV (Indonesia) (720p) [Not 24/7]
    88. Radio 51 TV
    89. Rajawali TV
    90. Rede Impacto Gospel TV (720p)
    91. Rinjani TV
    92. SCTV HD
    93. SMTV (720p)
    94. STV (Indonesia) (720p) [Not 24/7]
    95. Salam TV (720p)
    96. Sangaji TV (720p)
    97. SindoNews
    98. SindoNews (V+)
    99. Sriwijaya TV (720p) [Not 24/7]
    100. Stara TV Bojonegoro (720p)
    101. Stara TV Jakarta (1080p)
    102. Stara TV Parahyangan (720p)
    103. TLC HD
    104. TVE Internacional America (576p) [Geo-blocked]
    105. TVE Star (576p)
    106. TVE Star HD (1080p)
    107. TVOne (V+)
    108. TVRI
    109. TVRI (1080i)
    110. TVRI Aceh (720p)
    111. TVRI Bali (480p)
    112. TVRI Bangka Belitung (480p)
    113. TVRI Bengkulu (480p)
    114. TVRI Gorontalo (480p)
    115. TVRI Jakarta (576i) [Not 24/7]
    116. TVRI Jambi (720p) [Not 24/7]
    117. TVRI Jawa Tengah (720p)
    118. TVRI Jawa Timur (720p)
    119. TVRI Kalimantan Barat (480p)
    120. TVRI Kalimantan Selatan (720p)
    121. TVRI Kalimantan Tengah (480p)
    122. TVRI Kalimantan Timur (720p)
    123. TVRI Lampung (720p)
    124. TVRI Maluku (480p)
    125. TVRI North Sulawesi (1080p)
    126. TVRI North Sumatra (1080p)
    127. TVRI Nusa Tenggara Barat (720p)
    128. TVRI Nusa Tenggara Timur (480p)
    129. TVRI Papua (480p)
    130. TVRI Riau
    131. TVRI Riau (720p) [Not 24/7]
    132. TVRI Sulawesi Barat (720p)
    133. TVRI Sulawesi Selatan (480p)
    134. TVRI Sulawesi Tengah (720p)
    135. TVRI Sulawesi Tenggara (480p)
    136. TVRI Sumatera Barat (720p)
    137. TVRI Sumatera Selatan (480p)
    138. TVRI West Papua (1080p)
    139. TVRI Yogyakarta (720p)
    140. The Indonesia Channel (1080p)
    141. Timor TV
    142. Trans7 (Transcorp)
    143. Trans7 HD
    144. TransTV (Transcorp)
    145. TransTV HD
    146. Tropical Moon Urban TV [Not 24/7]
    147. U Channel
    148. UGTV (720p)
    149. VTV
    150. Warner TV Asia (720p)
    151. iNews HD
    152. Хузур ТВ (1080p) [Not 24/7]

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
