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
    14. Jawa pos tv jakarta (720p)
    15. Jogja istimewa tv (720p)
    16. Jogja tv (720p) [not 24/7]
    17. Jowo
    18. Kawanua tv (720p)
    19. Kompas tv
    20. Madu tv (576p)
    21. Magna channel (1080p) [not 24/7]
    22. Metro tv
    23. Moji tv
    24. Mqtv (720p) [not 24/7]
    25. Nhk world japan
    26. Padang tv (720p) [not 24/7]
    27. Pontv (720p)
    28. R tv
    29. Radar tasikmalaya tv (720p) [not 24/7]
    30. Rri net (1080p)
    31. Salira tv (720p)
    32. Smtv (720p) [not 24/7]
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

  📁 Grup: [Lokal (auto)] (136 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ANTV HD
    4. Abadan
    5. Ahsan TV
    6. Ajman TV (1080p)
    7. Al Qamar TV (1080p)
    8. Anadolu Net TV (1080p)
    9. Angel TV Indonesia (720p)
    10. Ashiil TV (480p)
    11. Astro Blitar TV (720p)
    12. Atambua TV (720p)
    13. Atomic Academy TV (480p)
    14. Atomic TV (360p)
    15. Azan TV
    16. BALI TV
    17. BBC LIFESTYLE
    18. BN Channel (ChannelFeed)
    19. BRTV (720p)
    20. BTV (Channel Feed)
    21. BTV (V+)
    22. Baan Baan TV 73
    23. Balapan HD (1080p)
    24. Balikpapan TV (720p)
    25. Banjar TV (720p) [Not 24/7]
    26. Batam TV (480p) [Not 24/7]
    27. Berita Satu
    28. Bungo TV
    29. CNBC Indonesia (ChannelFeed)
    30. CNN Indonesia (ChannelFeed)
    31. Canal 24 Horas (720p)
    32. Cao Bằng TV (720p)
    33. Clan Internacional Americas (1080p) [Geo-blocked]
    34. DAAI TV (Dens)
    35. DMI TV (576i)
    36. EmanTv (1080p)
    37. Fajar TV (720p) [Not 24/7]
    38. Ficom Channel
    39. Food Travel (V+)
    40. Garuda TV (Flashcon)
    41. Hmong Star TV (720p) [Not 24/7]
    42. Hyder TV (720p)
    43. I Am Channel (576p)
    44. Indosiar
    45. Indosiar HD
    46. Inter TV (1080p)
    47. Iunior TV (1080p)
    48. JAKTV
    49. JTV (720p)
    50. JTV Kediri (1080p) [Not 24/7]
    51. JTV Madiun
    52. JTV Malang
    53. Jagantara TV
    54. Kordia TV (1080p)
    55. La 2
    56. Lingkar TV
    57. Love the Planet (1080p)
    58. MAGNA Channel (Flashcon)
    59. MAGNA TV (ChannelFeed)
    60. MBG TV (1080p)
    61. MNC TV
    62. MOJI TV HD (Alt 3 - DensTV flashcon)
    63. MTV Ridiculousness
    64. MTV Ridiculousness (720p)
    65. Madani TV (720p)
    66. Matrix TV Yogyakarta (720p)
    67. Metro TV
    68. MetroTV (Flashcon)
    69. Nusantara TV (ChannelFeed)
    70. Omid e Iran TV
    71. Outdoor Channel (1080p)
    72. PKTV (480p)
    73. Peer TV Sudtirol (1080p)
    74. RCTI
    75. RCTV (Indonesia) (720p) [Not 24/7]
    76. RRI Net (1080p)
    77. Radio 51 TV
    78. Rajawali TV
    79. Regio TV (406p)
    80. Riau TV (1080p) [Not 24/7]
    81. Rinjani TV
    82. SCTV
    83. SCTV (DASH/MPD)
    84. SCTV HD
    85. SMTV (720p)
    86. STV (Indonesia) (720p) [Not 24/7]
    87. Salam TV (720p)
    88. Sangaji TV (720p)
    89. SindoNews
    90. Sooriyan TV (1080p)
    91. Sriwijaya TV (720p) [Not 24/7]
    92. Stara TV Bojonegoro (720p)
    93. Stara TV Jakarta (1080p)
    94. Stara TV Parahyangan (720p)
    95. TV Mu (720p) [Not 24/7]
    96. TVE Star (576p)
    97. TVE Star HD (1080p)
    98. TVRI (1080i)
    99. TVRI Aceh (720p)
    100. TVRI Bali (480p)
    101. TVRI Bangka Belitung (480p)
    102. TVRI Bengkulu (480p)
    103. TVRI Gorontalo (480p)
    104. TVRI Jakarta (576i) [Not 24/7]
    105. TVRI Jambi (720p) [Not 24/7]
    106. TVRI Jawa Tengah (720p)
    107. TVRI Kalimantan Barat (480p)
    108. TVRI Kalimantan Selatan (720p)
    109. TVRI Kalimantan Tengah (480p)
    110. TVRI Kalimantan Timur (720p)
    111. TVRI Lampung (720p)
    112. TVRI Maluku (480p)
    113. TVRI North Sulawesi (1080p)
    114. TVRI North Sumatra (1080p)
    115. TVRI Nusa Tenggara Barat (720p)
    116. TVRI Nusa Tenggara Timur (480p)
    117. TVRI Papua (480p)
    118. TVRI Riau
    119. TVRI Riau (720p) [Not 24/7]
    120. TVRI Sulawesi Barat (720p)
    121. TVRI Sulawesi Selatan (480p)
    122. TVRI Sulawesi Tengah (720p)
    123. TVRI Sulawesi Tenggara (480p)
    124. TVRI Sumatera Barat (720p)
    125. TVRI Sumatera Selatan (480p)
    126. TVRI WORLD
    127. TVRI West Papua (1080p)
    128. TVRI Yogyakarta (720p)
    129. The Indonesia Channel (1080p)
    130. Timor TV
    131. Trans7 HD
    132. TransTV HD
    133. U Channel
    134. UCL (720p)
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

=============================================
```
<!-- END_PROGRAM_LIST -->
