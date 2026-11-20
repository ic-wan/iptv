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

  📁 Grup: [Lokal (auto)] (154 Channel)
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
    33. Bir TV (720p)
    34. Bungo TV
    35. CNBC Indonesia (ChannelFeed)
    36. CNN Indonesia
    37. CTV Dla Ciebie TV
    38. Cao Bằng TV (720p)
    39. Clan Internacional Americas (1080p) [Geo-blocked]
    40. DAAI TV
    41. DAAI TV (Dens)
    42. DMI TV (576i)
    43. Dhamma TV (720p) [Not 24/7]
    44. Dhoho TV
    45. Dunia Lain
    46. Eat N Go
    47. EmanTv (1080p)
    48. Fajar TV (720p) [Not 24/7]
    49. Fashion TV
    50. Ficom Channel
    51. GTV
    52. Garuda TV (1080p)
    53. Garuda TV (Flashcon)
    54. Hmong Star TV (720p) [Not 24/7]
    55. Hyder TV (720p)
    56. I Am Channel (576p)
    57. Indonesia Movie Channel (Vision+)
    58. Indosiar HD
    59. Inter TV (1080p)
    60. Iunior TV (1080p)
    61. JTV (720p)
    62. JTV Kediri (1080p) [Not 24/7]
    63. JTV Madiun
    64. JTV Malang (480p)
    65. Kordia TV (1080p)
    66. La 2
    67. Lingkar TV
    68. Love the Planet (1080p)
    69. MAGNA Channel (DensTV)
    70. MAGNA TV (ChannelFeed)
    71. MBG TV (1080p)
    72. MDTV
    73. MDTV (DensTV)
    74. MOJI TV HD (Alt 3 - DensTV flashcon)
    75. MTV Ridiculousness
    76. MTV Ridiculousness (United States) LatAm (720p)
    77. Madani TV (720p)
    78. Magna Channel (1080p)
    79. Metro TV
    80. MetroTV (DensTV)
    81. MetroTV (Flashcon)
    82. Myanmar International TV
    83. Nusantara TV (ChannelFeed)
    84. Omid e Iran TV
    85. Outdoor Channel (1080p)
    86. PKTV (480p)
    87. Peer TV Sudtirol (1080p)
    88. RCTV (Indonesia) (720p) [Not 24/7]
    89. Radio 51 TV
    90. Rajawali TV
    91. Rede Impacto Gospel TV (720p)
    92. Rinjani TV
    93. SCTV (DASH/MPD)
    94. SCTV HD
    95. SMTV (720p)
    96. STV (Indonesia) (720p) [Not 24/7]
    97. Salam TV (720p)
    98. Sangaji TV (720p)
    99. SindoNews
    100. SindoNews (V+)
    101. Sriwijaya TV (720p) [Not 24/7]
    102. Stara TV Bojonegoro (720p)
    103. Stara TV Jakarta (1080p)
    104. Stara TV Parahyangan (720p)
    105. TLC HD
    106. TVE Internacional America (576p) [Geo-blocked]
    107. TVE Star (576p)
    108. TVE Star HD (1080p)
    109. TVOne (V+)
    110. TVRI
    111. TVRI (1080i)
    112. TVRI Aceh (720p)
    113. TVRI Bali (480p)
    114. TVRI Bangka Belitung (480p)
    115. TVRI Bengkulu (480p)
    116. TVRI Gorontalo (480p)
    117. TVRI Jakarta (576i) [Not 24/7]
    118. TVRI Jambi (720p) [Not 24/7]
    119. TVRI Jawa Tengah (720p)
    120. TVRI Jawa Timur (720p)
    121. TVRI Kalimantan Barat (480p)
    122. TVRI Kalimantan Selatan (720p)
    123. TVRI Kalimantan Tengah (480p)
    124. TVRI Kalimantan Timur (720p)
    125. TVRI Lampung (720p)
    126. TVRI Maluku (480p)
    127. TVRI North Sulawesi (1080p)
    128. TVRI North Sumatra (1080p)
    129. TVRI Nusa Tenggara Barat (720p)
    130. TVRI Nusa Tenggara Timur (480p)
    131. TVRI Papua (480p)
    132. TVRI Riau
    133. TVRI Riau (720p) [Not 24/7]
    134. TVRI Sulawesi Barat (720p)
    135. TVRI Sulawesi Selatan (480p)
    136. TVRI Sulawesi Tengah (720p)
    137. TVRI Sulawesi Tenggara (480p)
    138. TVRI Sumatera Barat (720p)
    139. TVRI Sumatera Selatan (480p)
    140. TVRI West Papua (1080p)
    141. TVRI Yogyakarta (720p)
    142. The Indonesia Channel (1080p)
    143. Timor TV
    144. Trans7 (Transcorp)
    145. Trans7 HD
    146. TransTV (Transcorp)
    147. TransTV HD
    148. Tropical Moon Urban TV [Not 24/7]
    149. U Channel
    150. UGTV (720p)
    151. Warner TV
    152. Warner TV Asia (720p)
    153. iNews HD
    154. Хузур ТВ (1080p) [Not 24/7]

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
