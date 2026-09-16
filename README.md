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

  📁 Grup: [Lokal] (45 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banyumas tv (720p) [not 24/7]
    3. Bn channel (720p)
    4. Caruban tv (1080p)
    5. Daai tv
    6. Dens tv learning
    7. Dhamma tv (720p) [not 24/7]
    8. Dhoho tv (720p)
    9. Duta tv (360p) [not 24/7]
    10. Efarina tv (720p)
    11. Garuda tv (1080p)
    12. Indonesiana tv
    13. Izzah tv (480p)
    14. Jawa pos tv jakarta (720p)
    15. Jogja istimewa tv (720p)
    16. Jogja tv (720p) [not 24/7]
    17. Jowo
    18. Jtv (480p)
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
    30. Radar tasikmalaya tv (720p) [not 24/7]
    31. Rodja tv (720p)
    32. Rri net (1080p)
    33. Salira tv (720p)
    34. Stara tv (720p)
    35. Stara tv bandung (1080p)
    36. Stara tv cianjur (720p)
    37. Stara tv malang (1080p)
    38. Tatv (720p) [not 24/7]
    39. Tv one
    40. Tv tabalong (720p) [not 24/7]
    41. Tv9 nusantara (720p)
    42. Tvri jawa barat (480p)
    43. Tvri jawa timur (720p)
    44. Tvri world
    45. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (123 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ANTV HD
    3. Abadan
    4. Ahsan TV
    5. Ajman TV (1080p)
    6. Al Qamar TV (1080p)
    7. Anadolu Net TV (1080p)
    8. Angel TV Indonesia (720p)
    9. Ashiil TV (480p)
    10. Astro Blitar TV (720p)
    11. Atomic Academy TV (480p)
    12. Atomic TV (360p)
    13. Azan TV
    14. BALI TV
    15. BBC LIFESTYLE
    16. BN Channel (ChannelFeed)
    17. BRTV (720p)
    18. BTV (Channel Feed)
    19. BTV (V+)
    20. Baan Baan TV 73
    21. Balapan HD (1080p)
    22. Balikpapan TV (720p)
    23. Banjar TV (720p) [Not 24/7]
    24. Batam TV (480p) [Not 24/7]
    25. Berita Satu
    26. Bungo TV
    27. CNBC Indonesia (ChannelFeed)
    28. Canal 24 Horas (720p)
    29. Cao Bằng TV (720p)
    30. Clan Internacional Americas (1080p) [Geo-blocked]
    31. DAAI TV (Dens)
    32. DMI TV (576i)
    33. EmanTv (1080p)
    34. Fajar TV (720p) [Not 24/7]
    35. Ficom Channel
    36. Food Travel (V+)
    37. Garuda TV (Flashcon)
    38. Hmong Star TV (720p) [Not 24/7]
    39. Hyder TV (720p)
    40. I Am Channel (576p)
    41. Indosiar
    42. Indosiar HD
    43. Inter TV (1080p)
    44. Iunior TV (1080p)
    45. JAKTV
    46. JTV Kediri (1080p) [Not 24/7]
    47. JTV Madiun
    48. JTV Malang
    49. Jagantara TV
    50. Kordia TV (1080p)
    51. La 2
    52. Lingkar TV
    53. Love the Planet (1080p)
    54. MAGNA Channel (Flashcon)
    55. MAGNA TV (ChannelFeed)
    56. MBG TV (1080p)
    57. MDTV
    58. MOJI TV HD (Alt 3 - DensTV flashcon)
    59. MTV Ridiculousness
    60. MTV Ridiculousness (720p)
    61. Madani TV (720p)
    62. Matrix TV Yogyakarta (720p)
    63. Metro TV
    64. MetroTV (Flashcon)
    65. Nusantara TV (ChannelFeed)
    66. Outdoor Channel (1080p)
    67. PKTV (480p)
    68. Radio 51 TV
    69. Rajawali TV
    70. Riau TV (1080p) [Not 24/7]
    71. Rinjani TV
    72. SCTV (DASH/MPD)
    73. SCTV HD
    74. SMTV (720p)
    75. Salam TV (720p)
    76. Sangaji TV (720p)
    77. SindoNews
    78. Sooriyan TV (1080p)
    79. Sriwijaya TV (720p) [Not 24/7]
    80. Stara TV Bojonegoro (720p)
    81. Stara TV Jakarta (1080p)
    82. Stara TV Parahyangan (720p)
    83. TV Mu (720p) [Not 24/7]
    84. TVE Star (576p)
    85. TVE Star HD (1080p)
    86. TVRI (1080i)
    87. TVRI Aceh (720p)
    88. TVRI Bali (480p)
    89. TVRI Bangka Belitung (480p)
    90. TVRI Bengkulu (480p)
    91. TVRI Gorontalo (480p)
    92. TVRI Jakarta (576i) [Not 24/7]
    93. TVRI Jambi (720p) [Not 24/7]
    94. TVRI Jawa Tengah (720p)
    95. TVRI Kalimantan Barat (480p)
    96. TVRI Kalimantan Selatan (720p)
    97. TVRI Kalimantan Tengah (480p)
    98. TVRI Kalimantan Timur (720p)
    99. TVRI Lampung (720p)
    100. TVRI Maluku (480p)
    101. TVRI North Sulawesi (1080p)
    102. TVRI North Sumatra (1080p)
    103. TVRI Nusa Tenggara Barat (720p)
    104. TVRI Nusa Tenggara Timur (480p)
    105. TVRI Papua (480p)
    106. TVRI Riau
    107. TVRI Riau (720p) [Not 24/7]
    108. TVRI Sulawesi Barat (720p)
    109. TVRI Sulawesi Selatan (480p)
    110. TVRI Sulawesi Tengah (720p)
    111. TVRI Sulawesi Tenggara (480p)
    112. TVRI Sumatera Barat (720p)
    113. TVRI Sumatera Selatan (480p)
    114. TVRI WORLD
    115. TVRI West Papua (1080p)
    116. TVRI Yogyakarta (720p)
    117. The Indonesia Channel (1080p)
    118. Timor TV
    119. U Channel
    120. UCL (720p)
    121. dTVi
    122. iNews HD
    123. Хузур ТВ (1080p) [Not 24/7]

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
