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
- `epg_source.txt` (atau format file terkait) — Daftar tautan atau sumber data EPG eksternal.
- `generate_epg.py` — Skrip utama untuk mengambil dan menghasilkan data EPG.
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

  📁 Grup: [Indihome] (10 Channel)
  ----------------------------------------
    1. Berita satu
    2. Cinemax
    3. Discovery
    4. I news
    5. Jtv
    6. Kompas tv
    7. Max sport
    8. Prambors tv
    9. Rtv
    10. Sctv

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

  📁 Grup: [Lokal] (57 Channel)
  ----------------------------------------
    1. Atambua tv (720p)
    2. Bandung tv (360p)
    3. Banyumas tv (720p) [not 24/7]
    4. Biznet adventure (1080p)
    5. Biznet lifestyle (1080p)
    6. Bn channel (720p)
    7. Brtv (720p)
    8. Bungo tv (480p) [not 24/7]
    9. Caruban tv (1080p)
    10. Cnbc hd
    11. Cnn 1 hd
    12. Cnn 2
    13. Daai tv
    14. Dens tv learning
    15. Dhamma tv (720p) [not 24/7]
    16. Discovery channel
    17. Efarina tv (720p)
    18. Garuda tv (1080p)
    19. Indonesiana tv
    20. Izzah tv (480p)
    21. Jawa pos tv jakarta (720p)
    22. Jogja istimewa tv (720p)
    23. Jowo
    24. Jtv (480p)
    25. Kawanua tv (720p)
    26. Kompas tv
    27. Ktv (720p)
    28. Lingkar tv
    29. Madani tv (720p)
    30. Madu tv (576p)
    31. Magna channel (1080p) [not 24/7]
    32. Metro tv
    33. Moji tv
    34. Mqtv (720p) [not 24/7]
    35. Nhk world japan
    36. Padang tv (720p) [not 24/7]
    37. Pontv (720p)
    38. R tv
    39. Radio kita tv (1080p)
    40. Rodja tv (720p)
    41. Rri net (1080p)
    42. Salira tv (720p)
    43. Smtv (720p) [not 24/7]
    44. Stara tv (720p)
    45. Stara tv bandung (1080p)
    46. Stara tv cianjur (720p)
    47. Stara tv malang (1080p)
    48. Timor tv (1080p)
    49. Tv one
    50. Tv tabalong (720p) [not 24/7]
    51. Tv9 nusantara (720p)
    52. Tvku (720p)
    53. Tvr parlemen (720p) [not 24/7]
    54. Tvri jawa barat (480p)
    55. Tvri jawa timur (720p)
    56. Tvri world
    57. Ugtv (720p)

  📁 Grup: [Lokal (auto)] (129 Channel)
  ----------------------------------------
    1. 24 Канал (1080p)
    2. ANTV HD (Alt 3 - DensTV flashcon)
    3. ATV (1080p)
    4. Abadan
    5. Ahsan TV
    6. Ajwa TV (1080p)
    7. Al Qamar TV (1080p)
    8. Al Quran Al Kareem TV (720p)
    9. Anadolu Net TV (1080p)
    10. Ashiil TV (480p)
    11. Astro Blitar TV (720p)
    12. Atomic Academy TV (480p)
    13. Atomic TV (360p)
    14. Aupur Television (1080p)
    15. Azan TV
    16. BALI TV
    17. BBC LIFESTYLE
    18. BIOSKOP INDONESIA
    19. BN Channel (ChannelFeed)
    20. Baan Baan TV 73
    21. Balapan HD (1080p)
    22. Balapan International (1080p)
    23. Balikpapan TV (720p)
    24. CBC (576p)
    25. CBC Drama (576p)
    26. CBC Sofra (576p)
    27. CNBC Indonesia (ChannelFeed)
    28. CNN INDONESIA
    29. CNN INDONESIA HD
    30. CNN Indonesia (ChannelFeed)
    31. CNN https://live.cnnindonesia.com/livecnn/smil:cnntv.smil/playlist.m3u8
    32. Canal 24 Horas (720p)
    33. Cao Bằng TV (720p)
    34. Clan Internacional Americas (1080p) [Geo-blocked]
    35. DAAI TV (Dens)
    36. DMI TV (576i)
    37. EmanTv (1080p)
    38. Ficom Channel
    39. Food Travel (V+)
    40. Garuda TV (ChannelFeed)
    41. Garuda TV (Flashcon)
    42. Garuda TV HD
    43. Hmong Star TV (720p) [Not 24/7]
    44. Hyder TV (720p)
    45. I Am Channel (576p)
    46. Indosiar
    47. Indosiar HD
    48. Inter TV (1080p)
    49. Iunior TV (1080p)
    50. JAKTV
    51. JTV Kediri (1080p) [Not 24/7]
    52. JTV Madiun
    53. JTV Malang
    54. Kids TV
    55. Kompas TV HD (Alt 3 - DensTV flashcon)
    56. Kordia TV (1080p)
    57. La 2
    58. Libya Al Ahrar TV (1080p)
    59. Love the Planet (1080p)
    60. MAGNA Channel (Flashcon)
    61. MAGNA TV (ChannelFeed)
    62. MBG TV (1080p)
    63. MDTV
    64. MDTV HD
    65. MOJI TV HD (Alt 3 - DensTV flashcon)
    66. MTV Ridiculousness
    67. MTV Ridiculousness (720p)
    68. Matrix TV Yogyakarta (720p)
    69. Metro TV
    70. MetroTV (Flashcon)
    71. Music JapanTV
    72. Outdoor Channel (1080p)
    73. PKTV (480p)
    74. Radio 51 TV
    75. Rajawali TV
    76. Riau TV (1080p) [Not 24/7]
    77. Rinjani TV
    78. SCTV (DASH/MPD)
    79. SCTV HD (Alt 3 - DensTV flashcon)
    80. Salam TV (720p)
    81. Sangaji TV (720p)
    82. SindoNews
    83. Sooriyan TV (1080p)
    84. Stara TV Bojonegoro (720p)
    85. Stara TV Jakarta (1080p)
    86. Stara TV Parahyangan (720p)
    87. Surau TV (720p)
    88. TVE Star (576p)
    89. TVE Star HD (1080p)
    90. TVRI (1080i)
    91. TVRI Aceh (720p)
    92. TVRI Bali (480p)
    93. TVRI Bangka Belitung (480p)
    94. TVRI Bengkulu (480p)
    95. TVRI Gorontalo (480p)
    96. TVRI Jakarta (576i) [Not 24/7]
    97. TVRI Jambi (720p) [Not 24/7]
    98. TVRI Jawa Tengah (720p)
    99. TVRI Kalimantan Barat (480p)
    100. TVRI Kalimantan Selatan (720p)
    101. TVRI Kalimantan Tengah (480p)
    102. TVRI Kalimantan Timur (720p)
    103. TVRI Lampung (720p)
    104. TVRI Maluku (480p)
    105. TVRI North Sulawesi (1080p)
    106. TVRI North Sumatra (1080p)
    107. TVRI Nusa Tenggara Barat (720p)
    108. TVRI Nusa Tenggara Timur (480p)
    109. TVRI Papua (480p)
    110. TVRI Riau
    111. TVRI Riau (720p) [Not 24/7]
    112. TVRI Sulawesi Barat (720p)
    113. TVRI Sulawesi Selatan (480p)
    114. TVRI Sulawesi Tengah (720p)
    115. TVRI Sulawesi Tenggara (480p)
    116. TVRI Sumatera Barat (720p)
    117. TVRI Sumatera Selatan (480p)
    118. TVRI WORLD
    119. TVRI West Papua (1080p)
    120. TVRI World
    121. TVRI Yogyakarta (720p)
    122. The Indonesia Channel (1080p)
    123. Trans7 HD
    124. TransTV HD
    125. U Channel
    126. UCL (720p)
    127. VTV HD (1080p)
    128. group-title="Lokal (auto)"CNN TV https://live.cnnindonesia.com/livecnn/smil:cnntv.smil/chunklist_w1299546647_b384000_sleng.m3u8
    129. Хузур ТВ (1080p) [Not 24/7]

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

  📁 Grup: [Indihome] (8 Channel)
  ----------------------------------------
    1. Cartoonito
    2. Global tv
    3. Hbo
    4. Hbo hits
    5. Hbo signature
    6. Mnc tv
    7. Rcti
    8. Warner tv

  📁 Grup: [Lokal] (10 Channel)
  ----------------------------------------
    1. Banten tv (720p) [not 24/7]
    2. Be tv (720p)
    3. Davika tv (480p)
    4. Dhoho tv (720p)
    5. Duta tv (360p) [not 24/7]
    6. Nusantara tv (1080p)
    7. Palembang tv (720p)
    8. Radar tasikmalaya tv (720p) [not 24/7]
    9. Rakyat bengkulu tv (720p)
    10. Tatv (720p) [not 24/7]

  📁 Grup: [Lokal (auto)] (215 Channel)
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
    40. Advocate Broadcasting Network
    41. Ajman TV (1080p)
    42. Al-Iman TV (720p)
    43. Angel TV Indonesia
    44. Angel TV Indonesia (720p)
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
    66. Banjar TV (720p) [Not 24/7]
    67. Batam TV
    68. Batam TV (480p) [Not 24/7]
    69. Berita Satu (DensTV)
    70. BeritaSatu (1080p)
    71. Bioskop Indonesia
    72. CITRA ENTERTAINMENT
    73. CNBC INDONESIA
    74. CelebritiesTV (V+)
    75. DAAI TV - LOCAL
    76. DAAI TV HD
    77. DAAI TV HD (Alt 2)
    78. DAAI TV http://210.210.155.35/qwr9ew/s/s13/01.m3u8
    79. Dens Life Style
    80. Entertainment (V+)
    81. Fajar TV (240p) [Not 24/7]
    82. Fajar TV (720p) [Not 24/7]
    83. First Lifestyle
    84. GLOBAL TV+ https://live.rctiplus.id/rctiplus/gtv_720p.m3u8
    85. GTV
    86. GTV HD
    87. Groovia Kanal
    88. Hanacaraka TV (V+)
    89. Hispan TV
    90. Hunan TV
    91. IDTV (720p) [Not 24/7]
    92. IDX (V+)
    93. INDOSIAR - LOCAL
    94. INDOSIAR BRI Super LIG
    95. INDOSIAR HD http://id1.indostreamingtv.com/live/indosiar/index.m3u8
    96. INDOSIAR http://id1.indostreamingtv.com/live/indosiar/index.m3u
    97. INEWS+ https://live.rctiplus.id/rctiplus/inews_720p.m3u8
    98. Iman TV (480p)
    99. Indonesia Movie Channel (V+)
    100. Indosiar
    101. Indosiar HD
    102. Indosiar HD (Alt 2)
    103. JAKTV - LOCAL
    104. JTV
    105. JTV (V+)
    106. JTV Madura (480p) [Not 24/7]
    107. Jak TV [Geo-blocked]
    108. Jambi TV
    109. Jogja TV (720p) [Not 24/7]
    110. KOMPAS TV
    111. KOMPASTV
    112. Kanal 10 Asia (540p)
    113. Kompas TV HD
    114. Kompas TV HD (Alt 2)
    115. KompasTV
    116. Love The Planet DE (1080p) [Geo-blocked]
    117. MAGNA Channel
    118. MAX KIDS
    119. MDTV
    120. MDTV HD
    121. MDTV HD (Alt 2)
    122. MENTARI TV HD
    123. METRO TV - LOCAL
    124. METRO TV HD http://edge.metrotvnews.com:1935/live-edge/smil:metro.smil/chunklist_w2006790992_b1492000_sleng.m3u8
    125. METROTV
    126. MNC TV
    127. MNC TV HD
    128. MNCTV
    129. MNCTV HD (720p)
    130. MOJI TV (Video)
    131. MOJI TV HD
    132. MOJI TV HD (Alt 2)
    133. MUSIC TOP
    134. Max Reels
    135. Mentari TV FHD
    136. Metro TV HD (Alt 2)
    137. MetroTV
    138. Music JapanTV
    139. NET TV
    140. NET TV HD http://id2.indostreamingtv.com/live/nettv/index.m3u8
    141. Naajiya TV (720p)
    142. PLANET FUN
    143. RCTI
    144. RCTI HD
    145. RCTI HD (720p)
    146. RCTI HD (Alt 2)
    147. RCTI SPORTS
    148. RTV
    149. RTV (V+)
    150. RTV (Vidio)
    151. RTV http://210.210.155.35/qwr9ew/s/s12/index1.m3u8
    152. Radar Lampung TV (480p)
    153. Riau TV
    154. SCTV
    155. SCTV (DASH/MPD)
    156. SCTV - LOCAL
    157. SCTV HD
    158. SCTV HD (Alt 2)
    159. SCTV HD http://id1.indostreamingtv.com/live/sctv/index.m3u8
    160. SCTV [Geo-blocked]
    161. SIN PO TV
    162. SIN PO TV HD
    163. SKY SPORT F1
    164. SMTV (720p)
    165. Sriwijaya TV (720p) [Not 24/7]
    166. TLC HD
    167. TRANS 7 TV
    168. TRANS 7 http://video.detik.com/trans7/smil:trans7.smil/chunklist_w1925750281_b384000_sleng.m3u8
    169. TRANS TV + http://id2.indostreamingtv.com/live/tv33/index.m3u8
    170. TRANS TV - LOCAL
    171. TRANS TV http://video.detik.com/transtv/smil:transtv.smil/chunklist_w1982763047_b384000_sleng.m3u8
    172. TRANS7 - LOCAL
    173. TV Mu (720p) [Not 24/7]
    174. TV ONE - LOCAL
    175. TV ONE http://id1.indostreamingtv.com/live/tv444/index.m3u8
    176. TVKU
    177. TVOne
    178. TVOne (V+)
    179. TVOne (V+) (Alt 2)
    180. TVOne HD
    181. TVOne HD (Alt 2)
    182. TVR Parlemen (720p) [Not 24/7]
    183. TVRI
    184. TVRI (480p) [Geo-blocked]
    185. TVRI + http://ott.tvri.co.id/Content/HLS/Live/Channel(TVRINasional)/Stream(02)/index.m3u8
    186. TVRI - LOCAL
    187. TVRI NASIONAL
    188. TVRI Sport HD
    189. TVRI Sport [Geo-blocked]
    190. Tegar TV Lampung (480p) [Not 24/7] [Geo-blocked]
    191. Trans TV cad
    192. Trans7 HD
    193. Trans7 HD (Alt 2)
    194. TransTV HD
    195. TransTV HD (Alt 2)
    196. Unknown 4
    197. Vision Prime (V+)
    198. dTVi
    199. group-title="Lokal (auto)"INDOSIAR http://210.210.155.35/session/9ec7c73c-099b-11ea-aff4-b82a72d63267/qwr9ew/s/s04/01.m3u8
    200. group-title="Lokal (auto)"INEWSTV https://cdn-livetv5.metube.id/hls/inewstv_240/index.m3u8
    201. group-title="Lokal (auto)"JAKTV https://cdn-livetv1.metube.id/hls/jaktv_480/536549.ts
    202. group-title="Lokal (auto)"JTV https://cdn-livetv1.metube.id/hls/jtv_240/index.m3u8
    203. group-title="Lokal (auto)"METROTV http://edge.metrotvnews.com:1935/live-edge/smil:metro.smil/chunklist_w391596422_b1492000_sleng.m3u8
    204. group-title="Lokal (auto)"MNCTV http://id6.indostreamingtv.com/live/mnctv/index.m3u8
    205. group-title="Lokal (auto)"RCTI http://id6.indostreamingtv.com/live/rcti/index.m3u8
    206. group-title="Lokal (auto)"RTV http://210.210.155.35/session/0c55f20a-0998-11ea-875c-b82a72d63267/qwr9ew/s/s12/01.m3u8
    207. group-title="Lokal (auto)"SCTV https://cdn-livetv1.metube.id/hls/sctv_480/index.m3u8
    208. group-title="Lokal (auto)"TRANS7 http://id2.indostreamingtv.com/live/trans7/index.m3u8
    209. group-title="Lokal (auto)"TVONE https://cdn-livetv1.metube.id/hls/tvone_240/index.m3u8
    210. group-title="Lokal (auto)"TVRI https://cdn-livetv1.metube.id/hls/tvri_480/index.m3u8
    211. http://oromartv.com/wp-content/uploads/2016/05/oromartv-logo.png"
    212. iNews
    213. iNews HD
    214. iNews HD (720p)
    215. tvOne [Geo-blocked]

=============================================


```
<!-- END_PROGRAM_LIST -->
