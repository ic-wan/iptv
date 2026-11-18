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

  📁 Grup: [Lokal] (35 Channel)
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
    18. Padang tv (720p) [not 24/7]
    19. Pontv (720p)
    20. R tv
    21. Radar tasikmalaya tv (720p) [not 24/7]
    22. Radio kita tv (1080p)
    23. Rodja tv (720p)
    24. Salira tv (720p)
    25. Smtv (720p) [not 24/7]
    26. Stara tv (720p)
    27. Stara tv bandung (1080p)
    28. Stara tv cianjur (720p)
    29. Stara tv malang (1080p)
    30. Tatv (720p) [not 24/7]
    31. Tv one
    32. Tv tabalong (720p) [not 24/7]
    33. Tv9 nusantara (720p)
    34. Tvri jawa barat (480p)
    35. Tvri world

  📁 Grup: [Lokal (auto)] (149 Channel)
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
    27. Balikpapan TV (720p)
    28. Banjar TV (720p) [Not 24/7]
    29. Banten TV
    30. Batam TV (480p) [Not 24/7]
    31. Berita Satu
    32. Berita Satu (DensTV)
    33. Bungo TV
    34. CNBC Indonesia
    35. CNBC Indonesia (ChannelFeed)
    36. CTV Dla Ciebie TV
    37. Cao Bằng TV (720p)
    38. Clan Internacional Americas (1080p) [Geo-blocked]
    39. DAAI TV
    40. DAAI TV (Dens)
    41. DMI TV (576i)
    42. Dhamma TV (720p) [Not 24/7]
    43. Dhoho TV
    44. Dunia Lain
    45. Eat N Go
    46. Fashion TV
    47. Ficom Channel
    48. GTV
    49. Garuda TV (1080p)
    50. Garuda TV (Flashcon)
    51. Hmong Star TV (720p) [Not 24/7]
    52. Hyder TV (720p)
    53. I Am Channel (576p)
    54. Indonesia Movie Channel (Vision+)
    55. Indosiar HD
    56. Inter TV (1080p)
    57. Iunior TV (1080p)
    58. JTV (720p)
    59. JTV Kediri (1080p) [Not 24/7]
    60. JTV Madiun
    61. Jagantara TV
    62. Kordia TV (1080p)
    63. La 2
    64. Lingkar TV
    65. Love the Planet (1080p)
    66. MAGNA Channel (DensTV)
    67. MAGNA TV (ChannelFeed)
    68. MBG TV (1080p)
    69. MDTV
    70. MDTV (DensTV)
    71. MOJI TV HD (Alt 3 - DensTV flashcon)
    72. MTV Ridiculousness
    73. MTV Ridiculousness (United States) LatAm (720p)
    74. Madani TV (720p)
    75. Magna Channel (1080p)
    76. Metro TV
    77. MetroTV (DensTV)
    78. MetroTV (Flashcon)
    79. Nusantara TV (ChannelFeed)
    80. Omid e Iran TV
    81. Outdoor Channel (1080p)
    82. PKTV (480p)
    83. Peer TV Sudtirol (1080p)
    84. RCTV (Indonesia) (720p) [Not 24/7]
    85. Radar Lampung TV (480p)
    86. Radio 51 TV
    87. Rajawali TV
    88. Rinjani TV
    89. SCTV HD
    90. SMTV (720p)
    91. STV (Indonesia) (720p) [Not 24/7]
    92. Salam TV (720p)
    93. SindoNews
    94. SindoNews (V+)
    95. Sriwijaya TV (720p) [Not 24/7]
    96. Stara TV Bojonegoro (720p)
    97. Stara TV Jakarta (1080p)
    98. Stara TV Parahyangan (720p)
    99. TLC HD
    100. TVE Internacional America (576p) [Geo-blocked]
    101. TVE Star (576p)
    102. TVE Star HD (1080p)
    103. TVOne (V+)
    104. TVRI
    105. TVRI (1080i)
    106. TVRI Aceh (720p)
    107. TVRI Bali (480p)
    108. TVRI Bangka Belitung (480p)
    109. TVRI Bengkulu (480p)
    110. TVRI Gorontalo (480p)
    111. TVRI Jakarta (576i) [Not 24/7]
    112. TVRI Jambi (720p) [Not 24/7]
    113. TVRI Jawa Tengah (720p)
    114. TVRI Jawa Timur (720p)
    115. TVRI Kalimantan Barat (480p)
    116. TVRI Kalimantan Selatan (720p)
    117. TVRI Kalimantan Tengah (480p)
    118. TVRI Kalimantan Timur (720p)
    119. TVRI Lampung (720p)
    120. TVRI Maluku (480p)
    121. TVRI North Sulawesi (1080p)
    122. TVRI North Sumatra (1080p)
    123. TVRI Nusa Tenggara Barat (720p)
    124. TVRI Nusa Tenggara Timur (480p)
    125. TVRI Papua (480p)
    126. TVRI Riau
    127. TVRI Riau (720p) [Not 24/7]
    128. TVRI Sulawesi Barat (720p)
    129. TVRI Sulawesi Selatan (480p)
    130. TVRI Sulawesi Tengah (720p)
    131. TVRI Sulawesi Tenggara (480p)
    132. TVRI Sumatera Barat (720p)
    133. TVRI Sumatera Selatan (480p)
    134. TVRI West Papua (1080p)
    135. TVRI Yogyakarta (720p)
    136. The Indonesia Channel (1080p)
    137. Timor TV
    138. Trans7 (Transcorp)
    139. Trans7 HD
    140. TransTV (Transcorp)
    141. TransTV HD
    142. Tropical Moon Urban TV [Not 24/7]
    143. U Channel
    144. UGTV (720p)
    145. VTV
    146. Warner TV
    147. Warner TV Asia (720p)
    148. iNews HD
    149. Хузур ТВ (1080p) [Not 24/7]

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
