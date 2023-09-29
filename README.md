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
Fetchs all data from "data.json".

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
  ...
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
  ...
```

### /getDataSize [get]

Returns current size of "data.json".

`/getDataSize`

```json
134
```

### Contributors 💕

<a href="https://github.com/dogukanurker"><img src="https://avatars.githubusercontent.com/u/62756402" title="ngryman" width="80" height="80"></a>

### Support 💰

<a href="https://dogukanurker.com/donate" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-red.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
