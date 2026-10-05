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
    2. I news
    3. Jtv
    4. Kompas tv
    5. Max sport
    6. Rtv
    7. Sctv

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
    6. Dens tv learning
    7. Dhamma tv (720p) [not 24/7]
    8. Dhoho tv (720p)
    9. Duta tv (360p) [not 24/7]
    10. Efarina tv (720p)
    11. Indonesiana tv
    12. Izzah tv (480p)
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
    25. Pontv (720p)
    26. R tv
    27. Radar tasikmalaya tv (720p) [not 24/7]
    28. Radio kita tv (1080p)
    29. Salira tv (720p)
    30. Smtv (720p) [not 24/7]
    31. Stara tv (720p)
    32. Stara tv bandung (1080p)
    33. Stara tv cianjur (720p)
    34. Stara tv malang (1080p)
    35. Tatv (720p) [not 24/7]
    36. Tv one
    37. Tv tabalong (720p) [not 24/7]
    38. Tv9 nusantara (720p)
    39. Tvri jawa barat (480p)
    40. Tvri world
    41. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (170 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV HD
    5. Abadan
    6. Ahsan TV
    7. Ajman TV (1080p)
    8. Al Qamar TV (1080p)
    9. Anadolu Net TV (1080p)
    10. Angel TV Indonesia (720p)
    11. Ashiil TV (480p)
    12. Astro Blitar TV (720p)
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
    24. Balapan International (1080p)
    25. Bali TV
    26. Balikpapan TV (720p)
    27. Bandung TV
    28. Banjar TV (720p) [Not 24/7]
    29. Batam TV (480p) [Not 24/7]
    30. Berita Satu
    31. Berita Satu (Maxstream)
    32. Bungo TV
    33. CNBC Indonesia (ChannelFeed)
    34. CNN Indonesia (ChannelFeed)
    35. Canal 24 Horas (720p)
    36. Cao Bằng TV (720p)
    37. CelebritiesTV (V+)
    38. Clan Internacional Americas (1080p) [Geo-blocked]
    39. DAAI TV (Dens)
    40. DMI TV (576i)
    41. EmanTv (1080p)
    42. Entertainment (V+)
    43. Fashion TV
    44. Ficom Channel
    45. Food Travel (V+)
    46. GTV
    47. Garuda TV (Flashcon)
    48. Hanacaraka TV (V+)
    49. Hmong Star TV (720p) [Not 24/7]
    50. Hyder TV (720p)
    51. I Am Channel (576p)
    52. IDX (Maxstream)
    53. IDX (V+)
    54. Indonesia Movie Channel (V+)
    55. Indosiar
    56. Indosiar (Maxstream)
    57. Indosiar HD
    58. Inter TV (1080p)
    59. Iunior TV (1080p)
    60. JAKTV
    61. JTV (720p)
    62. JTV (V+)
    63. JTV Kediri (1080p) [Not 24/7]
    64. JTV Madiun
    65. JTV Madura (480p) [Not 24/7]
    66. JTV Malang
    67. Jagantara TV
    68. Kompas TV HD (Maxstream)
    69. Kordia TV (1080p)
    70. La 2
    71. Lingkar TV
    72. Love the Planet (1080p)
    73. MAGNA Channel (DensTV)
    74. MAGNA TV (ChannelFeed)
    75. MBG TV (1080p)
    76. MDTV
    77. MDTV (DensTV)
    78. MOJI TV HD (Alt 3 - DensTV flashcon)
    79. MTV Ridiculousness
    80. MTV Ridiculousness (720p)
    81. Madani TV (720p)
    82. Matrix TV Yogyakarta (720p)
    83. MetroTV (DensTV)
    84. MetroTV (Flashcon)
    85. Nusantara TV (ChannelFeed)
    86. Nusantara TV (Maxstream)
    87. Omid e Iran TV
    88. Outdoor Channel (1080p)
    89. PKTV (480p)
    90. Peer TV Sudtirol (1080p)
    91. RCTV (Indonesia) (720p) [Not 24/7]
    92. RRI Net (1080p)
    93. RTV (Maxstream)
    94. Radar Lampung TV (480p)
    95. Radio 51 TV
    96. Rajawali TV
    97. Regio TV (406p)
    98. Riau TV (1080p) [Not 24/7]
    99. Rinjani TV
    100. SCTV
    101. SCTV (DASH/MPD)
    102. SCTV (Maxstream)
    103. SCTV (Vidio)
    104. SCTV HD
    105. SIN PO TV (Maxstream)
    106. SMTV (720p)
    107. STV (Indonesia) (720p) [Not 24/7]
    108. Salam TV (720p)
    109. Sangaji TV (720p)
    110. SindoNews
    111. SindoNews (Maxstream)
    112. SindoNews (V+)
    113. Sooriyan TV (1080p)
    114. Sriwijaya TV (720p) [Not 24/7]
    115. Stara TV Bojonegoro (720p)
    116. Stara TV Jakarta (1080p)
    117. Stara TV Parahyangan (720p)
    118. Szlagier TV
    119. TLC HD
    120. TV Mu (720p) [Not 24/7]
    121. TVE Star (576p)
    122. TVE Star HD (1080p)
    123. TVOne (V+)
    124. TVRI
    125. TVRI (1080i)
    126. TVRI Aceh (720p)
    127. TVRI Bali (480p)
    128. TVRI Bangka Belitung (480p)
    129. TVRI Bengkulu (480p)
    130. TVRI Gorontalo (480p)
    131. TVRI Jakarta (576i) [Not 24/7]
    132. TVRI Jambi (720p) [Not 24/7]
    133. TVRI Jawa Tengah (720p)
    134. TVRI Jawa Timur (720p)
    135. TVRI Kalimantan Barat (480p)
    136. TVRI Kalimantan Selatan (720p)
    137. TVRI Kalimantan Tengah (480p)
    138. TVRI Kalimantan Timur (720p)
    139. TVRI Lampung (720p)
    140. TVRI Maluku (480p)
    141. TVRI North Sulawesi (1080p)
    142. TVRI North Sumatra (1080p)
    143. TVRI Nusa Tenggara Barat (720p)
    144. TVRI Nusa Tenggara Timur (480p)
    145. TVRI Papua (480p)
    146. TVRI Riau
    147. TVRI Riau (720p) [Not 24/7]
    148. TVRI Sulawesi Barat (720p)
    149. TVRI Sulawesi Selatan (480p)
    150. TVRI Sulawesi Tengah (720p)
    151. TVRI Sulawesi Tenggara (480p)
    152. TVRI Sumatera Barat (720p)
    153. TVRI Sumatera Selatan (480p)
    154. TVRI WORLD
    155. TVRI West Papua (1080p)
    156. TVRI World (Maxstream)
    157. TVRI Yogyakarta (720p)
    158. The Indonesia Channel (1080p)
    159. Timor TV
    160. Trans7 (Transcorp)
    161. Trans7 HD
    162. TransTV (Transcorp)
    163. U Channel
    164. UCL (1080p)
    165. UCL (720p)
    166. VTV
    167. Vision Prime (V+)
    168. iNews (Maxstream)
    169. iNews HD
    170. Хузур ТВ (1080p) [Not 24/7]

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
