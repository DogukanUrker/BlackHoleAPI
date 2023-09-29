# [BlackHoleAPI⚫](https://dogukanurker.com/blackholesapi)

API of Black Holes.
This list of black holes (and stars considered probable candidates) is organized by mass (including black holes of undetermined mass); some items in this API are galaxies or star clusters that are believed to be organized around a black hole. [Total 97 Item] [134KB]


### [Demo Video 📺](https://youtu.be/9TLdmE_5Axw)


## Requirements 📦

- FastAPI
- Uvicorn

## Installation ⬇️

download source code from Github 💾
`git clone https://github.com/DogukanUrker/BlackHolesAPI.git`

go to directory 📁
`cd BlackHolesAPI`

install requirements.txt 🔽
`pip install -r requirements.txt`

it's ready to run 🎉
`python main.py`

## Requests 📚

### /data [get]
Fetchs all data from data.json

### /data/{id} [get]

Returns specific black hole with ID.

`/data/{2}`
```json
[
  {
    "id": 2,
    "name": [
      "TON 618",
      "Tonantzintla 618",
      "FBQS J122824.9+312837",
      "B2 1225+31",
      "QSO 1228+3128",
      "7C 1225+3145",
      "CSO 140",
      "2E 2728",
      "Gaia DR1 4015522739308729728"
    ],
    "list": "Supermassive Black Holes",
    "kind": "Quasar",
    "image": "https://upload.wikimedia.org/wikipedia/commons/c/cc/TON_618_SDSS9_version_2.jpg",
    "type": "Quasar",
    "age": {
      "text": "10.8 billion",
      "number": 10800000000
    },
    "constellation": "Canes Venatici",
    "rightAscension": "12h 28m 24.9s",
    "declination": "+31Â° 28' 38â€³",
    "coordinates": "12h 28m 24.97s, +31Â° 28' 37.7â€³",
    "map": "https://aladin.cds.unistra.fr/AladinLite/?target=12%2028%2024.966%2B31%2028%2037.63&fov=0.03&survey=CDS%2FP%2FDSS2%2Fcolor",
    "redshift": 2.219,
    "apparentMagnitude": 15.9,
    "absoluteMagnitude": -30.9,
    "discovery": {
      "year": 1957,
      "location": "Bologna in Italy",
      "discoverer": "Maarten Schmidt"
    },
    "solarmass": {
      "text": "66 billion",
      "number": 66000000000
    },
    "radius": "1949 * 10^14 meters",
    "luminosity": "4 * 10^40 watts",
    "temperature": {
      "kelvin": null,
      "celsius": null,
      "fahrenheit": null
    },
    "distance": {
      "m": 1.7218529460097055e+26,
      "km": 1.7218529460097057e+23,
      "ly": 18200000000,
      "gpc": 5.5801446100652985,
      "gly": 18.21246575342376
    },
    "wikipedia": "https://en.wikipedia.org/wiki/TON_618"
  }
]
```


### /random [get]

Returns random black hole from data.json

`/random`

```json
[
  {
    "id": 71,
    "name": [
      "Cygnus X-1",
      "Cyg X-1",
      "AG (or AGK2)+35 1910",
      "BD+34 3815",
      "HD 226868",
      "HDE 226868",
      "HIP 98298",
      "SAO 69181",
      "V1357 Cyg"
    ],
    "list": "Stellar Black Holes",
    "kind": "Microquasar",
    "image": "https://upload.wikimedia.org/wikipedia/commons/2/21/Chandra_image_of_Cygnus_X-1.jpg",
    "type": "Microquasar",
    "age": {
      "text": "5 million",
      "number": 5000000
    },
    "constellation": "Cygnus",
    "rightAscension": "19h 58m 21.67574s",
    "declination": "+35Â° 12' 05.7845â€³",
    "coordinates": "19h 58m 21.6756s, +35Â° 12' 05.775â€³",
    "map": "https://aladin.cds.unistra.fr/AladinLite/?target=19%2058%2021.676%2B35%2012%2005.78&fov=0.06&survey=CDS%2FP%2FDSS2%2Fcolor",
    "redshift": null,
    "apparentMagnitude": 8.95,
    "absoluteMagnitude": -6.5,
    "discovery": {
      "year": 1964,
      "location": "Royal Greenwich Observatory",
      "discoverer": "Louise Webster and Paul Murdin"
    },
    "solarmass": {
      "text": "21.2",
      "number": 21.2
    },
    "radius": 14609700,
    "luminosity": "3-4*105 Lâ˜‰",
    "temperature": {
      "kelvin": 31000,
      "celsius": 30726.85,
      "fahrenheit": 55340.33
    },
    "distance": {
      "m": 57425407418350120000,
      "km": 57425407418350120,
      "ly": 6070,
      "gpc": 0.0000018610702078624374,
      "gly": 0.000006074157534246276
    },
    "wikipedia": "https://en.wikipedia.org/wiki/Cygnus_X-1"
  }
]
```

### /randomValue/{value} [get]

Returns specific value from random black hole.


`/randomValue/name`
```json
[
  "HE0450-2958",
  "LEDA 75249",
  "QSO B0450-2958",
  "2MASSI J0452300-295335",
  "6dFGS gJ045230.1-295335",
  "2MASX J04523006-2953353",
  "NVSS J045230-295336",
  "IRAS F04505-2958",
  "QSO B0450-299",
  "IRAS 04505-2958",
  "RBS 597",
  "1RXS J045230.4-295329"
]
```

### /getValueByID/{value}/{id} [get]

Returns specific data from specific black hole.

`/getValueByID/name/2`
```json
[
  "TON 618",
  "Tonantzintla 618",
  "FBQS J122824.9+312837",
  "B2 1225+31",
  "QSO 1228+3128",
  "7C 1225+3145",
  "CSO 140",
  "2E 2728",
  "Gaia DR1 4015522739308729728"
]
```


### /getRandomDatas/{dataCount} [get]

Returns any number of random black holes

`/getRandomDatas/2`
```json
[
  {
    "id": 54,
    "name": [
      "NGC 7314",
      "Arp 14",
      "PGC 69253"
    ],
    "list": "Supermassive Black Holes",
    "kind": "Galaxy",
    "image": "https://upload.wikimedia.org/wikipedia/commons/f/f8/NGC7314-HST-R814GB450.jpg",
    "type": "SAB(rs)bc",
    "age": {
      "text": null,
      "number": null
    },
    "constellation": null,
    "rightAscension": null,
    "declination": null,
    "coordinates": null,
    "map": null,
    "redshift": null,
    "apparentMagnitude": null,
    "absoluteMagnitude": null,
    "discovery": {
      "year": 1834,
      "location": null,
      "discoverer": "John Herschel"
    },
    "solarmass": {
      "text": "870 thousand",
      "number": 870000
    },
    "radius": "5 arcsec",
    "luminosity": null,
    "temperature": {
      "kelvin": null,
      "celsius": null,
      "fahrenheit": null
    },
    "distance": {
      "m": 5.1620232056964635e+23,
      "km": 516202320569646400000,
      "ly": 54562628.33675581,
      "gpc": 0.016728975627711213,
      "gly": 0.05459999999999748
    },
    "wikipedia": "https://en.wikipedia.org/wiki/NGC_7314"
  },
  {
    "id": 7,
    "name": [
      "APM 08279+5255",
      "IRAS F08279+5255",
      "QSO B0827+5255",
      "QSO J0831+5245"
    ],
    "list": "Supermassive Black Holes",
    "kind": "Quasar",
    "image": "https://upload.wikimedia.org/wikipedia/commons/6/69/Quasar_in_Water_Vapor_concept.jpg",
    "type": "broad absorption line (BAL) quasar, hyperluminous infrared galaxy",
    "age": {
      "text": "2 - 3Gyr",
      "number": null
    },
    "constellation": "Lynx",
    "rightAscension": "08h 31m 41.70s",
    "declination": "52Â° 45' 16.8â€³",
    "coordinates": "08h 31m 41.70s, +52Â° 45' 16.8â€³",
    "map": "https://aladin.cds.unistra.fr/AladinLite/?target=08%2031%2041.700%2B52%2045%2016.80&fov=0.05&survey=CDS%2FP%2FDSS2%2Fcolor",
    "redshift": 3.911,
    "apparentMagnitude": 15.2,
    "absoluteMagnitude": 15,
    "discovery": {
      "year": 1998,
      "location": null,
      "discoverer": "Totten, Edward J"
    },
    "solarmass": {
      "text": "23 billion",
      "number": 23000000000
    },
    "radius": 0.468,
    "luminosity": "5*10 15 L solar",
    "temperature": {
      "kelvin": 112.5,
      "celsius": -160.65,
      "fahrenheit": -257.17
    },
    "distance": {
      "m": 2.221688159999995e+26,
      "km": 2.22168828385523e+23,
      "ly": 23483262380.626083,
      "gpc": 7.2,
      "gly": 23.6
    },
    "wikipedia": "https://en.wikipedia.org/wiki/APM_08279%2B5255"
  }
]
```
### /getAll/{value} [get]

Returns specific value from all black holes.

`/getAll/image`

```json
[
  "https://www.swift.psu.edu/monitoring/data_new/1ES2344+514/pc_image.png",
  "https://upload.wikimedia.org/wikipedia/commons/c/cc/TON_618_SDSS9_version_2.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/9/9d/3C-371-jet-O5GV07NEQ.gif",
  "https://i.ibb.co/KsVSk2Z/Aladin-Lite.png",
  "https://th.bing.com/th/id/OIP.3wqsIAWEp3SVVuspUWUkNwHaHH?pid=ImgDet&rs=1",
  "https://upload.wikimedia.org/wikipedia/commons/0/0b/Black-hole-feeding-accreting-esa-nasa.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/6/69/Quasar_in_Water_Vapor_concept.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/9/9a/Arp_220_-_JWST%2C_HST.png",
  "https://upload.wikimedia.org/wikipedia/commons/d/d2/ESO_Centaurus_A_LABOCA.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/a/a4/Ngc1316_hst.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/0/08/Quasar_HE0450-2958.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/d/df/IC_1459_U2BM0104T.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/c/c2/M31_09-01-2011_%28cropped%29.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/c/cc/M32_Francione_inverted.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/2/2a/Messier_60_-_Hubble_%282013-9-24%29.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/d/db/Messier51_sRGB.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/d/d9/Messier_77_spiral_galaxy_by_HST.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/6/63/Messier_81_HST.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/5/59/A_fascinating_core.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/4/4f/Black_hole_-_Messier_87_crop_max_res.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/9/98/Sombrero_Galaxy_in_infrared_%28Ssc2005-11a3%29.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/e/ec/Messier105_-_HST_-_Potw1901a.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/2/2d/Messier_106_visible_and_infrared_composite.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/1/1f/SDSS_Mrk_421.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/1/1e/SDSS_Mrk_501.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/f/f0/NGC_821_PanS.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/4/41/NGC1023_JeffJohnson.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/5/59/NGC1097_-_ESO_-_eso0438d.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/e/e9/SDSS_NGC_1271.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/e/e2/NGC_1277_viewed_by_Hubble.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/e/e2/NGC1332-hst-R814GB555.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/6/62/Potw1422a.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/3/39/NGC_2787.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/e/e8/NGC_3079.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/3/3e/NGC_3115.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/a/ab/NGC_3377_Hubble_WikiSky.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/e/ef/Settling_into_old_age_NGC_3384.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/4/4e/NGC3998_-_SDSS_DR14.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/e/eb/NGC4151_Galaxy_from_the_Mount_Lemmon_SkyCenter_Schulman_Telescope_courtesy_Adam_Block.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/8/86/NGC_4261_X-ray.png",
  "https://upload.wikimedia.org/wikipedia/commons/7/76/NGC4438-NGC4435-eso1131a.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/3/32/NGC_4459_wikisky.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/8/8b/SDSS_NGC_4473.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/0/07/Messier_87_Hubble_WikiSky.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/b/b8/SDSS_NGC_4564.jpeg",
  "https://upload.wikimedia.org/wikipedia/commons/b/b0/M58s_%28visible%29.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/3/3c/SDSS_NGC_4596.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/0/08/NGC_4697_HST_10003_R850_B475.png",
  "https://upload.wikimedia.org/wikipedia/commons/4/43/Caldwell_35.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Spiral_Galaxy_NGC_4945.jpg/520px-Spiral_Galaxy_NGC_4945.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/A_galaxy_with_a_bright_heart_NGC_5033.tif/lossy-page1-682px-A_galaxy_with_a_bright_heart_NGC_5033.tif.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/a/a6/NGC_6251_R814B547.png",
  "https://upload.wikimedia.org/wikipedia/commons/8/84/Ngc7052a.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/f/f8/NGC7314-HST-R814GB450.jpg",
  "https://alchetron.com/cdn/pks-0521-365-ae425900-3cce-4122-bfe1-61574370b2a-resize-750.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/d/d2/Q0906p6930Location.png",
  "https://upload.wikimedia.org/wikipedia/commons/5/53/RX_J1131.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/EHT_Saggitarius_A_black_hole.tif/lossy-page1-600px-EHT_Saggitarius_A_black_hole.tif.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/e/e5/Phoenix_Cluster_center%2C_artist%27s_depiction.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/M82_HST_ACS_2006-14-a-large_web.jpg/600px-M82_HST_ACS_2006-14-a-large_web.jpg",
  "https://jumk.de/astronomie/img/irs-13e.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/7/75/ESO_243-49_%28HST%29.jpg",
  "http://blackholes.stardate.org/images/sig06-010_Med.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/2/2a/M15_Globular_Cluster_from_the_Mount_Lemmon_SkyCenter_Schulman_Telescope_courtesy_Adam_Block.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/1/1b/Not_So_Dead_After_All_%2848763200193%29.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/NGC_253_Galaxy.jpg/560px-NGC_253_Galaxy.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/VST_snaps_a_very_detailed_view_of_the_Triangulum_Galaxy.jpg/1000px-VST_snaps_a_very_detailed_view_of_the_Triangulum_Galaxy.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/c/cf/Ss433_art_big.gif",
  "http://maxi.riken.jp/star_data/J1547-476/J1547-476_g_img_1m.gif",
  "https://upload.wikimedia.org/wikipedia/commons/d/d2/V616mon_sdss_ugiz_1_besk.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/2/21/Chandra_image_of_Cygnus_X-1.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/9/90/Cygnus_X3.jpg",
  "https://th.bing.com/th/id/R.bda2f17be3da67d824561b02bc49f388?rik=xwKZNOBdj1wkQA&riu=http%3a%2f%2fblackholes.stardate.org%2fimages%2fGRO_J0422_32_artist-impression.jpg&ehk=N8IO4Sz%2fKLEV7V1Ag4MeqeSnZtNCfXSyPiAGPfqjEZ8%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/GRO_J1655-40.jpg/300px-GRO_J1655-40.jpg",
  "https://dic.academic.ru/pictures/wiki/files/51/300px-Black_hole.jpg",
  "https://chandra.harvard.edu/photo/2009/g1915/g1915_xray.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/3/3d/QZVulLightCurve.png",
  "https://upload.wikimedia.org/wikipedia/commons/d/dc/Flaring_Black_Hole.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/6/60/IGR_J17091-3624.jpg",
  "https://images.firstpost.com/optimize/Lg2e6g4KH-RJVDE8KN6hJVUFnsk=/images.firstpost.com/wp-content/uploads/2019/11/LB-1-Black-Hole-1.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/b/b5/M33_X-7.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/b/b0/Rogue_black_hole_OGLE-2011-BLG-0462.gif",
  "https://upload.wikimedia.org/wikipedia/commons/b/b2/N3147v.gif",
  "https://upload.wikimedia.org/wikipedia/commons/d/dd/W50_medium.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/2/2e/V404Cyg_XRT_halo_fullsize.jpg",
  "https://i.ibb.co/VJPsNPX/aladin-cds-unistra-fr-Aladin-Lite-5.png",
  "https://upload.wikimedia.org/wikipedia/commons/6/69/Xtej1118_xray.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/c/ce/V381NorLightCurve.png",
  "https://upload.wikimedia.org/wikipedia/commons/9/99/XTE_J1650-500.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/8/8d/V4641SgrLightCurve.png",
  "https://upload.wikimedia.org/wikipedia/commons/6/6b/Artist%27s_impression_of_the_closest_black_hole_to_Earth_and_its_Sun-like_companion_star.jpg",
  "https://th.bing.com/th/id/R.644459a22c91fc1b31aee8df1e8aebe9?rik=DPzxHNPq6EmWgQ&riu=http%3a%2f%2fscimonitors.com%2fwp-content%2fuploads%2f2021%2f07%2f5-blackhole.jpg&ehk=gX6Jnx2ufRojIMABbYOZ6kgHn8T5dwKO1FrHL8UJpzo%3d&risl=&pid=ImgRaw&r=0",
  "https://i.ytimg.com/vi/v_Mg0nBqxCY/maxresdefault.jpg",
  "https://miro.medium.com/v2/resize:fit:640/format:webp/1*H9Lxg7cdwk3OHS0Clj5APg.png",
  "https://news.pku.edu.cn/xwzh/attachement/jpg/site2/20140802/a41731fa3e5e154747d601.jpg",
  "https://th.bing.com/th/id/OIP.Ahdosozq6IlkTrsxcxcf6gHaHG?pid=ImgDet&rs=1",
  "https://th.bing.com/th/id/OIP.j-27rNmfGc6OCLmKdLd4-QHaEK?pid=ImgDet&rs=1",
  "https://th.bing.com/th/id/R.3d71676772bfb2f433c0b322c3adfe79?rik=YxYHl3H7%2faXv4g&riu=http%3a%2f%2fzap.aeiou.pt%2fwp-content%2fuploads%2f2015%2f04%2f460c1cb621ab420585018b5abac3edf01-783x450.jpg&ehk=TgjBxrPoE8sxaLUXpDVootr%2bXS1rwQsDKvHj4TCmyMk%3d&risl=&pid=ImgRaw&r=0"
]
```
### /getAllWithID/{value} [get]

Returns specific value with IDs from all black holes.

`/getAll/image`

```json
[
  [
    1,
    "https://en.wikipedia.org/wiki/1ES_2344%2B514"
  ],
  [
    2,
    "https://en.wikipedia.org/wiki/TON_618"
  ],
  [
    3,
    "https://en.wikipedia.org/wiki/3C_371#:~:text=3C%20371%20is%20a%20BL%20Lac%20object%20located,among%20the%20nearest%20and%20brightest%20BL%20Lacs.%20"
  ],
  [
    4,
    "https://en.wikipedia.org/wiki/4C_%2B37.11#:~:text=4C%20%2B37.11%20or%20Galaxy%200402%2B379%20is%20a%20radio,parsecs%2C%20with%20an%20orbital%20period%20of%2030%2C000%20years."
  ],
  [
    5,
    "https://en.wikipedia.org/wiki/AP_Librae"
  ],
  [
    6,
    "https://en.wikipedia.org/wiki/S5_0014%2B81"
  ],
  [
    7,
    "https://en.wikipedia.org/wiki/APM_08279%2B5255"
  ],
  [
    8,
    "https://en.wikipedia.org/wiki/Arp_220"
  ],
  [
    9,
    "https://en.wikipedia.org/wiki/Centaurus_A"
  ],
  [
    10,
    "https://en.wikipedia.org/wiki/NGC_1316"
  ],
  [
    11,
    "https://en.wikipedia.org/wiki/HE0450-2958"
  ],
  [
    12,
    "https://en.wikipedia.org/wiki/IC_1459"
  ],
  [
    13,
    "https://en.wikipedia.org/wiki/Andromeda_Galaxy"
  ],
  [
    14,
    "https://en.wikipedia.org/wiki/Messier_32"
  ],
  [
    15,
    "https://en.wikipedia.org/wiki/Messier_60"
  ],
  [
    16,
    "https://en.wikipedia.org/wiki/Whirlpool_Galaxy"
  ],
  [
    17,
    "https://en.wikipedia.org/wiki/Messier_77"
  ],
  [
    18,
    "https://en.wikipedia.org/wiki/Messier_81"
  ],
  [
    19,
    "https://en.wikipedia.org/wiki/Messier_84"
  ],
  [
    20,
    "https://en.wikipedia.org/wiki/Messier_87#Supermassive_black_hole_M87*"
  ],
  [
    21,
    "https://en.wikipedia.org/wiki/Sombrero_Galaxy#Central_supermassive_black_hole"
  ],
  [
    22,
    "https://en.wikipedia.org/wiki/Messier_105"
  ],
  [
    23,
    "https://en.wikipedia.org/wiki/Messier_106"
  ],
  [
    24,
    "https://en.wikipedia.org/wiki/Markarian_421"
  ],
  [
    25,
    "https://en.wikipedia.org/wiki/Markarian_501"
  ],
  [
    26,
    "https://en.wikipedia.org/wiki/NGC_821"
  ],
  [
    27,
    "https://en.wikipedia.org/wiki/NGC_1023"
  ],
  [
    28,
    "https://en.wikipedia.org/wiki/NGC_1097"
  ],
  [
    29,
    "https://en.wikipedia.org/wiki/NGC_1271"
  ],
  [
    30,
    "https://en.wikipedia.org/wiki/NGC_1277"
  ],
  [
    31,
    "https://en.wikipedia.org/wiki/NGC_1332"
  ],
  [
    32,
    "https://en.wikipedia.org/wiki/NGC_1566"
  ],
  [
    33,
    "https://en.wikipedia.org/wiki/NGC_2787"
  ],
  [
    34,
    "https://en.wikipedia.org/wiki/NGC_3079"
  ],
  [
    35,
    "https://en.wikipedia.org/wiki/NGC_3115#Black_hole"
  ],
  [
    36,
    "https://en.wikipedia.org/wiki/NGC_3377"
  ],
  [
    37,
    "https://en.wikipedia.org/wiki/NGC_3384"
  ],
  [
    38,
    "https://en.wikipedia.org/wiki/NGC_3998"
  ],
  [
    39,
    "https://en.wikipedia.org/wiki/NGC_4151"
  ],
  [
    40,
    "https://en.wikipedia.org/wiki/NGC_4261"
  ],
  [
    41,
    "https://en.wikipedia.org/wiki/Eyes_Galaxies"
  ],
  [
    42,
    "https://en.wikipedia.org/wiki/NGC_4459#Super_massive_black_hole"
  ],
  [
    43,
    "https://en.wikipedia.org/wiki/NGC_4473#Supermassive_black_hole"
  ],
  [
    44,
    "https://en.wikipedia.org/wiki/Messier_87#Supermassive_black_hole_M87*"
  ],
  [
    45,
    "https://en.wikipedia.org/wiki/NGC_4564"
  ],
  [
    46,
    "https://en.wikipedia.org/wiki/Messier_58"
  ],
  [
    47,
    "https://en.wikipedia.org/wiki/NGC_4596#Supermassive_black_hole"
  ],
  [
    48,
    "https://en.wikipedia.org/wiki/NGC_4697"
  ],
  [
    49,
    "https://en.wikipedia.org/wiki/NGC_4889#Supermassive_black_hole"
  ],
  [
    50,
    "https://en.wikipedia.org/wiki/NGC_4945"
  ],
  [
    51,
    "https://en.wikipedia.org/wiki/NGC_5033"
  ],
  [
    52,
    "https://en.wikipedia.org/wiki/NGC_6251"
  ],
  [
    53,
    "https://en.wikipedia.org/wiki/NGC_7052"
  ],
  [
    54,
    "https://en.wikipedia.org/wiki/NGC_7314"
  ],
  [
    55,
    "https://en.wikipedia.org/wiki/PKS_0521-365"
  ],
  [
    56,
    "https://en.wikipedia.org/wiki/Q0906%2B6930"
  ],
  [
    57,
    "https://en.wikipedia.org/wiki/RX_J1131-1231"
  ],
  [
    58,
    "https://en.wikipedia.org/wiki/Sagittarius_A*"
  ],
  [
    59,
    "https://en.wikipedia.org/wiki/Phoenix_Cluster#Supermassive_black_hole"
  ],
  [
    60,
    "https://en.wikipedia.org/wiki/Messier_82"
  ],
  [
    61,
    "https://en.wikipedia.org/wiki/GCIRS_13E"
  ],
  [
    62,
    "https://en.wikipedia.org/wiki/HLX-1"
  ],
  [
    63,
    "https://en.wikipedia.org/wiki/M82_X-1"
  ],
  [
    64,
    "https://en.wikipedia.org/wiki/Messier_15"
  ],
  [
    65,
    "https://en.wikipedia.org/wiki/Messier_110"
  ],
  [
    66,
    "https://en.wikipedia.org/wiki/Sculptor_Galaxy#Central_black_hole"
  ],
  [
    67,
    "https://en.wikipedia.org/wiki/Triangulum_Galaxy"
  ],
  [
    68,
    "https://en.wikipedia.org/wiki/Great_Annihilator"
  ],
  [
    69,
    "https://en.wikipedia.org/wiki/4U_1543-475"
  ],
  [
    70,
    "https://en.wikipedia.org/wiki/A0620-00"
  ],
  [
    71,
    "https://en.wikipedia.org/wiki/Cygnus_X-1"
  ],
  [
    72,
    "https://en.wikipedia.org/wiki/Cygnus_X-3"
  ],
  [
    73,
    "https://en.wikipedia.org/wiki/GRO_J0422%2B32"
  ],
  [
    74,
    "https://en.wikipedia.org/wiki/GRO_J1655%E2%88%9240"
  ],
  [
    75,
    "https://en.wikipedia.org/wiki/GRS_1124-683"
  ],
  [
    76,
    "https://en.wikipedia.org/wiki/GRS_1915%2B105"
  ],
  [
    77,
    "https://en.wikipedia.org/wiki/GS_2000%2B25"
  ],
  [
    78,
    "https://en.wikipedia.org/wiki/GX_339-4"
  ],
  [
    79,
    "https://en.wikipedia.org/wiki/IGR_J17091-3624"
  ],
  [
    80,
    "https://en.wikipedia.org/wiki/LB-1"
  ],
  [
    81,
    "https://en.wikipedia.org/wiki/M33_X-7"
  ],
  [
    82,
    "https://en.wikipedia.org/wiki/OGLE-2011-BLG-0462"
  ],
  [
    83,
    "https://en.wikipedia.org/wiki/SN_1997D"
  ],
  [
    84,
    "https://en.wikipedia.org/wiki/SS_433"
  ],
  [
    85,
    "https://en.wikipedia.org/wiki/V404_Cygni"
  ],
  [
    86,
    "https://en.wikipedia.org/wiki/V_Puppis"
  ],
  [
    87,
    "https://en.wikipedia.org/wiki/XTE_J1118%2B480"
  ],
  [
    88,
    "https://en.wikipedia.org/wiki/XTE_J1550%E2%80%93564"
  ],
  [
    89,
    "https://en.wikipedia.org/wiki/XTE_J1650%E2%88%92500"
  ],
  [
    90,
    "https://en.wikipedia.org/wiki/V4641_Sagittarii"
  ],
  [
    91,
    "https://en.wikipedia.org/wiki/EGSD2_J142033.66_525917.5"
  ],
  [
    91,
    "https://en.wikipedia.org/wiki/EGSD2_J142033.66_525917.5"
  ],
  [
    92,
    "https://en.wikipedia.org/wiki/OJ_287"
  ],
  [
    93,
    "https://en.wikipedia.org/wiki/PKS_1302-102"
  ],
  [
    94,
    "https://en.wikipedia.org/wiki/SDSS_J120136.02%2B300305.5"
  ],
  [
    95,
    "https://en.wikipedia.org/wiki/SDSS_J150243.09%2B111557.3"
  ],
  [
    96,
    "https://en.wikipedia.org/wiki/GOODS_J123652.77%2B621354.7"
  ],
  [
    97,
    "https://en.wikipedia.org/wiki/2MASX_J10270057%2B1749001"
  ]
]
```

### Contributors 💕

<a href="https://github.com/dogukanurker"><img src="https://avatars.githubusercontent.com/u/62756402" title="ngryman" width="80" height="80"></a>

### Support 💰

<a href="https://dogukanurker.com/donate" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-red.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
