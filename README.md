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

  📁 Grup: [Lokal (auto)] (144 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ANTV HD
    3. Abadan
    4. Ahsan TV
    5. Ajwa TV (1080p)
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
    16. BERITASATU
    17. BN Channel (ChannelFeed)
    18. BRTV (720p)
    19. Baan Baan TV 73
    20. Balapan HD (1080p)
    21. Balapan International (1080p)
    22. Balikpapan TV (720p)
    23. Bandung TV (360p)
    24. Batam TV (480p) [Not 24/7]
    25. Bungo TV
    26. CBC (576p)
    27. CBC Drama (576p)
    28. CBC Sofra (576p)
    29. Canal 24 Horas (720p)
    30. Cao Bằng TV (720p)
    31. Caruban TV (1080p)
    32. Channel Jowo (DensTV)
    33. Clan Internacional Americas (1080p) [Geo-blocked]
    34. DAAI TV
    35. DAAI TV (Dens)
    36. DMI TV (576i)
    37. Dhamma TV (720p) [Not 24/7]
    38. EmanTv (1080p)
    39. Food Travel (V+)
    40. Garuda TV (1080p)
    41. Garuda TV (Flashcon)
    42. Hmong Star TV (720p) [Not 24/7]
    43. Hyder TV (720p)
    44. I Am Channel (576p)
    45. INEWS
    46. Indonesiana.TV (720p)
    47. Indosiar
    48. Indosiar HD
    49. Inter TV (1080p)
    50. Iunior TV (1080p)
    51. JAKTV
    52. JTV
    53. JTV (720p)
    54. JTV Kediri (1080p) [Not 24/7]
    55. JTV Madiun
    56. JTV Malang
    57. Jawa Pos TV Jakarta (720p)
    58. Jogja TV (720p) [Not 24/7]
    59. KOMPAS TV
    60. Kompas TV HD
    61. Kordia TV (1080p)
    62. La 2
    63. Libya Al Ahrar TV (1080p)
    64. Lingkar TV
    65. Love the Planet (1080p)
    66. MAGNA Channel (Flashcon)
    67. MAGNA TV (ChannelFeed)
    68. MBG TV (1080p)
    69. MDTV
    70. MOJI TV (Dens)
    71. MOJI TV HD (Alt 3 - DensTV flashcon)
    72. MTV Ridiculousness
    73. MTV Ridiculousness (720p)
    74. Madani TV (720p)
    75. Magna Channel (1080p)
    76. Matrix TV Yogyakarta (720p)
    77. Metro TV
    78. MetroTV (Flashcon)
    79. Outdoor Channel (1080p)
    80. PKTV (480p)
    81. RRI Net (1080p)
    82. RTV
    83. RTV (Dens)
    84. Radio 51 TV
    85. Rajawali TV
    86. Riau TV (1080p) [Not 24/7]
    87. SCTV (DASH/MPD)
    88. SCTV HD
    89. SMTV (720p)
    90. Salam TV (720p)
    91. Sangaji TV (720p)
    92. SindoNews
    93. Sooriyan TV (1080p)
    94. Sriwijaya TV (720p) [Not 24/7]
    95. Stara TV Bojonegoro (720p)
    96. Stara TV Jakarta (1080p)
    97. Stara TV Parahyangan (720p)
    98. Surau TV (720p)
    99. TV9 Nusantara (720p)
    100. TVE Star (576p)
    101. TVE Star HD (1080p)
    102. TVKU (720p)
    103. TVOne (DensTV)
    104. TVRI (1080i)
    105. TVRI Aceh (720p)
    106. TVRI Bali (480p)
    107. TVRI Bangka Belitung (480p)
    108. TVRI Bengkulu (480p)
    109. TVRI Gorontalo (480p)
    110. TVRI Jakarta (576i) [Not 24/7]
    111. TVRI Jambi (720p) [Not 24/7]
    112. TVRI Jawa Barat (480p)
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
    134. TVRI WORLD
    135. TVRI West Papua (1080p)
    136. TVRI World (1080p)
    137. TVRI Yogyakarta (720p)
    138. The Indonesia Channel (1080p)
    139. U Channel
    140. UCL (720p)
    141. UGTV (720p)
    142. VTV (720p)
    143. VTV HD (1080p)
    144. Хузур ТВ (1080p) [Not 24/7]

  📁 Grup: [Uncategorized] (1 Channel)
  ----------------------------------------
    1. Unknown

=============================================
```
<!-- END_PROGRAM_LIST -->
