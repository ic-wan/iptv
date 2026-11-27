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

  📁 Grup: [Kids] (5 Channel)
  ----------------------------------------
    1. 3abn kids network
    2. Baby shark tv (720p)
    3. Kidsflix (1080p) [not 24/7]
    4. Moonbug kids (1080p)
    5. Pbs kids

  📁 Grup: [Lokal] (31 Channel)
  ----------------------------------------
    1. Bandung tv (360p)
    2. Banyumas tv (720p) [not 24/7]
    3. Caruban tv (1080p)
    4. Dens tv learning
    5. Duta tv (360p) [not 24/7]
    6. Efarina tv (720p)
    7. Indonesiana tv
    8. Izzah tv (480p)
    9. Jowo
    10. Kawanua tv (720p)
    11. Kompas tv
    12. Madu tv (576p)
    13. Moji tv
    14. Mqtv (720p) [not 24/7]
    15. Nhk world japan
    16. Pontv (720p)
    17. R tv
    18. Radar tasikmalaya tv (720p) [not 24/7]
    19. Rodja tv (720p)
    20. Salira tv (720p)
    21. Smtv (720p) [not 24/7]
    22. Stara tv (720p)
    23. Stara tv bandung (1080p)
    24. Stara tv cianjur (720p)
    25. Stara tv malang (1080p)
    26. Tatv (720p) [not 24/7]
    27. Tv one
    28. Tv tabalong (720p) [not 24/7]
    29. Tv9 nusantara (720p)
    30. Tvri jawa barat (480p)
    31. Tvri world

  📁 Grup: [Lokal (auto)] (253 Channel)
  ----------------------------------------
    1. !nsert
    2. 24 Horas (720p)
    3. 24 Канал (1080p)
    4. A Spor SD (1080p)
    5. ABC Australia
    6. AKTV
    7. ALJAZEERA
    8. ANTV HD
    9. ATV (Turkiye) (1080p)
    10. AXN
    11. AXN Asia Indonesia (720p)
    12. Aathavan TV (720p)
    13. Abadan
    14. Ahsan TV
    15. Ajman TV (1080p)
    16. Al Qamar TV (1080p)
    17. Al Wafa Tarim
    18. An Ninh TV HD (1080p)
    19. Anadolu Net TV (1080p)
    20. Angel TV Indonesia (720p)
    21. Ashiil TV
    22. Ashiil TV (480p)
    23. Astro Blitar TV
    24. Astro Blitar TV (720p)
    25. Atomic Academy TV (480p)
    26. Atomic TV (360p)
    27. Azan TV
    28. BBC LIFESTYLE
    29. BMS TV
    30. BN Channel (ChannelFeed)
    31. BRTV
    32. BRTV (720p)
    33. BTV
    34. BTV (Channel Feed)
    35. BTV (V+)
    36. Baan Baan TV 73
    37. Balapan HD (1080p)
    38. Balikpapan TV (720p)
    39. Bandung TV
    40. Banjar TV
    41. Banjar TV (720p) [Not 24/7]
    42. Banten TV
    43. Batam TV (480p) [Not 24/7]
    44. Berita Satu
    45. Berita Satu (DensTV)
    46. Bir TV (720p)
    47. Bungo TV
    48. CNBC
    49. CNBC Indonesia (ChannelFeed)
    50. CNN
    51. CNN Indonesia (ChannelFeed)
    52. CTV Dla Ciebie TV
    53. Cao Bằng TV (720p)
    54. Caruban TV
    55. Channel Jowo (DensTV)
    56. Clan Internacional Americas (1080p) [Geo-blocked]
    57. DAAI TV
    58. DAAI TV (Dens)
    59. DMI TV
    60. DMI TV (576i)
    61. Davika TV (480p)
    62. DensKnowledge
    63. DensLifeandStyle
    64. DensPlay
    65. Dhoho TV
    66. Dunia Lain
    67. Duta TV
    68. Eat N Go
    69. Efarina TV
    70. Elshinta TV
    71. EmanTv (1080p)
    72. Fashion TV
    73. Ficom Channel
    74. GTV
    75. Garuda TV (1080p)
    76. Garuda TV (ChannelFeed)
    77. Garuda TV (Flashcon)
    78. HBO Cinemax
    79. Hmong Star TV (720p) [Not 24/7]
    80. Hyder TV (720p)
    81. I Am Channel
    82. I Am Channel (576p)
    83. Indonesia Movie Channel (Vision+)
    84. Indonesiana TV (ChannelFeed)
    85. Indosiar (Vidio)
    86. Indosiar HD
    87. Inter TV (1080p)
    88. Iunior TV (1080p)
    89. JAKTV (Vision +)
    90. JTV (720p)
    91. JTV Kediri (1080p) [Not 24/7]
    92. JTV Madiun
    93. JTV Malang (480p)
    94. Jagantara TV
    95. Jambi TV
    96. Jawa Pos TV Jakarta (720p)
    97. Jogja TV (720p) [Not 24/7]
    98. Kordia TV (1080p)
    99. La 2
    100. Love Nature V+
    101. Love the Planet (1080p)
    102. MAGNA Channel (DensTV)
    103. MAGNA TV (ChannelFeed)
    104. MBG TV (1080p)
    105. MDTV
    106. MDTV (DensTV)
    107. MDTV (Vidio)
    108. MNC Entertainment
    109. MNCTV
    110. MOJI TV HD (Alt 3 - DensTV flashcon)
    111. MQTV
    112. MTV Ridiculousness
    113. MTV Ridiculousness (United States) LatAm (720p)
    114. Madani TV
    115. Madani TV (720p)
    116. Madu TV
    117. Magna Channel
    118. Magna Channel (1080p)
    119. Mentari TV
    120. Metro TV
    121. MetroTV (DensTV)
    122. MetroTV (Flashcon)
    123. Music TV
    124. Nickelodeon Asia Indonesia (720p)
    125. Nusantara TV
    126. Nusantara TV (ChannelFeed)
    127. OKTV
    128. Omid e Iran TV
    129. PKTV
    130. PKTV (480p)
    131. Peer TV Sudtirol (1080p)
    132. Quran TV
    133. RCTV
    134. RCTV (Indonesia) (720p) [Not 24/7]
    135. Radar Lampung TV (480p)
    136. Radio 51 TV
    137. Rajawali TV
    138. Rede Impacto Gospel TV (720p)
    139. Riau TV (1080p) [Not 24/7]
    140. Rinjani TV
    141. Rodja.tv
    142. SCTV (Vidio)
    143. SCTV HD
    144. SIN PO TV
    145. SMTV
    146. SMTV (720p)
    147. Salam TV
    148. Salam TV (720p)
    149. Salira TV
    150. Sangaji TV
    151. Sangaji TV (720p)
    152. SindoNews
    153. SindoNews (V+)
    154. SporTV BR 1
    155. SporTV BR 2
    156. SporTV BR 3
    157. Sportdigital Fussball
    158. Sriwijaya TV (720p) [Not 24/7]
    159. Stara TV
    160. Stara TV Bojonegoro (720p)
    161. Stara TV Jakarta (1080p)
    162. Stara TV Parahyangan (720p)
    163. Surau TV (720p)
    164. TLC HD
    165. TV Mu
    166. TV Mu (720p) [Not 24/7]
    167. TV9 Nusantara
    168. TVE Internacional America (576p) [Geo-blocked]
    169. TVE Star (576p)
    170. TVE Star HD (1080p)
    171. TVOne (DensTV)
    172. TVOne (V+)
    173. TVRI
    174. TVRI (1080i)
    175. TVRI Aceh
    176. TVRI Aceh (720p)
    177. TVRI Ambon
    178. TVRI Babel
    179. TVRI Bali
    180. TVRI Bali (480p)
    181. TVRI Bangka Belitung (480p)
    182. TVRI Bengkulu
    183. TVRI Bengkulu (480p)
    184. TVRI DKI
    185. TVRI Gorontalo
    186. TVRI Gorontalo (480p)
    187. TVRI Jabar
    188. TVRI Jakarta (576i) [Not 24/7]
    189. TVRI Jambi
    190. TVRI Jambi (720p) [Not 24/7]
    191. TVRI Jateng
    192. TVRI Jatim
    193. TVRI Jawa Tengah (720p)
    194. TVRI Jawa Timur (720p)
    195. TVRI Jogja
    196. TVRI Kalbar
    197. TVRI Kalimantan Barat (480p)
    198. TVRI Kalimantan Selatan (720p)
    199. TVRI Kalimantan Tengah (480p)
    200. TVRI Kalimantan Timur (720p)
    201. TVRI Kalsel
    202. TVRI Kalteng
    203. TVRI Kaltim
    204. TVRI Lampung
    205. TVRI Lampung (720p)
    206. TVRI Maluku (480p)
    207. TVRI NTB
    208. TVRI NTT
    209. TVRI Nasional
    210. TVRI North Sulawesi (1080p)
    211. TVRI North Sumatra (1080p)
    212. TVRI Nusa Tenggara Barat (720p)
    213. TVRI Nusa Tenggara Timur (480p)
    214. TVRI Papua
    215. TVRI Papua (480p)
    216. TVRI Papua barat
    217. TVRI Riau
    218. TVRI Riau (720p) [Not 24/7]
    219. TVRI Sulawesi Barat (720p)
    220. TVRI Sulawesi Selatan (480p)
    221. TVRI Sulawesi Tengah (720p)
    222. TVRI Sulawesi Tenggara (480p)
    223. TVRI Sulbar
    224. TVRI Sulsel
    225. TVRI Sulteng
    226. TVRI Sultra
    227. TVRI Sulut
    228. TVRI Sumatera Barat (720p)
    229. TVRI Sumatera Selatan (480p)
    230. TVRI Sumbar
    231. TVRI Sumsel
    232. TVRI Sumut
    233. TVRI West Papua (1080p)
    234. TVRI World
    235. TVRI Yogyakarta (720p)
    236. The Indonesia Channel
    237. The Indonesia Channel (1080p)
    238. Trans TV HD (720p)
    239. Trans7 (Transcorp)
    240. Trans7 HD
    241. TransTV (Transcorp)
    242. TransTV HD
    243. Tropical Moon Urban TV [Not 24/7]
    244. U Channel
    245. USM TV
    246. VIVO D-Sports 1 UR
    247. Warner TV
    248. Warner TV Asia (720p)
    249. YOY International
    250. iLol Funny
    251. iNews HD
    252. tVN Movies
    253. Хузур ТВ (1080p) [Not 24/7]

  📁 Grup: [Radio] (4 Channel)
  ----------------------------------------
    1. Prambors fm
    2. Rodja fm
    3. The rockin life
    4. The rockin life (indirect)

  📁 Grup: [Travels] (4 Channel)
  ----------------------------------------
    1. Dronetv (1080p)
    2. Intravel (1080p)
    3. Travel escapes (1080p)
    4. Travel tv (576p)

  📁 Grup: [Youtube Music] (1 Channel)
  ----------------------------------------
    1. YouTube Stream (DNL6Wy6IstE)

=============================================
```
<!-- END_PROGRAM_LIST -->
