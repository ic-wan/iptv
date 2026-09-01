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

  📁 Grup: [Lokal] (2 Channel)
  ----------------------------------------
    1. Radar tasikmalaya tv (720p) [not 24/7]
    2. Tv one

  📁 Grup: [Lokal (auto)] (160 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ABC Big Kids All Aussie
    3. ANTV HD
    4. Abadan
    5. Ahsan TV
    6. Ajwa TV (1080p)
    7. Al Qamar TV (1080p)
    8. Anadolu Net TV (1080p)
    9. Angel TV Indonesia (720p)
    10. Ashiil TV (480p)
    11. Astro Blitar TV (720p)
    12. Atomic Academy TV (480p)
    13. Atomic TV (360p)
    14. Azan TV
    15. BALI TV
    16. BBC LIFESTYLE
    17. BERITASATU
    18. BN Channel (ChannelFeed)
    19. BRTV (720p)
    20. Baan Baan TV 73
    21. Balapan HD (1080p)
    22. Balapan International (1080p)
    23. Balikpapan TV (720p)
    24. Bandung TV (360p)
    25. Banjar TV (720p) [Not 24/7]
    26. Batam TV (480p) [Not 24/7]
    27. Bungo TV
    28. CBC (576p)
    29. CBC Drama (576p)
    30. CBC Sofra (576p)
    31. CNBC Indonesia (ChannelFeed)
    32. CNN
    33. CNN INDONESIA
    34. CNN INDONESIA HD
    35. CNN Indonesia (ChannelFeed)
    36. Canal 24 Horas (720p)
    37. Cao Bằng TV (720p)
    38. Caruban TV (1080p)
    39. Channel Jowo (DensTV)
    40. Clan Internacional Americas (1080p) [Geo-blocked]
    41. DAAI TV
    42. DAAI TV (Dens)
    43. DMI TV (576i)
    44. Dhamma TV (720p) [Not 24/7]
    45. EmanTv (1080p)
    46. Fajar TV (720p) [Not 24/7]
    47. Ficom Channel
    48. Food Travel (V+)
    49. Garuda TV (1080p)
    50. Garuda TV (Flashcon)
    51. Hmong Star TV (720p) [Not 24/7]
    52. Hyder TV (720p)
    53. I Am Channel (576p)
    54. INEWS
    55. Indonesiana.TV (720p)
    56. Indosiar
    57. Indosiar HD
    58. Inter TV (1080p)
    59. Iunior TV (1080p)
    60. JAKTV
    61. JTV
    62. JTV (720p)
    63. JTV Kediri (1080p) [Not 24/7]
    64. JTV Madiun
    65. JTV Malang
    66. Jawa Pos TV Jakarta (720p)
    67. Jogja TV (720p) [Not 24/7]
    68. KOMPAS TV
    69. Kids TV
    70. Kompas TV HD
    71. Kordia TV (1080p)
    72. La 2
    73. Libya Al Ahrar TV (1080p)
    74. Lingkar TV
    75. Love the Planet (1080p)
    76. MAGNA Channel (Flashcon)
    77. MAGNA TV (ChannelFeed)
    78. MBG TV (1080p)
    79. MDTV
    80. MOJI TV (Dens)
    81. MOJI TV HD (Alt 3 - DensTV flashcon)
    82. MTV Ridiculousness
    83. MTV Ridiculousness (720p)
    84. Madani TV (720p)
    85. Magna Channel (1080p)
    86. Matrix TV Yogyakarta (720p)
    87. Metro TV
    88. MetroTV (Flashcon)
    89. Nusantara TV (ChannelFeed)
    90. Outdoor Channel (1080p)
    91. PKTV (480p)
    92. RRI Net (1080p)
    93. RTV
    94. RTV (Dens)
    95. Radar Lampung TV (480p)
    96. Radio 51 TV
    97. Rajawali TV
    98. Riau TV (1080p) [Not 24/7]
    99. Rinjani TV
    100. SCTV (DASH/MPD)
    101. SCTV HD
    102. SMTV (720p)
    103. Salam TV (720p)
    104. Sangaji TV (720p)
    105. SindoNews
    106. Sooriyan TV (1080p)
    107. Sriwijaya TV (720p) [Not 24/7]
    108. Stara TV Bojonegoro (720p)
    109. Stara TV Jakarta (1080p)
    110. Stara TV Parahyangan (720p)
    111. Surau TV (720p)
    112. TV Mu (720p) [Not 24/7]
    113. TV9 Nusantara (720p)
    114. TVE Star (576p)
    115. TVE Star HD (1080p)
    116. TVKU (720p)
    117. TVOne (DensTV)
    118. TVRI (1080i)
    119. TVRI Aceh (720p)
    120. TVRI Bali (480p)
    121. TVRI Bangka Belitung (480p)
    122. TVRI Bengkulu (480p)
    123. TVRI Gorontalo (480p)
    124. TVRI Jakarta (576i) [Not 24/7]
    125. TVRI Jambi (720p) [Not 24/7]
    126. TVRI Jawa Barat (480p)
    127. TVRI Jawa Tengah (720p)
    128. TVRI Jawa Timur (720p)
    129. TVRI Kalimantan Barat (480p)
    130. TVRI Kalimantan Selatan (720p)
    131. TVRI Kalimantan Tengah (480p)
    132. TVRI Kalimantan Timur (720p)
    133. TVRI Lampung (720p)
    134. TVRI Maluku (480p)
    135. TVRI North Sulawesi (1080p)
    136. TVRI North Sumatra (1080p)
    137. TVRI Nusa Tenggara Barat (720p)
    138. TVRI Nusa Tenggara Timur (480p)
    139. TVRI Papua (480p)
    140. TVRI Riau
    141. TVRI Riau (720p) [Not 24/7]
    142. TVRI Sulawesi Barat (720p)
    143. TVRI Sulawesi Selatan (480p)
    144. TVRI Sulawesi Tengah (720p)
    145. TVRI Sulawesi Tenggara (480p)
    146. TVRI Sumatera Barat (720p)
    147. TVRI Sumatera Selatan (480p)
    148. TVRI WORLD
    149. TVRI West Papua (1080p)
    150. TVRI World (1080p)
    151. TVRI Yogyakarta (720p)
    152. The Indonesia Channel (1080p)
    153. Timor TV
    154. U Channel
    155. UCL (720p)
    156. UGTV (720p)
    157. VTV (720p)
    158. VTV HD (1080p)
    159. group-title="Lokal (auto)"CNN TV
    160. Хузур ТВ (1080p) [Not 24/7]

  📁 Grup: [Uncategorized] (1 Channel)
  ----------------------------------------
    1. Unknown

=============================================
```
<!-- END_PROGRAM_LIST -->
