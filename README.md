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

  📁 Grup: [Lokal] (33 Channel)
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
    16. Padang tv (720p) [not 24/7]
    17. Pontv (720p)
    18. R tv
    19. Radar tasikmalaya tv (720p) [not 24/7]
    20. Radio kita tv (1080p)
    21. Rodja tv (720p)
    22. Salira tv (720p)
    23. Smtv (720p) [not 24/7]
    24. Stara tv (720p)
    25. Stara tv bandung (1080p)
    26. Stara tv cianjur (720p)
    27. Stara tv malang (1080p)
    28. Tatv (720p) [not 24/7]
    29. Tv one
    30. Tv tabalong (720p) [not 24/7]
    31. Tv9 nusantara (720p)
    32. Tvri jawa barat (480p)
    33. Tvri world

  📁 Grup: [Lokal (auto)] (267 Channel)
  ----------------------------------------
    1. !nsert
    2. 24 Horas (720p)
    3. 24 Канал (1080p)
    4. A Spor SD (1080p)
    5. ABC Australia
    6. ALJAZEERA
    7. ANTV HD
    8. AXN
    9. AXN Asia Indonesia (720p)
    10. Aathavan TV (720p)
    11. Abadan
    12. Ahsan TV
    13. Ajman TV (1080p)
    14. Al Qamar TV (1080p)
    15. Al Wafa Tarim
    16. An Ninh TV HD (1080p)
    17. Anadolu Net TV (1080p)
    18. Angel TV Indonesia (720p)
    19. Ashiil TV
    20. Ashiil TV (480p)
    21. Astro Blitar TV
    22. Astro Blitar TV (720p)
    23. Atomic Academy TV (480p)
    24. Atomic TV (360p)
    25. Azan TV
    26. BBC LIFESTYLE
    27. BMS TV
    28. BN Channel (ChannelFeed)
    29. BRTV
    30. BRTV (720p)
    31. BTV
    32. BTV (Channel Feed)
    33. BTV (V+)
    34. Baan Baan TV 73
    35. Balapan HD (1080p)
    36. Balapan International (1080p)
    37. Bali TV (Vision+)
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
    49. CNBC Indonesia
    50. CNBC Indonesia (ChannelFeed)
    51. CNN
    52. CNN Indonesia
    53. CNN Indonesia (ChannelFeed)
    54. CTV Dla Ciebie TV
    55. Cao Bằng TV (720p)
    56. Caruban TV
    57. Channel Jowo (DensTV)
    58. Clan Internacional Americas (1080p) [Geo-blocked]
    59. DAAI TV
    60. DAAI TV (Dens)
    61. DMI TV
    62. DMI TV (576i)
    63. DensKnowledge
    64. DensLifeandStyle
    65. DensPlay
    66. Dhoho TV
    67. Dunia Lain
    68. Duta TV
    69. Eat N Go
    70. Efarina TV
    71. Elshinta TV
    72. Fashion TV
    73. Ficom Channel
    74. GTV
    75. Garuda TV (1080p)
    76. Garuda TV (ChannelFeed)
    77. Garuda TV (Flashcon)
    78. HBO Cinemax
    79. Hanacaraka TV
    80. Hmong Star TV (720p) [Not 24/7]
    81. Hyder TV (720p)
    82. I Am Channel
    83. I Am Channel (576p)
    84. Indonesia Movie Channel (Vision+)
    85. Indonesiana TV (ChannelFeed)
    86. Indosiar (Vidio)
    87. Indosiar HD
    88. Inter TV (1080p)
    89. Iunior TV (1080p)
    90. JTV (720p)
    91. JTV Kediri (1080p) [Not 24/7]
    92. JTV Madiun
    93. JTV Malang (480p)
    94. Jambi TV
    95. Jawa Pos TV Jakarta (720p)
    96. Jogja TV (720p) [Not 24/7]
    97. Kordia TV (1080p)
    98. La 2
    99. Lingkar TV
    100. LingkarTV
    101. Love Nature V+
    102. Love the Planet (1080p)
    103. MAGNA Channel (DensTV)
    104. MAGNA TV (ChannelFeed)
    105. MBG TV (1080p)
    106. MDTV
    107. MDTV (DensTV)
    108. MDTV (Vidio)
    109. MNC Entertainment
    110. MNC TV (Vision+)
    111. MNCTV
    112. MOJI TV HD (Alt 3 - DensTV flashcon)
    113. MQTV
    114. MTV Ridiculousness
    115. MTV Ridiculousness (United States) LatAm (720p)
    116. Madani TV
    117. Madani TV (720p)
    118. Madu TV
    119. Magna Channel
    120. Magna Channel (1080p)
    121. Mentari TV
    122. Metro TV
    123. Metro TV HD
    124. MetroTV (DensTV)
    125. MetroTV (Flashcon)
    126. Music TV
    127. Myanmar International TV
    128. NET
    129. Nickelodeon Asia Indonesia (720p)
    130. Nusantara TV
    131. Nusantara TV (ChannelFeed)
    132. OKTV
    133. Omid e Iran TV
    134. PKTV
    135. PKTV (480p)
    136. Peer TV Sudtirol (1080p)
    137. Premiere Brazil 4
    138. Quran TV
    139. RCTI
    140. RCTV
    141. RCTV (Indonesia) (720p) [Not 24/7]
    142. Radio 51 TV
    143. Rajawali TV
    144. Rede Impacto Gospel TV (720p)
    145. Riau TV (1080p) [Not 24/7]
    146. Rinjani TV
    147. Rodja.tv
    148. SCTV (Vidio)
    149. SCTV HD
    150. SIN PO TV
    151. SMTV
    152. SMTV (720p)
    153. STV (Indonesia) (720p) [Not 24/7]
    154. Salam TV
    155. Salam TV (720p)
    156. Salira TV
    157. Sangaji TV
    158. Sangaji TV (720p)
    159. SindoNews
    160. SindoNews (V+)
    161. Slager TV
    162. SporTV BR 1
    163. SporTV BR 2
    164. SporTV BR 3
    165. Sportdigital Fussball
    166. Sriwijaya TV (720p) [Not 24/7]
    167. Stara TV
    168. Stara TV Bojonegoro (720p)
    169. Stara TV Jakarta (1080p)
    170. Stara TV Parahyangan (720p)
    171. Surau TV (720p)
    172. TLC HD
    173. TV Mu
    174. TV Mu (720p) [Not 24/7]
    175. TV9 Nusantara
    176. TVE Internacional America (576p) [Geo-blocked]
    177. TVE Star (576p)
    178. TVE Star HD (1080p)
    179. TVOne (DensTV)
    180. TVOne (V+)
    181. TVRI
    182. TVRI (1080i)
    183. TVRI (1080p)
    184. TVRI Aceh
    185. TVRI Aceh (720p)
    186. TVRI Ambon
    187. TVRI Babel
    188. TVRI Bali
    189. TVRI Bali (480p)
    190. TVRI Bangka Belitung (480p)
    191. TVRI Bengkulu
    192. TVRI Bengkulu (480p)
    193. TVRI DKI
    194. TVRI Gorontalo
    195. TVRI Gorontalo (480p)
    196. TVRI Jabar
    197. TVRI Jakarta (576i) [Not 24/7]
    198. TVRI Jambi
    199. TVRI Jambi (720p) [Not 24/7]
    200. TVRI Jateng
    201. TVRI Jatim
    202. TVRI Jawa Tengah (720p)
    203. TVRI Jawa Timur (720p)
    204. TVRI Jogja
    205. TVRI Kalbar
    206. TVRI Kalimantan Barat (480p)
    207. TVRI Kalimantan Selatan (720p)
    208. TVRI Kalimantan Tengah (480p)
    209. TVRI Kalimantan Timur (720p)
    210. TVRI Kalsel
    211. TVRI Kalteng
    212. TVRI Kaltim
    213. TVRI Lampung
    214. TVRI Lampung (720p)
    215. TVRI Maluku (480p)
    216. TVRI NTB
    217. TVRI NTT
    218. TVRI Nasional
    219. TVRI North Sulawesi (1080p)
    220. TVRI North Sumatra (1080p)
    221. TVRI Nusa Tenggara Barat (720p)
    222. TVRI Nusa Tenggara Timur (480p)
    223. TVRI Papua
    224. TVRI Papua (480p)
    225. TVRI Papua barat
    226. TVRI Riau
    227. TVRI Riau (720p) [Not 24/7]
    228. TVRI Sulawesi Barat (720p)
    229. TVRI Sulawesi Selatan (480p)
    230. TVRI Sulawesi Tengah (720p)
    231. TVRI Sulawesi Tenggara (480p)
    232. TVRI Sulbar
    233. TVRI Sulsel
    234. TVRI Sulteng
    235. TVRI Sultra
    236. TVRI Sulut
    237. TVRI Sumatera Barat (720p)
    238. TVRI Sumatera Selatan (480p)
    239. TVRI Sumbar
    240. TVRI Sumsel
    241. TVRI Sumut
    242. TVRI West Papua (1080p)
    243. TVRI World
    244. TVRI Yogyakarta (720p)
    245. The Indonesia Channel
    246. The Indonesia Channel (1080p)
    247. Timor TV
    248. Trans TV HD (720p)
    249. Trans7 (Transcorp)
    250. Trans7 HD
    251. Trans7 HD (720p)
    252. TransTV (Detik)
    253. TransTV (Transcorp)
    254. TransTV HD
    255. Tropical Moon Urban TV [Not 24/7]
    256. U Channel
    257. UGTV (720p)
    258. USM TV
    259. VIVO D-Sports 1 UR
    260. VTV (Indonesia) HD (1080p)
    261. Warner TV
    262. Warner TV Asia (720p)
    263. YOY International
    264. iLol Funny
    265. iNews HD
    266. tVN Movies
    267. Хузур ТВ (1080p) [Not 24/7]

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
