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

  📁 Grup: [Kids] (6 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Kidsflix (1080p) [not 24/7]
    4. Moonbug kids (1080p)
    5. Pbs kids
    6. Vtv (720p)

  📁 Grup: [Lokal] (43 Channel)
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
    31. Salira tv (720p)
    32. Stara tv (720p)
    33. Stara tv bandung (1080p)
    34. Stara tv cianjur (720p)
    35. Stara tv malang (1080p)
    36. Tatv (720p) [not 24/7]
    37. Tv one
    38. Tv tabalong (720p) [not 24/7]
    39. Tv9 nusantara (720p)
    40. Tvri jawa barat (480p)
    41. Tvri jawa timur (720p)
    42. Tvri world
    43. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (150 Channel)
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
    12. Atambua TV (720p)
    13. Atomic Academy TV (480p)
    14. Atomic TV (360p)
    15. Azan TV
    16. BALI TV
    17. BBC LIFESTYLE
    18. BIOSKOP INDONESIA (Transcorp)
    19. BN Channel (ChannelFeed)
    20. BRTV (720p)
    21. BTV (Channel Feed)
    22. BTV (V+)
    23. Baan Baan TV 73
    24. Balapan HD (1080p)
    25. Balikpapan TV (720p)
    26. Banjar TV (720p) [Not 24/7]
    27. Batam TV (480p) [Not 24/7]
    28. Berita Satu
    29. Berita Satu (Transcorp)
    30. Bungo TV
    31. CNBC Indonesia (ChannelFeed)
    32. CNBC Indonesia (Transcorp)
    33. CNN Indonesia (ChannelFeed)
    34. CNN Indonesia (Transcorp)
    35. Canal 24 Horas (720p)
    36. Cao Bằng TV (720p)
    37. Clan Internacional Americas (1080p) [Geo-blocked]
    38. DAAI TV (Dens)
    39. DMI TV (576i)
    40. EmanTv (1080p)
    41. Food Travel (V+)
    42. GTV (Transcorp)
    43. Garuda TV (Flashcon)
    44. Hmong Star TV (720p) [Not 24/7]
    45. Hyder TV (720p)
    46. I Am Channel (576p)
    47. Indosiar
    48. Indosiar (Transcorp)
    49. Indosiar HD
    50. Inter TV (1080p)
    51. Iunior TV (1080p)
    52. JAKTV
    53. JTV (720p)
    54. JTV Kediri (1080p) [Not 24/7]
    55. JTV Madiun
    56. JTV Malang
    57. Jagantara TV
    58. Kompas TV HD (Transcorp)
    59. Kordia TV (1080p)
    60. La 2
    61. Lingkar TV
    62. Love the Planet (1080p)
    63. MAGNA Channel (Flashcon)
    64. MAGNA TV (ChannelFeed)
    65. MBG TV (1080p)
    66. MDTV
    67. MDTV (DensTV)
    68. MDTV (Transcorp)
    69. MNC TV
    70. MNC TV (Transcorp)
    71. MOJI TV HD (Alt 3 - DensTV flashcon)
    72. MTV Ridiculousness
    73. MTV Ridiculousness (720p)
    74. Madani TV (720p)
    75. Matrix TV Yogyakarta (720p)
    76. Metro TV
    77. Metro TV (Transcorp)
    78. MetroTV (Flashcon)
    79. Nusantara TV (ChannelFeed)
    80. Omid e Iran TV
    81. Outdoor Channel (1080p)
    82. PKTV (480p)
    83. Peer TV Sudtirol (1080p)
    84. RCTI
    85. RCTI (Transcorp)
    86. RCTV (Indonesia) (720p) [Not 24/7]
    87. RRI Net (1080p)
    88. RTV (Transcorp)
    89. Radio 51 TV
    90. Rajawali TV
    91. Regio TV (406p)
    92. Riau TV (1080p) [Not 24/7]
    93. SCTV
    94. SCTV (DASH/MPD)
    95. SCTV (Transcorp)
    96. SCTV HD
    97. SMTV (720p)
    98. STV (Indonesia) (720p) [Not 24/7]
    99. Salam TV (720p)
    100. Sangaji TV (720p)
    101. SindoNews
    102. Sooriyan TV (1080p)
    103. Sriwijaya TV (720p) [Not 24/7]
    104. Stara TV Bojonegoro (720p)
    105. Stara TV Jakarta (1080p)
    106. Stara TV Parahyangan (720p)
    107. TV Mu (720p) [Not 24/7]
    108. TVE Star (576p)
    109. TVE Star HD (1080p)
    110. TVOne (Transcorp)
    111. TVRI (1080i)
    112. TVRI Aceh (720p)
    113. TVRI Bali (480p)
    114. TVRI Bangka Belitung (480p)
    115. TVRI Bengkulu (480p)
    116. TVRI Gorontalo (480p)
    117. TVRI Jakarta (576i) [Not 24/7]
    118. TVRI Jambi (720p) [Not 24/7]
    119. TVRI Jawa Tengah (720p)
    120. TVRI Kalimantan Barat (480p)
    121. TVRI Kalimantan Selatan (720p)
    122. TVRI Kalimantan Timur (720p)
    123. TVRI Lampung (720p)
    124. TVRI Maluku (480p)
    125. TVRI North Sulawesi (1080p)
    126. TVRI North Sumatra (1080p)
    127. TVRI Nusa Tenggara Barat (720p)
    128. TVRI Nusa Tenggara Timur (480p)
    129. TVRI Papua (480p)
    130. TVRI Riau
    131. TVRI Sulawesi Barat (720p)
    132. TVRI Sulawesi Selatan (480p)
    133. TVRI Sulawesi Tengah (720p)
    134. TVRI Sulawesi Tenggara (480p)
    135. TVRI Sumatera Barat (720p)
    136. TVRI Sumatera Selatan (480p)
    137. TVRI WORLD
    138. TVRI West Papua (1080p)
    139. TVRI Yogyakarta (720p)
    140. The Indonesia Channel (1080p)
    141. Timor TV
    142. Trans7 (Transcorp)
    143. Trans7 HD
    144. TransTV (Transcorp)
    145. U Channel
    146. UCL (720p)
    147. Warner TV (Transcorp)
    148. dTVi
    149. iNews HD
    150. Хузур ТВ (1080p) [Not 24/7]

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
