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

  📁 Grup: [Lokal] (47 Channel)
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
    19. Jtv (480p)
    20. Kawanua tv (720p)
    21. Kompas tv
    22. Madu tv (576p)
    23. Magna channel (1080p) [not 24/7]
    24. Metro tv
    25. Moji tv
    26. Mqtv (720p) [not 24/7]
    27. Nhk world japan
    28. Padang tv (720p) [not 24/7]
    29. Pontv (720p)
    30. R tv
    31. Radar tasikmalaya tv (720p) [not 24/7]
    32. Radio kita tv (1080p)
    33. Rodja tv (720p)
    34. Salira tv (720p)
    35. Smtv (720p) [not 24/7]
    36. Stara tv (720p)
    37. Stara tv bandung (1080p)
    38. Stara tv cianjur (720p)
    39. Stara tv malang (1080p)
    40. Tatv (720p) [not 24/7]
    41. Tv one
    42. Tv tabalong (720p) [not 24/7]
    43. Tv9 nusantara (720p)
    44. Tvri jawa barat (480p)
    45. Tvri jawa timur (720p)
    46. Tvri world
    47. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (135 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ANTV HD
    4. ATV (1080p)
    5. ATV (Turkiye) (1080p)
    6. Abadan
    7. Ahsan TV
    8. Ajman TV (1080p)
    9. Al Qamar TV (1080p)
    10. Anadolu Net TV (1080p)
    11. Angel TV Indonesia (720p)
    12. Ashiil TV (480p)
    13. Astro Blitar TV (720p)
    14. Atambua TV (720p)
    15. Atomic Academy TV (480p)
    16. Atomic TV (360p)
    17. Azan TV
    18. BALI TV
    19. BBC LIFESTYLE
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
    31. Bungo TV
    32. CNBC Indonesia (ChannelFeed)
    33. CNN Indonesia (ChannelFeed)
    34. Canal 24 Horas (720p)
    35. Cao Bằng TV (720p)
    36. Clan Internacional Americas (1080p) [Geo-blocked]
    37. DAAI TV (Dens)
    38. DMI TV (576i)
    39. Fajar TV (720p) [Not 24/7]
    40. Ficom Channel
    41. Food Travel (V+)
    42. Garuda TV (Flashcon)
    43. Hmong Star TV (720p) [Not 24/7]
    44. Hyder TV (720p)
    45. I Am Channel (576p)
    46. Indosiar
    47. Indosiar HD
    48. Inter TV (1080p)
    49. Iunior TV (1080p)
    50. JAKTV
    51. JTV (720p)
    52. JTV Kediri (1080p) [Not 24/7]
    53. JTV Madiun
    54. JTV Malang
    55. Jagantara TV
    56. Kordia TV (1080p)
    57. La 2
    58. Lingkar TV
    59. Love the Planet (1080p)
    60. MAGNA Channel (Flashcon)
    61. MAGNA TV (ChannelFeed)
    62. MBG TV (1080p)
    63. MDTV
    64. MOJI TV HD (Alt 3 - DensTV flashcon)
    65. MTV Ridiculousness
    66. MTV Ridiculousness (720p)
    67. Madani TV (720p)
    68. Matrix TV Yogyakarta (720p)
    69. Metro TV
    70. MetroTV (Flashcon)
    71. Nusantara TV (ChannelFeed)
    72. Omid e Iran TV
    73. Outdoor Channel (1080p)
    74. PKTV (480p)
    75. Peer TV Sudtirol (1080p)
    76. RCTV (Indonesia) (720p) [Not 24/7]
    77. Radio 51 TV
    78. Rajawali TV
    79. Regio TV (406p)
    80. Riau TV (1080p) [Not 24/7]
    81. SCTV
    82. SCTV HD
    83. SMTV (720p)
    84. STV (Indonesia) (720p) [Not 24/7]
    85. Salam TV (720p)
    86. Sangaji TV (720p)
    87. SindoNews
    88. Sooriyan TV (1080p)
    89. Sriwijaya TV (720p) [Not 24/7]
    90. Stara TV Bojonegoro (720p)
    91. Stara TV Jakarta (1080p)
    92. Stara TV Parahyangan (720p)
    93. TV Mu (720p) [Not 24/7]
    94. TVE Star (576p)
    95. TVE Star HD (1080p)
    96. TVRI (1080i)
    97. TVRI Aceh (720p)
    98. TVRI Bali (480p)
    99. TVRI Bangka Belitung (480p)
    100. TVRI Bengkulu (480p)
    101. TVRI Gorontalo (480p)
    102. TVRI Jakarta (576i) [Not 24/7]
    103. TVRI Jambi (720p) [Not 24/7]
    104. TVRI Jawa Tengah (720p)
    105. TVRI Kalimantan Barat (480p)
    106. TVRI Kalimantan Selatan (720p)
    107. TVRI Kalimantan Tengah (480p)
    108. TVRI Kalimantan Timur (720p)
    109. TVRI Lampung (720p)
    110. TVRI Maluku (480p)
    111. TVRI North Sulawesi (1080p)
    112. TVRI North Sumatra (1080p)
    113. TVRI Nusa Tenggara Barat (720p)
    114. TVRI Nusa Tenggara Timur (480p)
    115. TVRI Papua (480p)
    116. TVRI Riau
    117. TVRI Riau (720p) [Not 24/7]
    118. TVRI Sulawesi Barat (720p)
    119. TVRI Sulawesi Selatan (480p)
    120. TVRI Sulawesi Tengah (720p)
    121. TVRI Sulawesi Tenggara (480p)
    122. TVRI Sumatera Barat (720p)
    123. TVRI Sumatera Selatan (480p)
    124. TVRI WORLD
    125. TVRI West Papua (1080p)
    126. TVRI Yogyakarta (720p)
    127. The Indonesia Channel (1080p)
    128. Timor TV
    129. Trans7 HD
    130. TransTV HD
    131. U Channel
    132. UCL (720p)
    133. dTVi
    134. iNews HD
    135. Хузур ТВ (1080p) [Not 24/7]

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
