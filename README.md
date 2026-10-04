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
    27. Pontv (720p)
    28. R tv
    29. Radar tasikmalaya tv (720p) [not 24/7]
    30. Radio kita tv (1080p)
    31. Rodja tv (720p)
    32. Salira tv (720p)
    33. Smtv (720p) [not 24/7]
    34. Stara tv (720p)
    35. Stara tv bandung (1080p)
    36. Stara tv cianjur (720p)
    37. Stara tv malang (1080p)
    38. Tatv (720p) [not 24/7]
    39. Tv one
    40. Tv tabalong (720p) [not 24/7]
    41. Tv9 nusantara (720p)
    42. Tvri jawa barat (480p)
    43. Tvri world
    44. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (183 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. A Spor SD (1080p)
    3. ABC Australia
    4. ANTV HD
    5. ANTV HD (Transcorp)
    6. ATV (Turkiye) (1080p)
    7. Abadan
    8. Ahsan TV
    9. Ajman TV (1080p)
    10. Al Qamar TV (1080p)
    11. Anadolu Net TV (1080p)
    12. Angel TV Indonesia (720p)
    13. Ashiil TV (480p)
    14. Astro Blitar TV (720p)
    15. Atomic Academy TV (480p)
    16. Atomic TV (360p)
    17. Azan TV
    18. BALI TV
    19. BBC LIFESTYLE
    20. BIOSKOP INDONESIA (Transcorp)
    21. BN Channel (ChannelFeed)
    22. BRTV (720p)
    23. BTV (Channel Feed)
    24. BTV (V+)
    25. Baan Baan TV 73
    26. Balapan HD (1080p)
    27. Balapan International (1080p)
    28. Bali TV
    29. Balikpapan TV (720p)
    30. Bandung TV
    31. Banjar TV (720p) [Not 24/7]
    32. Batam TV (480p) [Not 24/7]
    33. Berita Satu
    34. Berita Satu (Maxstream)
    35. Berita Satu (Transcorp)
    36. Bungo TV
    37. CNBC Indonesia (ChannelFeed)
    38. CNBC Indonesia (Transcorp)
    39. CNN Indonesia (ChannelFeed)
    40. CNN Indonesia (Transcorp)
    41. Canal 24 Horas (720p)
    42. Cao Bằng TV (720p)
    43. CelebritiesTV (V+)
    44. Clan Internacional Americas (1080p) [Geo-blocked]
    45. DAAI TV (Dens)
    46. DMI TV (576i)
    47. EmanTv (1080p)
    48. Entertainment (V+)
    49. Fashion TV
    50. Ficom Channel
    51. Food Travel (V+)
    52. GTV
    53. Garuda TV (1080p)
    54. Garuda TV (Flashcon)
    55. Global TV (Transcorp)
    56. Hanacaraka TV (V+)
    57. Hmong Star TV (720p) [Not 24/7]
    58. Hyder TV (720p)
    59. I Am Channel (576p)
    60. IDX (Maxstream)
    61. IDX (V+)
    62. Indonesia Movie Channel (V+)
    63. Indosiar
    64. Indosiar (Maxstream)
    65. Indosiar (Transcorp)
    66. Indosiar HD
    67. Inter TV (1080p)
    68. Iunior TV (1080p)
    69. JAKTV
    70. JTV (720p)
    71. JTV (V+)
    72. JTV Kediri (1080p) [Not 24/7]
    73. JTV Madiun
    74. Jagantara TV
    75. Kompas TV HD (Maxstream)
    76. Kompas TV HD (Transcorp)
    77. Kordia TV (1080p)
    78. La 2
    79. Lingkar TV
    80. Love the Planet (1080p)
    81. MAGNA Channel (DensTV)
    82. MAGNA TV (ChannelFeed)
    83. MBG TV (1080p)
    84. MDTV
    85. MDTV (DensTV)
    86. MDTV (Transcorp)
    87. MNC TV (Transcorp)
    88. MOJI TV HD (Alt 3 - DensTV flashcon)
    89. MTV Ridiculousness
    90. MTV Ridiculousness (720p)
    91. Madani TV (720p)
    92. Matrix TV Yogyakarta (720p)
    93. Metro TV (Transcorp)
    94. MetroTV (DensTV)
    95. MetroTV (Flashcon)
    96. Myanmar International TV
    97. Nusantara TV (ChannelFeed)
    98. Nusantara TV (Maxstream)
    99. Omid e Iran TV
    100. Outdoor Channel (1080p)
    101. PKTV (480p)
    102. Peer TV Sudtirol (1080p)
    103. RCTI (Transcorp)
    104. RCTV (Indonesia) (720p) [Not 24/7]
    105. RRI Net (1080p)
    106. RTV (Maxstream)
    107. RTV (Transcorp)
    108. Radio 51 TV
    109. Rajawali TV
    110. Regio TV (406p)
    111. Riau TV (1080p) [Not 24/7]
    112. SCTV (DASH/MPD)
    113. SCTV (Maxstream)
    114. SCTV (Transcorp)
    115. SCTV HD
    116. SIN PO TV (Maxstream)
    117. SMTV (720p)
    118. STV (Indonesia) (720p) [Not 24/7]
    119. Salam TV (720p)
    120. Sangaji TV (720p)
    121. SindoNews
    122. SindoNews (Maxstream)
    123. SindoNews (V+)
    124. Sooriyan TV (1080p)
    125. Sriwijaya TV (720p) [Not 24/7]
    126. Stara TV Bojonegoro (720p)
    127. Stara TV Jakarta (1080p)
    128. Stara TV Parahyangan (720p)
    129. Szlagier TV
    130. TLC HD
    131. TV Mu (720p) [Not 24/7]
    132. TVE Star (576p)
    133. TVE Star HD (1080p)
    134. TVOne (Transcorp)
    135. TVOne (V+)
    136. TVRI
    137. TVRI (1080i)
    138. TVRI Aceh (720p)
    139. TVRI Bali (480p)
    140. TVRI Bangka Belitung (480p)
    141. TVRI Bengkulu (480p)
    142. TVRI Gorontalo (480p)
    143. TVRI Jakarta (576i) [Not 24/7]
    144. TVRI Jambi (720p) [Not 24/7]
    145. TVRI Jawa Tengah (720p)
    146. TVRI Jawa Timur (720p)
    147. TVRI Kalimantan Barat (480p)
    148. TVRI Kalimantan Selatan (720p)
    149. TVRI Kalimantan Tengah (480p)
    150. TVRI Kalimantan Timur (720p)
    151. TVRI Lampung (720p)
    152. TVRI Maluku (480p)
    153. TVRI North Sulawesi (1080p)
    154. TVRI North Sumatra (1080p)
    155. TVRI Nusa Tenggara Barat (720p)
    156. TVRI Nusa Tenggara Timur (480p)
    157. TVRI Papua (480p)
    158. TVRI Riau
    159. TVRI Riau (720p) [Not 24/7]
    160. TVRI Sulawesi Barat (720p)
    161. TVRI Sulawesi Selatan (480p)
    162. TVRI Sulawesi Tengah (720p)
    163. TVRI Sulawesi Tenggara (480p)
    164. TVRI Sumatera Barat (720p)
    165. TVRI Sumatera Selatan (480p)
    166. TVRI WORLD
    167. TVRI West Papua (1080p)
    168. TVRI World (Maxstream)
    169. TVRI Yogyakarta (720p)
    170. The Indonesia Channel (1080p)
    171. Timor TV
    172. Trans7 (Transcorp)
    173. Trans7 HD
    174. TransTV (Transcorp)
    175. TransTV HD
    176. U Channel
    177. UCL (1080p)
    178. UCL (720p)
    179. VTV
    180. Vision Prime (V+)
    181. iNews (Maxstream)
    182. iNews HD
    183. Хузур ТВ (1080p) [Not 24/7]

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
