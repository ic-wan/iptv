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

  📁 Grup: [Lokal] (41 Channel)
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
    27. Pontv (720p)
    28. R tv
    29. Salira tv (720p)
    30. Stara tv (720p)
    31. Stara tv bandung (1080p)
    32. Stara tv cianjur (720p)
    33. Stara tv malang (1080p)
    34. Tatv (720p) [not 24/7]
    35. Tv one
    36. Tv tabalong (720p) [not 24/7]
    37. Tv9 nusantara (720p)
    38. Tvri jawa barat (480p)
    39. Tvri jawa timur (720p)
    40. Tvri world
    41. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (148 Channel)
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
    26. Balikpapan TV (720p)
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
    38. Clan Internacional Americas (1080p) [Geo-blocked]
    39. DAAI TV (Dens)
    40. DMI TV (576i)
    41. EmanTv (1080p)
    42. Ficom Channel
    43. Food Travel (V+)
    44. GTV (Transcorp)
    45. Garuda TV (Flashcon)
    46. Hmong Star TV (720p) [Not 24/7]
    47. Hyder TV (720p)
    48. I Am Channel (576p)
    49. Indosiar
    50. Indosiar (Transcorp)
    51. Indosiar HD
    52. Inter TV (1080p)
    53. Iunior TV (1080p)
    54. JAKTV
    55. JTV (720p)
    56. JTV Kediri (1080p) [Not 24/7]
    57. JTV Madiun
    58. JTV Malang
    59. Jagantara TV
    60. Kompas TV HD (Transcorp)
    61. Kordia TV (1080p)
    62. La 2
    63. Lingkar TV
    64. Love the Planet (1080p)
    65. MAGNA TV (ChannelFeed)
    66. MBG TV (1080p)
    67. MDTV (DensTV)
    68. MNC TV (Transcorp)
    69. MOJI TV HD (Alt 3 - DensTV flashcon)
    70. MTV Ridiculousness
    71. MTV Ridiculousness (720p)
    72. Madani TV (720p)
    73. Matrix TV Yogyakarta (720p)
    74. Metro TV
    75. Metro TV (Transcorp)
    76. MetroTV (Flashcon)
    77. Nusantara TV (ChannelFeed)
    78. Omid e Iran TV
    79. Outdoor Channel (1080p)
    80. PKTV (480p)
    81. Peer TV Sudtirol (1080p)
    82. RCTI (Transcorp)
    83. RCTV (Indonesia) (720p) [Not 24/7]
    84. RRI Net (1080p)
    85. RTV (Transcorp)
    86. Radio 51 TV
    87. Rajawali TV
    88. Regio TV (406p)
    89. Riau TV (1080p) [Not 24/7]
    90. Rinjani TV
    91. SCTV (DASH/MPD)
    92. SCTV (Transcorp)
    93. SCTV HD
    94. SMTV (720p)
    95. STV (Indonesia) (720p) [Not 24/7]
    96. Salam TV (720p)
    97. Sangaji TV (720p)
    98. SindoNews
    99. Sooriyan TV (1080p)
    100. Sriwijaya TV (720p) [Not 24/7]
    101. Stara TV Bojonegoro (720p)
    102. Stara TV Jakarta (1080p)
    103. Stara TV Parahyangan (720p)
    104. TV Mu (720p) [Not 24/7]
    105. TVE Star (576p)
    106. TVE Star HD (1080p)
    107. TVOne (Transcorp)
    108. TVRI (1080i)
    109. TVRI Aceh (720p)
    110. TVRI Bali (480p)
    111. TVRI Bangka Belitung (480p)
    112. TVRI Bengkulu (480p)
    113. TVRI Gorontalo (480p)
    114. TVRI Jakarta (576i) [Not 24/7]
    115. TVRI Jambi (720p) [Not 24/7]
    116. TVRI Jawa Tengah (720p)
    117. TVRI Kalimantan Barat (480p)
    118. TVRI Kalimantan Selatan (720p)
    119. TVRI Kalimantan Tengah (480p)
    120. TVRI Lampung (720p)
    121. TVRI Maluku (480p)
    122. TVRI North Sulawesi (1080p)
    123. TVRI North Sumatra (1080p)
    124. TVRI Nusa Tenggara Barat (720p)
    125. TVRI Nusa Tenggara Timur (480p)
    126. TVRI Papua (480p)
    127. TVRI Riau
    128. TVRI Riau (720p) [Not 24/7]
    129. TVRI Sulawesi Barat (720p)
    130. TVRI Sulawesi Selatan (480p)
    131. TVRI Sulawesi Tengah (720p)
    132. TVRI Sulawesi Tenggara (480p)
    133. TVRI Sumatera Barat (720p)
    134. TVRI Sumatera Selatan (480p)
    135. TVRI WORLD
    136. TVRI West Papua (1080p)
    137. TVRI Yogyakarta (720p)
    138. The Indonesia Channel (1080p)
    139. Timor TV
    140. Trans7 (Transcorp)
    141. Trans7 HD
    142. TransTV (Transcorp)
    143. TransTV HD
    144. U Channel
    145. UCL (720p)
    146. Warner TV (Transcorp)
    147. iNews HD
    148. Хузур ТВ (1080p) [Not 24/7]

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
