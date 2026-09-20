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
    10. Efarina tv (720p)
    11. Garuda tv (1080p)
    12. Indonesiana tv
    13. Jawa pos tv jakarta (720p)
    14. Jogja istimewa tv (720p)
    15. Jogja tv (720p) [not 24/7]
    16. Jowo
    17. Kawanua tv (720p)
    18. Kompas tv
    19. Madu tv (576p)
    20. Magna channel (1080p) [not 24/7]
    21. Metro tv
    22. Moji tv
    23. Mqtv (720p) [not 24/7]
    24. Nhk world japan
    25. Padang tv (720p) [not 24/7]
    26. Pontv (720p)
    27. R tv
    28. Radar tasikmalaya tv (720p) [not 24/7]
    29. Rodja tv (720p)
    30. Salira tv (720p)
    31. Smtv (720p) [not 24/7]
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

  📁 Grup: [Lokal (auto)] (136 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ANTV HD
    4. ATV (Turkiye) (1080p)
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
    29. Bungo TV
    30. CNBC Indonesia (ChannelFeed)
    31. CNN Indonesia (ChannelFeed)
    32. Canal 24 Horas (720p)
    33. Cao Bằng TV (720p)
    34. Clan Internacional Americas (1080p) [Geo-blocked]
    35. DAAI TV (Dens)
    36. DMI TV (576i)
    37. Ficom Channel
    38. Food Travel (V+)
    39. Garuda TV (Flashcon)
    40. Hmong Star TV (720p) [Not 24/7]
    41. Hyder TV (720p)
    42. I Am Channel (576p)
    43. Indosiar
    44. Indosiar HD
    45. Inter TV (1080p)
    46. Iunior TV (1080p)
    47. JAKTV
    48. JTV (720p)
    49. JTV Kediri (1080p) [Not 24/7]
    50. JTV Madiun
    51. JTV Malang
    52. Jagantara TV
    53. Kordia TV (1080p)
    54. La 2
    55. Lingkar TV
    56. Love the Planet (1080p)
    57. MAGNA Channel (Flashcon)
    58. MAGNA TV (ChannelFeed)
    59. MBG TV (1080p)
    60. MDTV
    61. MNC TV
    62. MOJI TV HD (Alt 3 - DensTV flashcon)
    63. MTV Ridiculousness
    64. MTV Ridiculousness (720p)
    65. Madani TV (720p)
    66. Matrix TV Yogyakarta (720p)
    67. Metro TV
    68. MetroTV (Flashcon)
    69. Myanmar International TV
    70. Nusantara TV (ChannelFeed)
    71. Omid e Iran TV
    72. Outdoor Channel (1080p)
    73. PKTV (480p)
    74. Peer TV Sudtirol (1080p)
    75. RCTV (Indonesia) (720p) [Not 24/7]
    76. Radio 51 TV
    77. Rajawali TV
    78. Regio TV (406p)
    79. Riau TV (1080p) [Not 24/7]
    80. Rinjani TV
    81. SCTV
    82. SCTV (DASH/MPD)
    83. SCTV HD
    84. SMTV (720p)
    85. STV (Indonesia) (720p) [Not 24/7]
    86. Salam TV (720p)
    87. Sangaji TV (720p)
    88. SindoNews
    89. Sooriyan TV (1080p)
    90. Sriwijaya TV (720p) [Not 24/7]
    91. Stara TV Bojonegoro (720p)
    92. Stara TV Jakarta (1080p)
    93. Stara TV Parahyangan (720p)
    94. TV Mu (720p) [Not 24/7]
    95. TVE Star (576p)
    96. TVE Star HD (1080p)
    97. TVRI (1080i)
    98. TVRI Aceh (720p)
    99. TVRI Bali (480p)
    100. TVRI Bangka Belitung (480p)
    101. TVRI Bengkulu (480p)
    102. TVRI Gorontalo (480p)
    103. TVRI Jakarta (576i) [Not 24/7]
    104. TVRI Jambi (720p) [Not 24/7]
    105. TVRI Jawa Tengah (720p)
    106. TVRI Kalimantan Barat (480p)
    107. TVRI Kalimantan Selatan (720p)
    108. TVRI Kalimantan Tengah (480p)
    109. TVRI Kalimantan Timur (720p)
    110. TVRI Lampung (720p)
    111. TVRI Maluku (480p)
    112. TVRI North Sulawesi (1080p)
    113. TVRI North Sumatra (1080p)
    114. TVRI Nusa Tenggara Barat (720p)
    115. TVRI Nusa Tenggara Timur (480p)
    116. TVRI Papua (480p)
    117. TVRI Riau
    118. TVRI Riau (720p) [Not 24/7]
    119. TVRI Sulawesi Barat (720p)
    120. TVRI Sulawesi Selatan (480p)
    121. TVRI Sulawesi Tengah (720p)
    122. TVRI Sulawesi Tenggara (480p)
    123. TVRI Sumatera Barat (720p)
    124. TVRI Sumatera Selatan (480p)
    125. TVRI WORLD
    126. TVRI West Papua (1080p)
    127. TVRI Yogyakarta (720p)
    128. The Indonesia Channel (1080p)
    129. Timor TV
    130. Trans7 HD
    131. TransTV HD
    132. U Channel
    133. UCL (720p)
    134. dTVi
    135. iNews HD
    136. Хузур ТВ (1080p) [Not 24/7]

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
