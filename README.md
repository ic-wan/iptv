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

- `ich-iptv.m3u` — Playlist utama channel IPTV aktif.
- `hapus.m3u` — Arsip cadangan untuk link channel yang sedang mati.
- `epg-ich.xml.gz` — File panduan acara (EPG) terkompresi untuk seluruh channel.
- `List_program.txt` — Laporan rekapitulasi daftar channel dan grup.
- `keyword.txt` — Konfigurasi kata kunci pencarian channel.
- `blacklist_program.txt` — Daftar hitam channel/program yang ingin diabaikan.
- `m3u_source.txt` — Daftar tautan sumber M3U eksternal.
- `youtube_source.txt` — Daftar tautan sumber playlist/live stream YouTube.
- `epg_source.txt` — Daftar tautan atau sumber data EPG eksternal.
- `generate_epg.py` — Skrip utama untuk mengambil dan menghasilkan data EPG.
- `generate_youtube_m3u.py` — Skrip untuk mengonversi dan menggabungkan stream YouTube.
- `.github/workflows/update-m3u-epg.yml` — Konfigurasi otomatisasi GitHub Actions.

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

  📁 Grup: [Entertainment] (3 Channel)
  ----------------------------------------
    1. Just for laughs gags (720p)
    2. Pluto tv science
    3. Top gear

  📁 Grup: [INDONESIA] (1 Channel)
  ----------------------------------------
    1. Indonesia raya

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

  📁 Grup: [Kids] (11 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Biznet kids (1080p)
    4. Forever kids
    5. Kidsflix (1080p) [not 24/7]
    6. Lego kids tv
    7. Moonbug kids (1080p)
    8. Nick jr. pluto tv
    9. Nickelodeon
    10. Pbs kids
    11. Vtv (720p)

  📁 Grup: [Lokal] (58 Channel)
  ----------------------------------------
    1. Atambua tv (720p)
    2. Bandung tv (360p)
    3. Banten tv (720p) [not 24/7]
    4. Banyumas tv (720p) [not 24/7]
    5. Biznet adventure (1080p)
    6. Biznet lifestyle (1080p)
    7. Bn channel (720p)
    8. Brtv (720p)
    9. Bungo tv (480p) [not 24/7]
    10. Caruban tv (1080p)
    11. Cnbc hd
    12. Cnn 1 hd
    13. Cnn 2
    14. Daai tv
    15. Dens tv learning
    16. Dhamma tv (720p) [not 24/7]
    17. Dhoho tv (720p)
    18. Duta tv (360p) [not 24/7]
    19. Efarina tv (720p)
    20. Garuda tv (1080p)
    21. Indonesiana tv
    22. Izzah tv (480p)
    23. Jawa pos tv jakarta (720p)
    24. Jogja istimewa tv (720p)
    25. Jowo
    26. Jtv (480p)
    27. Kawanua tv (720p)
    28. Kompas tv
    29. Ktv (720p)
    30. Lingkar tv
    31. Madani tv (720p)
    32. Magna channel (1080p) [not 24/7]
    33. Metro tv
    34. Moji tv
    35. Mqtv (720p) [not 24/7]
    36. Nhk world japan
    37. Nusantara tv (1080p)
    38. Padang tv (720p) [not 24/7]
    39. Pontv (720p)
    40. R tv
    41. Radio kita tv (1080p)
    42. Rodja tv (720p)
    43. Rri net (1080p)
    44. Salira tv (720p)
    45. Smtv (720p) [not 24/7]
    46. Stara tv (720p)
    47. Stara tv bandung (1080p)
    48. Stara tv cianjur (720p)
    49. Stara tv malang (1080p)
    50. Timor tv (1080p)
    51. Tv one
    52. Tv tabalong (720p) [not 24/7]
    53. Tv9 nusantara (720p)
    54. Tvku (720p)
    55. Tvri jawa barat (480p)
    56. Tvri jawa timur (720p)
    57. Tvri world
    58. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (137 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ANTV HD (Alt 3 - DensTV flashcon)
    3. Abadan
    4. Ahsan TV
    5. Ajwa TV (1080p)
    6. Al Qamar TV (1080p)
    7. Al Quran Al Kareem TV (720p)
    8. Anadolu Net TV (1080p)
    9. Angel TV Indonesia (720p)
    10. Ashiil TV (480p)
    11. Astro Blitar TV (720p)
    12. Atambua TV (720p)
    13. Atomic Academy TV (480p)
    14. Atomic TV (360p)
    15. Aupur Television (1080p)
    16. Azan TV
    17. BALI TV
    18. BBC LIFESTYLE
    19. BIOSKOP INDONESIA
    20. BN Channel (ChannelFeed)
    21. Baan Baan TV 73
    22. Balapan HD (1080p)
    23. Balapan International (1080p)
    24. Balikpapan TV (720p)
    25. Banjar TV (720p) [Not 24/7]
    26. Batam TV (480p) [Not 24/7]
    27. CBC (576p)
    28. CBC Drama (576p)
    29. CBC Sofra (576p)
    30. CNBC Indonesia (ChannelFeed)
    31. CNN INDONESIA
    32. CNN INDONESIA HD
    33. CNN Indonesia (ChannelFeed)
    34. CNN https://live.cnnindonesia.com/livecnn/smil:cnntv.smil/playlist.m3u8
    35. Canal 24 Horas (720p)
    36. Cao Bằng TV (720p)
    37. Clan Internacional Americas (1080p) [Geo-blocked]
    38. DAAI TV (Dens)
    39. DMI TV (576i)
    40. EmanTv (1080p)
    41. Fajar TV (720p) [Not 24/7]
    42. Ficom Channel
    43. Food Travel (V+)
    44. Garuda TV (ChannelFeed)
    45. Garuda TV (Flashcon)
    46. Garuda TV HD
    47. Hmong Star TV (720p) [Not 24/7]
    48. Hyder TV (720p)
    49. I Am Channel (576p)
    50. Indosiar
    51. Indosiar HD
    52. Inter TV (1080p)
    53. Iunior TV (1080p)
    54. JAKTV
    55. JTV Kediri (1080p) [Not 24/7]
    56. JTV Madiun
    57. JTV Madura (480p) [Not 24/7]
    58. JTV Malang
    59. Jogja TV (720p) [Not 24/7]
    60. Kids TV
    61. Kompas TV HD (Alt 3 - DensTV flashcon)
    62. Kordia TV (1080p)
    63. La 2
    64. Libya Al Ahrar TV (1080p)
    65. Love the Planet (1080p)
    66. MAGNA Channel (Flashcon)
    67. MAGNA TV (ChannelFeed)
    68. MBG TV (1080p)
    69. MDTV
    70. MDTV HD
    71. MOJI TV HD (Alt 3 - DensTV flashcon)
    72. MTV Ridiculousness
    73. MTV Ridiculousness (720p)
    74. Matrix TV Yogyakarta (720p)
    75. Metro TV
    76. MetroTV (Flashcon)
    77. Music JapanTV
    78. Nusantara TV (ChannelFeed)
    79. Outdoor Channel (1080p)
    80. PKTV (480p)
    81. Radio 51 TV
    82. Rajawali TV
    83. Rinjani TV
    84. SCTV (DASH/MPD)
    85. SCTV HD (Alt 3 - DensTV flashcon)
    86. Salam TV (720p)
    87. Sangaji TV (720p)
    88. SindoNews
    89. Sooriyan TV (1080p)
    90. Sriwijaya TV (720p) [Not 24/7]
    91. Stara TV Bojonegoro (720p)
    92. Stara TV Jakarta (1080p)
    93. Stara TV Parahyangan (720p)
    94. Surau TV (720p)
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
    128. TVRI World
    129. TVRI Yogyakarta (720p)
    130. The Indonesia Channel (1080p)
    131. Trans7 HD
    132. TransTV HD
    133. U Channel
    134. UCL (720p)
    135. VTV HD (1080p)
    136. group-title="Lokal (auto)"CNN TV https://live.cnnindonesia.com/livecnn/smil:cnntv.smil/chunklist_w1299546647_b384000_sleng.m3u8
    137. Хузур ТВ (1080p) [Not 24/7]

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

📂 SUMBER FILE: Arsip Link Mati (hapus.m3u)
=============================================

  📁 Grup: [Indihome] (10 Channel)
  ----------------------------------------
    1. Cartoonito
    2. Cinemax
    3. Discovery
    4. Global tv
    5. Hbo
    6. Hbo hits
    7. Hbo signature
    8. Mnc tv
    9. Rcti
    10. Warner tv

  📁 Grup: [Lokal] (9 Channel)
  ----------------------------------------
    1. Be tv (720p)
    2. Davika tv (480p)
    3. Discovery channel
    4. Madu tv (576p)
    5. Palembang tv (720p)
    6. Radar tasikmalaya tv (720p) [not 24/7]
    7. Rakyat bengkulu tv (720p)
    8. Tatv (720p) [not 24/7]
    9. Tvr parlemen (720p) [not 24/7]

  📁 Grup: [Lokal (auto)] (209 Channel)
  ----------------------------------------
    1. (ID) TVRI ACEH
    2. (ID) TVRI BALI
    3. (ID) TVRI BANGKA BELITUNG
    4. (ID) TVRI BENGKULU
    5. (ID) TVRI DKI JAKARTA
    6. (ID) TVRI GORONTALO
    7. (ID) TVRI JAMBI
    8. (ID) TVRI JAWA BARAT
    9. (ID) TVRI JAWA TENGAH
    10. (ID) TVRI JAWA TIMUR
    11. (ID) TVRI KALIMANTAN BARAT
    12. (ID) TVRI KALIMANTAN SELATAN
    13. (ID) TVRI KALIMANTAN TENGAH
    14. (ID) TVRI KALIMANTAN TIMUR
    15. (ID) TVRI LAMPUNG
    16. (ID) TVRI MALUKU
    17. (ID) TVRI NASIONAL
    18. (ID) TVRI NUSA TENGGARA BARAT
    19. (ID) TVRI NUSA TENGGARA TIMUR
    20. (ID) TVRI OLAHRAGA
    21. (ID) TVRI PAPUA
    22. (ID) TVRI RIAU
    23. (ID) TVRI SULAWESI BARAT
    24. (ID) TVRI SULAWESI SELATAN
    25. (ID) TVRI SULAWESI TENGAH
    26. (ID) TVRI SULAWESI TENGGARA
    27. (ID) TVRI SULAWESI UTARA
    28. (ID) TVRI SUMATERA BARAT
    29. (ID) TVRI SUMATERA SELATAN
    30. (ID) TVRI SUMATERA UTARA
    31. (ID) YOGYAKARTA
    32. ABC Big Kids All Aussie
    33. ANTV
    34. ANTV (1080p)
    35. ANTV (720p)
    36. ANTV - LOCAL
    37. ANTV HD
    38. ANTV HD (Alt 2)
    39. ANTV http://id2.indostreamingtv.com/live/antv/index.m3u8
    40. ATV (1080p)
    41. Advocate Broadcasting Network
    42. Ajman TV (1080p)
    43. Al-Iman TV (720p)
    44. Angel TV Indonesia
    45. Antara TV
    46. Aragon TV Internacional (720p) [Not 24/7]
    47. Asia TV (720p)
    48. BACKUP ANTV
    49. BACKUP CNBC Indonesia
    50. BACKUP INDOSIAR 2
    51. BACKUP INDOSIAR 3
    52. BACKUP JTV 2
    53. BACKUP JTV 3
    54. BACKUP SCTV 2
    55. BACKUP SCTV 3
    56. BERITA SATU - LOCAL
    57. BERITA SATU HD
    58. BERITA SATU http://edge.linknetott.swiftserve.com/live/BsNew/amlst:beritasatunewsbs/playlist.m3u8
    59. BIOSKOP INDONESIA
    60. BIZNET KIDS
    61. BTV
    62. BTV (V+)
    63. BTV [Geo-blocked]
    64. Bali TV
    65. Bandung TV
    66. Batam TV
    67. Berita Satu (DensTV)
    68. BeritaSatu (1080p)
    69. Bioskop Indonesia
    70. CITRA ENTERTAINMENT
    71. CNBC INDONESIA
    72. CelebritiesTV (V+)
    73. DAAI TV - LOCAL
    74. DAAI TV HD
    75. DAAI TV HD (Alt 2)
    76. DAAI TV http://210.210.155.35/qwr9ew/s/s13/01.m3u8
    77. Dens Life Style
    78. Entertainment (V+)
    79. Fajar TV (240p) [Not 24/7]
    80. First Lifestyle
    81. GLOBAL TV+ https://live.rctiplus.id/rctiplus/gtv_720p.m3u8
    82. GTV
    83. GTV HD
    84. Groovia Kanal
    85. Hanacaraka TV (V+)
    86. Hispan TV
    87. Hunan TV
    88. IDTV (720p) [Not 24/7]
    89. IDX (V+)
    90. INDOSIAR - LOCAL
    91. INDOSIAR BRI Super LIG
    92. INDOSIAR HD http://id1.indostreamingtv.com/live/indosiar/index.m3u8
    93. INDOSIAR http://id1.indostreamingtv.com/live/indosiar/index.m3u
    94. INEWS+ https://live.rctiplus.id/rctiplus/inews_720p.m3u8
    95. Iman TV (480p)
    96. Indonesia Movie Channel (V+)
    97. Indosiar
    98. Indosiar HD
    99. Indosiar HD (Alt 2)
    100. JAKTV - LOCAL
    101. JTV
    102. JTV (V+)
    103. Jak TV [Geo-blocked]
    104. Jambi TV
    105. KOMPAS TV
    106. KOMPASTV
    107. Kanal 10 Asia (540p)
    108. Kompas TV HD
    109. Kompas TV HD (Alt 2)
    110. KompasTV
    111. Love The Planet DE (1080p) [Geo-blocked]
    112. MAGNA Channel
    113. MAX KIDS
    114. MDTV
    115. MDTV HD
    116. MDTV HD (Alt 2)
    117. MENTARI TV HD
    118. METRO TV - LOCAL
    119. METRO TV HD http://edge.metrotvnews.com:1935/live-edge/smil:metro.smil/chunklist_w2006790992_b1492000_sleng.m3u8
    120. METROTV
    121. MNC TV
    122. MNC TV HD
    123. MNCTV
    124. MNCTV HD (720p)
    125. MOJI TV (Video)
    126. MOJI TV HD
    127. MOJI TV HD (Alt 2)
    128. MUSIC TOP
    129. Max Reels
    130. Mentari TV FHD
    131. Metro TV HD (Alt 2)
    132. MetroTV
    133. Music JapanTV
    134. NET TV
    135. NET TV HD http://id2.indostreamingtv.com/live/nettv/index.m3u8
    136. Naajiya TV (720p)
    137. PLANET FUN
    138. RCTI
    139. RCTI HD
    140. RCTI HD (720p)
    141. RCTI HD (Alt 2)
    142. RCTI SPORTS
    143. RTV
    144. RTV (V+)
    145. RTV (Vidio)
    146. RTV http://210.210.155.35/qwr9ew/s/s12/index1.m3u8
    147. Radar Lampung TV (480p)
    148. Riau TV
    149. Riau TV (1080p) [Not 24/7]
    150. SCTV
    151. SCTV (DASH/MPD)
    152. SCTV - LOCAL
    153. SCTV HD
    154. SCTV HD (Alt 2)
    155. SCTV HD http://id1.indostreamingtv.com/live/sctv/index.m3u8
    156. SCTV [Geo-blocked]
    157. SIN PO TV
    158. SIN PO TV HD
    159. SKY SPORT F1
    160. SMTV (720p)
    161. TLC HD
    162. TRANS 7 TV
    163. TRANS 7 http://video.detik.com/trans7/smil:trans7.smil/chunklist_w1925750281_b384000_sleng.m3u8
    164. TRANS TV + http://id2.indostreamingtv.com/live/tv33/index.m3u8
    165. TRANS TV - LOCAL
    166. TRANS TV http://video.detik.com/transtv/smil:transtv.smil/chunklist_w1982763047_b384000_sleng.m3u8
    167. TRANS7 - LOCAL
    168. TV ONE - LOCAL
    169. TV ONE http://id1.indostreamingtv.com/live/tv444/index.m3u8
    170. TVKU
    171. TVOne
    172. TVOne (V+)
    173. TVOne (V+) (Alt 2)
    174. TVOne HD
    175. TVOne HD (Alt 2)
    176. TVR Parlemen (720p) [Not 24/7]
    177. TVRI
    178. TVRI (480p) [Geo-blocked]
    179. TVRI + http://ott.tvri.co.id/Content/HLS/Live/Channel(TVRINasional)/Stream(02)/index.m3u8
    180. TVRI - LOCAL
    181. TVRI NASIONAL
    182. TVRI Sport HD
    183. TVRI Sport [Geo-blocked]
    184. Tegar TV Lampung (480p) [Not 24/7] [Geo-blocked]
    185. Trans TV cad
    186. Trans7 HD
    187. Trans7 HD (Alt 2)
    188. TransTV HD
    189. TransTV HD (Alt 2)
    190. Unknown 4
    191. Vision Prime (V+)
    192. dTVi
    193. group-title="Lokal (auto)"INDOSIAR http://210.210.155.35/session/9ec7c73c-099b-11ea-aff4-b82a72d63267/qwr9ew/s/s04/01.m3u8
    194. group-title="Lokal (auto)"INEWSTV https://cdn-livetv5.metube.id/hls/inewstv_240/index.m3u8
    195. group-title="Lokal (auto)"JAKTV https://cdn-livetv1.metube.id/hls/jaktv_480/536549.ts
    196. group-title="Lokal (auto)"JTV https://cdn-livetv1.metube.id/hls/jtv_240/index.m3u8
    197. group-title="Lokal (auto)"METROTV http://edge.metrotvnews.com:1935/live-edge/smil:metro.smil/chunklist_w391596422_b1492000_sleng.m3u8
    198. group-title="Lokal (auto)"MNCTV http://id6.indostreamingtv.com/live/mnctv/index.m3u8
    199. group-title="Lokal (auto)"RCTI http://id6.indostreamingtv.com/live/rcti/index.m3u8
    200. group-title="Lokal (auto)"RTV http://210.210.155.35/session/0c55f20a-0998-11ea-875c-b82a72d63267/qwr9ew/s/s12/01.m3u8
    201. group-title="Lokal (auto)"SCTV https://cdn-livetv1.metube.id/hls/sctv_480/index.m3u8
    202. group-title="Lokal (auto)"TRANS7 http://id2.indostreamingtv.com/live/trans7/index.m3u8
    203. group-title="Lokal (auto)"TVONE https://cdn-livetv1.metube.id/hls/tvone_240/index.m3u8
    204. group-title="Lokal (auto)"TVRI https://cdn-livetv1.metube.id/hls/tvri_480/index.m3u8
    205. http://oromartv.com/wp-content/uploads/2016/05/oromartv-logo.png"
    206. iNews
    207. iNews HD
    208. iNews HD (720p)
    209. tvOne [Geo-blocked]

=============================================


```
<!-- END_PROGRAM_LIST -->
