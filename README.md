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

  📁 Grup: [Indihome] (7 Channel)
  ----------------------------------------
    1. Berita satu
    2. Jtv
    3. Kompas tv
    4. Max sport
    5. Prambors tv
    6. Rtv
    7. Sctv

  📁 Grup: [Kids] (6 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Kidsflix (1080p) [not 24/7]
    4. Moonbug kids (1080p)
    5. Pbs kids
    6. Vtv (720p)

  📁 Grup: [Lokal] (44 Channel)
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
    30. Radio kita tv (1080p)
    31. Rodja tv (720p)
    32. Salira tv (720p)
    33. Stara tv (720p)
    34. Stara tv bandung (1080p)
    35. Stara tv cianjur (720p)
    36. Stara tv malang (1080p)
    37. Tatv (720p) [not 24/7]
    38. Tv one
    39. Tv tabalong (720p) [not 24/7]
    40. Tv9 nusantara (720p)
    41. Tvri jawa barat (480p)
    42. Tvri jawa timur (720p)
    43. Tvri world
    44. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (155 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ANTV HD
    4. ANTV HD (Transcorp)
    5. Abadan
    6. Ahsan TV
    7. Ajman TV (1080p)
    8. Al Qamar TV (1080p)
    9. Anadolu Net TV (1080p)
    10. Angel TV Indonesia (720p)
    11. Ashiil TV (480p)
    12. Astro Blitar TV (720p)
    13. Atambua TV (720p)
    14. Atomic Academy TV (480p)
    15. Atomic TV (360p)
    16. Azan TV
    17. BALI TV
    18. BBC LIFESTYLE
    19. BIOSKOP INDONESIA (Transcorp)
    20. BN Channel (ChannelFeed)
    21. BRTV (720p)
    22. BTV (Channel Feed)
    23. BTV (V+)
    24. Baan Baan TV 73
    25. Balapan HD (1080p)
    26. Balapan International (1080p)
    27. Balikpapan TV (720p)
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
    39. Clan Internacional Americas (1080p) [Geo-blocked]
    40. DAAI TV (Dens)
    41. DMI TV (576i)
    42. EmanTv (1080p)
    43. Ficom Channel
    44. Food Travel (V+)
    45. GTV (Transcorp)
    46. Garuda TV (Flashcon)
    47. Hmong Star TV (720p) [Not 24/7]
    48. Hyder TV (720p)
    49. I Am Channel (576p)
    50. Indosiar
    51. Indosiar (Transcorp)
    52. Indosiar HD
    53. Inter TV (1080p)
    54. Iunior TV (1080p)
    55. JAKTV
    56. JTV (720p)
    57. JTV Kediri (1080p) [Not 24/7]
    58. JTV Madiun
    59. JTV Malang
    60. Jagantara TV
    61. Kompas TV HD (Transcorp)
    62. Kordia TV (1080p)
    63. La 2
    64. Lingkar TV
    65. Love the Planet (1080p)
    66. MAGNA Channel (Flashcon)
    67. MAGNA TV (ChannelFeed)
    68. MBG TV (1080p)
    69. MDTV (DensTV)
    70. MDTV (Transcorp)
    71. MNC TV
    72. MNC TV (Transcorp)
    73. MOJI TV HD (Alt 3 - DensTV flashcon)
    74. MTV Ridiculousness
    75. MTV Ridiculousness (720p)
    76. Madani TV (720p)
    77. Matrix TV Yogyakarta (720p)
    78. Metro TV
    79. Metro TV (Transcorp)
    80. MetroTV (Flashcon)
    81. Nusantara TV (ChannelFeed)
    82. Omid e Iran TV
    83. Outdoor Channel (1080p)
    84. PKTV (480p)
    85. Peer TV Sudtirol (1080p)
    86. RCTI
    87. RCTI (Transcorp)
    88. RCTV (Indonesia) (720p) [Not 24/7]
    89. RRI Net (1080p)
    90. RTV (Transcorp)
    91. Radar Lampung TV (480p)
    92. Radio 51 TV
    93. Rajawali TV
    94. Regio TV (406p)
    95. Riau TV (1080p) [Not 24/7]
    96. SCTV
    97. SCTV (DASH/MPD)
    98. SCTV (Transcorp)
    99. SCTV HD
    100. STV (Indonesia) (720p) [Not 24/7]
    101. Salam TV (720p)
    102. Sangaji TV (720p)
    103. SindoNews
    104. Sooriyan TV (1080p)
    105. Sriwijaya TV (720p) [Not 24/7]
    106. Stara TV Bojonegoro (720p)
    107. Stara TV Jakarta (1080p)
    108. Stara TV Parahyangan (720p)
    109. TV Mu (720p) [Not 24/7]
    110. TVE Star (576p)
    111. TVE Star HD (1080p)
    112. TVOne (Transcorp)
    113. TVRI (1080i)
    114. TVRI Aceh (720p)
    115. TVRI Bali (480p)
    116. TVRI Bangka Belitung (480p)
    117. TVRI Bengkulu (480p)
    118. TVRI Gorontalo (480p)
    119. TVRI Jakarta (576i) [Not 24/7]
    120. TVRI Jambi (720p) [Not 24/7]
    121. TVRI Jawa Tengah (720p)
    122. TVRI Kalimantan Barat (480p)
    123. TVRI Kalimantan Selatan (720p)
    124. TVRI Kalimantan Tengah (480p)
    125. TVRI Kalimantan Timur (720p)
    126. TVRI Lampung (720p)
    127. TVRI Maluku (480p)
    128. TVRI North Sulawesi (1080p)
    129. TVRI North Sumatra (1080p)
    130. TVRI Nusa Tenggara Barat (720p)
    131. TVRI Nusa Tenggara Timur (480p)
    132. TVRI Papua (480p)
    133. TVRI Riau
    134. TVRI Riau (720p) [Not 24/7]
    135. TVRI Sulawesi Barat (720p)
    136. TVRI Sulawesi Selatan (480p)
    137. TVRI Sulawesi Tengah (720p)
    138. TVRI Sulawesi Tenggara (480p)
    139. TVRI Sumatera Barat (720p)
    140. TVRI Sumatera Selatan (480p)
    141. TVRI WORLD
    142. TVRI West Papua (1080p)
    143. TVRI Yogyakarta (720p)
    144. The Indonesia Channel (1080p)
    145. Timor TV
    146. Trans7 (Transcorp)
    147. Trans7 HD
    148. TransTV (Transcorp)
    149. TransTV HD
    150. U Channel
    151. UCL (720p)
    152. Warner TV (Transcorp)
    153. dTVi
    154. iNews HD
    155. Хузур ТВ (1080p) [Not 24/7]

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
