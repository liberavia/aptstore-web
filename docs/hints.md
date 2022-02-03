# Hints and research results

## Steam
Based on: https://nik-davis.github.io/posts/2019/steam-data-collection/

Needs libs:
```python
import json
import requests
```

For beeing prepared for getting request caps, the use of a specialized request method is a good idea:
```python
def get_request(url, parameters=None):
    """Return json-formatted response of a get request using optional parameters.
    
    Parameters
    ----------
    url : string
    parameters : {'parameter': 'value'}
        parameters to pass as part of get request
    
    Returns
    -------
    json_data
        json-formatted response (dict-like)
    """
    try:
        response = requests.get(url=url, params=parameters)
    except SSLError as s:
        print('SSL Error:', s)
        
        for i in range(5, 0, -1):
            print('\rWaiting... ({})'.format(i), end='')
            time.sleep(1)
        print('\rRetrying.' + ' '*10)
        
        # recusively try again
        return get_request(url, parameters)
    
    if response:
        return response.json()
    else:
        # response is none usually means too many requests. Wait and try again 
        print('No response, waiting 10 seconds...')
        time.sleep(10)
        print('Retrying.')
        return get_request(url, parameters)
```

### Fetching list of all appid's

```python
url = "https://steamspy.com/api.php"
parameters = {"request": "all"}
json_data = get_request(url, parameters=parameters)
```

Delviers a json list with entries like this:
```json
{
   "appid":945360,
   "name":"Among Us",
   "developer":"Innersloth",
   "publisher":"Innersloth",
   "score_rank":"",
   "positive":560223,
   "negative":47138,
   "userscore":0,
   "owners":"20,000,000 .. 50,000,000",
   "average_forever":2076,
   "average_2weeks":592,
   "median_forever":655,
   "median_2weeks":78,
   "price":"374",
   "initialprice":"499",
   "discount":"25",
   "ccu":10135
}
```
### Fetching Json details of a certain appid
Request like:
```python
appid = 1593500
url = "http://store.steampowered.com/api/appdetails/"
parameters = {"appids": appid}
```
Delivers a very detailed result. But currently no steam verified sadly:
```json
{
   "1593500":{
      "success":true,
      "data":{
         "type":"game",
         "name":"God of War",
         "steam_appid":1593500,
         "required_age":"18",
         "is_free":false,
         "controller_support":"full",
         "detailed_description":"<strong>Enter the Norse realm</strong><br>His vengeance against the Gods of Olympus years behind him, Kratos now lives as a man in the realm of Norse Gods and monsters. It is in this harsh, unforgiving world that he must fight to survive\u2026 and teach his son to do the same. <br><br><strong>Grasp a second chance </strong><br>Kratos is a father again. As mentor and protector to Atreus, a son determined to earn his respect, he is forced to deal with and control the rage that has long defined him while out in a very dangerous world with his son. <br><br><strong>Journey to a dark, elemental world of fearsome creatures</strong><br>From the marble and columns of ornate Olympus to the gritty forests, mountains and caves of pre-Viking Norse lore, this is a distinctly new realm with its own pantheon of creatures, monsters and gods. <br><br><strong>Engage in visceral, physical combat </strong><br>With an over the shoulder camera that brings the player closer to the action than ever before, fights in God of War\u2122 mirror the pantheon of Norse creatures Kratos will face: grand, gritty and grueling. A new main weapon and new abilities retain the defining spirit of the God of War series while presenting a vision of conflict that forges new ground in the genre.<h2 class=\"bb_tag\">PC FEATURES</h2><br><strong>High Fidelity Graphics</strong><br>Striking visuals enhanced on PC. Enjoy true 4K resolution, on supported devices, [MU1] with unlocked framerates for peak performance. Dial in your settings via a wide range of graphical presets and options including higher resolution shadows, improved screen space reflections, the addition of GTAO and SSDO, and much more.<br><br><strong>NVIDIA\u00ae DLSS and Reflex Support</strong><br>Quality meets performance. Harness the AI power of NVIDIA Deep Learning Super Sampling (DLSS) to boost frame rates and generate beautiful, sharp images on select Nvidia GPUs. Utilize NVIDIA Reflex low latency technology allowing you to react quicker and hit harder combos with the responsive gameplay you crave on GeForce GPUs.<br><br><strong>Controls Customization</strong><br>Play your way. With support for the DUALSHOCK\u00ae4 and DUALSENSE\u00ae wireless controllers, a wide range of other gamepads, and fully customizable bindings for mouse and keyboard, you have the power to fine-tune every action to match your playstyle.<br><br><strong>Ultra-wide Support</strong><br>Immerse yourself like never before. Journey through the Norse realms taking in breathtaking vistas in panoramic widescreen. With 21:9 ultra-widescreen support, God of War\u2122 presents a cinema quality experience that further expands the original seamless theatrical vision.",
         "about_the_game":"<strong>Enter the Norse realm</strong><br>His vengeance against the Gods of Olympus years behind him, Kratos now lives as a man in the realm of Norse Gods and monsters. It is in this harsh, unforgiving world that he must fight to survive\u2026 and teach his son to do the same. <br><br><strong>Grasp a second chance </strong><br>Kratos is a father again. As mentor and protector to Atreus, a son determined to earn his respect, he is forced to deal with and control the rage that has long defined him while out in a very dangerous world with his son. <br><br><strong>Journey to a dark, elemental world of fearsome creatures</strong><br>From the marble and columns of ornate Olympus to the gritty forests, mountains and caves of pre-Viking Norse lore, this is a distinctly new realm with its own pantheon of creatures, monsters and gods. <br><br><strong>Engage in visceral, physical combat </strong><br>With an over the shoulder camera that brings the player closer to the action than ever before, fights in God of War\u2122 mirror the pantheon of Norse creatures Kratos will face: grand, gritty and grueling. A new main weapon and new abilities retain the defining spirit of the God of War series while presenting a vision of conflict that forges new ground in the genre.<h2 class=\"bb_tag\">PC FEATURES</h2><br><strong>High Fidelity Graphics</strong><br>Striking visuals enhanced on PC. Enjoy true 4K resolution, on supported devices, [MU1] with unlocked framerates for peak performance. Dial in your settings via a wide range of graphical presets and options including higher resolution shadows, improved screen space reflections, the addition of GTAO and SSDO, and much more.<br><br><strong>NVIDIA\u00ae DLSS and Reflex Support</strong><br>Quality meets performance. Harness the AI power of NVIDIA Deep Learning Super Sampling (DLSS) to boost frame rates and generate beautiful, sharp images on select Nvidia GPUs. Utilize NVIDIA Reflex low latency technology allowing you to react quicker and hit harder combos with the responsive gameplay you crave on GeForce GPUs.<br><br><strong>Controls Customization</strong><br>Play your way. With support for the DUALSHOCK\u00ae4 and DUALSENSE\u00ae wireless controllers, a wide range of other gamepads, and fully customizable bindings for mouse and keyboard, you have the power to fine-tune every action to match your playstyle.<br><br><strong>Ultra-wide Support</strong><br>Immerse yourself like never before. Journey through the Norse realms taking in breathtaking vistas in panoramic widescreen. With 21:9 ultra-widescreen support, God of War\u2122 presents a cinema quality experience that further expands the original seamless theatrical vision.",
         "short_description":"His vengeance against the Gods of Olympus years behind him, Kratos now lives as a man in the realm of Norse Gods and monsters. It is in this harsh, unforgiving world that he must fight to survive\u2026 and teach his son to do the same.",
         "supported_languages":"English<strong>*</strong>, French<strong>*</strong>, Italian<strong>*</strong>, German<strong>*</strong>, Spanish - Spain<strong>*</strong>, Dutch, Japanese<strong>*</strong>, Korean, Polish<strong>*</strong>, Portuguese<strong>*</strong>, Portuguese - Brazil<strong>*</strong>, Russian<strong>*</strong>, Spanish - Latin America<strong>*</strong>, Turkish, Traditional Chinese, Czech, Hungarian, Greek<br><strong>*</strong>languages with full audio support",
         "header_image":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/header.jpg?t=1642526157",
         "website":null,
         "pc_requirements":{
            "minimum":"<strong>Minimum:</strong><br><ul class=\"bb_ul\"><li>Requires a 64-bit processor and operating system<br></li><li><strong>OS:</strong> Windows 10 64-bit<br></li><li><strong>Processor:</strong> Intel i5-2500k (4 core 3.3 GHz) or AMD Ryzen 3 1200 (4 core 3.1 GHz)<br></li><li><strong>Memory:</strong> 8 GB RAM<br></li><li><strong>Graphics:</strong> NVIDIA GTX 960 (4 GB) or AMD R9 290X (4 GB)<br></li><li><strong>DirectX:</strong> Version 11<br></li><li><strong>Storage:</strong> 70 GB available space<br></li><li><strong>Additional Notes:</strong> DirectX feature level 11_1 required</li></ul>",
            "recommended":"<strong>Recommended:</strong><br><ul class=\"bb_ul\"><li>Requires a 64-bit processor and operating system<br></li><li><strong>OS:</strong> Windows 10 64-bit<br></li><li><strong>Processor:</strong> Intel i5-6600k (4 core 3.5 GHz) or AMD Ryzen 5 2400 G (4 core 3.6 GHz)<br></li><li><strong>Memory:</strong> 8 GB RAM<br></li><li><strong>Graphics:</strong> NVIDIA GTX 1060 (6 GB) or AMD RX 570 (4 GB)<br></li><li><strong>DirectX:</strong> Version 11<br></li><li><strong>Storage:</strong> 70 GB available space<br></li><li><strong>Additional Notes:</strong> DirectX feature level 11_1 required</li></ul>"
         },
         "mac_requirements":{
            "minimum":"<strong>Minimum:</strong><br><ul class=\"bb_ul\"><li>Requires a 64-bit processor and operating system</li></ul>",
            "recommended":"<strong>Recommended:</strong><br><ul class=\"bb_ul\"><li>Requires a 64-bit processor and operating system</li></ul>"
         },
         "linux_requirements":{
            "minimum":"<strong>Minimum:</strong><br><ul class=\"bb_ul\"><li>Requires a 64-bit processor and operating system</li></ul>",
            "recommended":"<strong>Recommended:</strong><br><ul class=\"bb_ul\"><li>Requires a 64-bit processor and operating system</li></ul>"
         },
         "legal_notice":"<h2 class=\"bb_tag\">PRIVACY POLICY</h2><a href=\"https://steamcommunity.com/linkfilter/?url=https://www.playstation.com/en-us/legal/terms-of-use/op-privacy-policy/\" target=\"_blank\" rel=\"noopener\"  >https://www.playstation.com/en-us/legal/terms-of-use/op-privacy-policy/</a><h2 class=\"bb_tag\">USER AGREEMENT</h2>Software subject to license <a href=\"https://steamcommunity.com/linkfilter/?url=https://www.playstation.com/legal/op-eula/\" target=\"_blank\" rel=\"noopener\"  >https://www.playstation.com/legal/op-eula/</a><h2 class=\"bb_tag\">HEALTH WARNING</h2>WARNING: IF YOU HAVE A HISTORY OF EPILEPSY OR SEIZURES, CONSULT A DOCTOR BEFORE USE. CERTAIN PATTERNS MAY TRIGGER SEIZURES WITH NO PRIOR HISTORY. BEFORE USING AND FOR MORE DETAILS, SEE IMPORTANT HEALTH AND SAFETY WARNINGS <a href=\"https://steamcommunity.com/linkfilter/?url=https://www.playstation.com/en-us/legal/health-warning/\" target=\"_blank\" rel=\"noopener\"  >https://www.playstation.com/en-us/legal/health-warning/</a><br><br>\u00a9 2018, 2021 Sony Interactive Entertainment LLC. God of War is a registered trademark or trademark of Sony Interactive Entertainment LLC and related companies.",
         "developers":[
            "Santa Monica Studio"
         ],
         "publishers":[
            "PlayStation PC LLC"
         ],
         "price_overview":{
            "currency":"EUR",
            "initial":4999,
            "final":4999,
            "discount_percent":0,
            "initial_formatted":"",
            "final_formatted":"49,99\u20ac"
         },
         "packages":[
            564166
         ],
         "package_groups":[
            {
               "name":"default",
               "title":"Buy God of War",
               "description":"",
               "selection_text":"Select a purchase option",
               "save_text":"",
               "display_type":0,
               "is_recurring_subscription":"false",
               "subs":[
                  {
                     "packageid":564166,
                     "percent_savings_text":" ",
                     "percent_savings":0,
                     "option_text":"God of War - 49,99\u20ac",
                     "option_description":"",
                     "can_get_free_license":"0",
                     "is_free_license":false,
                     "price_in_cents_with_discount":4999
                  }
               ]
            }
         ],
         "platforms":{
            "windows":true,
            "mac":false,
            "linux":false
         },
         "metacritic":{
            "score":93,
            "url":"https://www.metacritic.com/game/pc/god-of-war?ftag=MCD-06-10aaa1f"
         },
         "categories":[
            {
               "id":2,
               "description":"Single-player"
            },
            {
               "id":22,
               "description":"Steam Achievements"
            },
            {
               "id":28,
               "description":"Full controller support"
            },
            {
               "id":23,
               "description":"Steam Cloud"
            },
            {
               "id":43,
               "description":"Remote Play on TV"
            }
         ],
         "genres":[
            {
               "id":"1",
               "description":"Action"
            },
            {
               "id":"25",
               "description":"Adventure"
            },
            {
               "id":"3",
               "description":"RPG"
            }
         ],
         "screenshots":[
            {
               "id":0,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_6eccc970b5de2943546d93d319be1b5c0618f21b.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_6eccc970b5de2943546d93d319be1b5c0618f21b.1920x1080.jpg?t=1642526157"
            },
            {
               "id":1,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_f1bff24d3967a21d303d95e11ed892e3d9113057.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_f1bff24d3967a21d303d95e11ed892e3d9113057.1920x1080.jpg?t=1642526157"
            },
            {
               "id":2,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_3670ba72c7e3e9c3c3225547ef2c1053504e62b8.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_3670ba72c7e3e9c3c3225547ef2c1053504e62b8.1920x1080.jpg?t=1642526157"
            },
            {
               "id":3,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_93a3ca63aa2cd8c675bbb6430324ee3f2d44b845.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_93a3ca63aa2cd8c675bbb6430324ee3f2d44b845.1920x1080.jpg?t=1642526157"
            },
            {
               "id":4,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_1bd99270dcbd4ff9fe9c94b0d9c8ffc50ebb42c7.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_1bd99270dcbd4ff9fe9c94b0d9c8ffc50ebb42c7.1920x1080.jpg?t=1642526157"
            },
            {
               "id":5,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_0858b868ea51d53f73bd805ba7382f027dd33dca.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_0858b868ea51d53f73bd805ba7382f027dd33dca.1920x1080.jpg?t=1642526157"
            },
            {
               "id":6,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_1351cb512d008f7e47fc50b74197f4f8eb6f3419.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_1351cb512d008f7e47fc50b74197f4f8eb6f3419.1920x1080.jpg?t=1642526157"
            },
            {
               "id":7,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_8db3de5b5d611e50945268848de2889e1ed4ba84.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_8db3de5b5d611e50945268848de2889e1ed4ba84.1920x1080.jpg?t=1642526157"
            },
            {
               "id":8,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_190a972a5bd3144d8944dcdfd7759bb1149017c0.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_190a972a5bd3144d8944dcdfd7759bb1149017c0.1920x1080.jpg?t=1642526157"
            },
            {
               "id":9,
               "path_thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_e0edce62c590bc063a90a1296184392d0a9521da.600x338.jpg?t=1642526157",
               "path_full":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_e0edce62c590bc063a90a1296184392d0a9521da.1920x1080.jpg?t=1642526157"
            }
         ],
         "movies":[
            {
               "id":256864004,
               "name":"Features Trailer",
               "thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/256864004/movie.293x165.jpg?t=1639001817",
               "webm":{
                  "480":"http://cdn.akamai.steamstatic.com/steam/apps/256864004/movie480_vp9.webm?t=1639001817",
                  "max":"http://cdn.akamai.steamstatic.com/steam/apps/256864004/movie_max_vp9.webm?t=1639001817"
               },
               "mp4":{
                  "480":"http://cdn.akamai.steamstatic.com/steam/apps/256864004/movie480.mp4?t=1639001817",
                  "max":"http://cdn.akamai.steamstatic.com/steam/apps/256864004/movie_max.mp4?t=1639001817"
               },
               "highlight":true
            },
            {
               "id":256852991,
               "name":"Announce Trailer EN",
               "thumbnail":"https://cdn.akamai.steamstatic.com/steam/apps/256852991/movie.293x165.jpg?t=1634742079",
               "webm":{
                  "480":"http://cdn.akamai.steamstatic.com/steam/apps/256852991/movie480_vp9.webm?t=1634742079",
                  "max":"http://cdn.akamai.steamstatic.com/steam/apps/256852991/movie_max_vp9.webm?t=1634742079"
               },
               "mp4":{
                  "480":"http://cdn.akamai.steamstatic.com/steam/apps/256852991/movie480.mp4?t=1634742079",
                  "max":"http://cdn.akamai.steamstatic.com/steam/apps/256852991/movie_max.mp4?t=1634742079"
               },
               "highlight":true
            }
         ],
         "recommendations":{
            "total":23491
         },
         "achievements":{
            "total":37,
            "highlighted":[
               {
                  "name":"Father and Son",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/9dd96851cbfa508d1a3a3b7b2fb837a9cc22dbbc.jpg"
               },
               {
                  "name":"The Journey Begins",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/8017a315dee83a8dc52e046c77960a1832b66074.jpg"
               },
               {
                  "name":"A New Friend",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/29a0d59563c648d6dd0d88b6375f6caf5c3a9c0a.jpg"
               },
               {
                  "name":"Feels Like Home",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/b49a5ca29ec12bd768aa35c5337c78630a08fc9b.jpg"
               },
               {
                  "name":"Dragon Slayer",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/38e3847c83c8e452741159ec935883a722dacaed.jpg"
               },
               {
                  "name":"Troubling Consequences",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/79d586813dbe614ea56437bdb411196f6549768f.jpg"
               },
               {
                  "name":"Hello, Old Friend",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/4f29997250648a1d6d5712c5a78d16adafbf1af0.jpg"
               },
               {
                  "name":"Promise Fulfilled",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/e70689b1dfc201feecfd8314edc60b0d14d92e54.jpg"
               },
               {
                  "name":"Round 2",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/bb7a3475524856d64f78805190f9bdff8bff01f6.jpg"
               },
               {
                  "name":"Past Haunts",
                  "path":"https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/1593500/74d20177e407458fc5b62be0e45c6d9a479b323c.jpg"
               }
            ]
         },
         "release_date":{
            "coming_soon":false,
            "date":"14 Jan, 2022"
         },
         "support_info":{
            "url":"https://support.sms.playstation.com/hc/",
            "email":""
         },
         "background":"https://cdn.akamai.steamstatic.com/steam/apps/1593500/page_bg_generated_v6b.jpg?t=1642526157",
         "content_descriptors":{
            "ids":[
               2,
               5
            ],
            "notes":"Gameplay consists of frequent combat scenarios with characters punching and kicking or using their axe to slash/stab/impale enemies. Some larger enemies  are opened up to intense finishing moves showing enemies being ripped apart, dismembered, or decapitated.\r\n\r\nStrong Language is used in the dialogue."
         }
      }
   }
}
```

### Fetching gold+ appids from protondb

```python
url = 'https://www.protondb.com/data/protondb/top_scoring.json'
json_data = get_request(url)
```

Will lead to a json list with about thousand entries like:

```
{
   "lastUpdated":1416967283,
   "appType":"Game",
   "appTypeSort":9,
   "name":"Dishonored",
   "userScore":95.79,
   "acronyms":[
      
   ],
   "categories":[
      "Steam Achievements",
      "Steam Cloud",
      "Full controller support",
      "Remote Play on Tablet",
      "Remote Play on TV"
   ],
   "multiplayerCategories":[
      "Single-player"
   ],
   "vrCategories":[
      
   ],
   "followers":85600,
   "description":"Dishonored is an immersive first-person action game that casts you as a supernatural assassin driven by revenge. With Dishonored flexible combat system, creatively eliminate your targets as you combine the supernatural abilities, weapons and unusual gadgets at your disposal.",
   "developer":[
      "Arkane Studios"
   ],
   "publisher":[
      "Bethesda Softworks"
   ],
   "oslist":[
      "Steam Deck Verified"
   ],
   "technologies":[
      "Engine.Unreal",
      "SDK.Bink_Video",
      "SDK.NVIDIA_PhysX"
   ],
   "name_localized":[
      
   ],
   "releaseYear":2012,
   "languages":[
      "English",
      "German",
      "French",
      "Italian",
      "Spanish - Spain"
   ],
   "languagesAudio":[
      "English",
      "German",
      "French",
      "Italian",
      "Spanish - Spain"
   ],
   "tags":[
      "Action",
      "Adventure",
      "RPG",
      "FPS",
      "Fantasy",
      "Stealth",
      "Open World",
      "Story Rich",
      "Shooter",
      "Steampunk",
      "First-Person",
      "Magic",
      "Atmospheric",
      "Singleplayer",
      "Dark",
      "Assassin",
      "Replay Value",
      "Dystopian ",
      "Multiple Endings",
      "Immersive Sim"
   ],
   "price_us":9.99,
   "objectID":"205100",
   "title":"Dishonored",
   "appId":"205100",
   "peakPlayersToday":1904,
   "contextType":"protonDbRating",
   "context":0.94
}
```

### Fetch compatibility details
ByAppId
```
https://www.protondb.com/api/v1/reports/summaries/<AppId>.json
```

Results in (For AppId 205100):
```json
{
  "bestReportedTier": "platinum",
  "confidence": "strong",
  "score": 0.94,
  "tier": "platinum",
  "total": 432,
  "trendingTier": "platinum"
}
```

### Related links to offer

SteamDb details page: 
```
https://steamdb.info/app/<AppId>/info/
```
ProtonDb details page:
```
https://www.protondb.com/app/<AppId>
```

## Debian

### Get available debian packages

Buster general:
```
http://ftp2.de.debian.org/debian/dists/buster/
```
Example for main-branch (contrib and non-free accordingly):
```
http://ftp2.de.debian.org/debian/dists/buster/main/binary-amd64/Packages.gz
```
Contains entries foreach package seperated by an empty line:
```
Package: gnome-clocks
Version: 3.30.1-2
Installed-Size: 1735
Maintainer: Debian GNOME Maintainers <pkg-gnome-maintainers@lists.alioth.debian.org>
Architecture: amd64
Depends: libc6 (>= 2.4), libcairo2 (>= 1.2.4), libgdk-pixbuf2.0-0 (>= 2.22.0), libgeoclue-2-0 (>= 2.4.0), libgeocode-glib0 (>= 1.0), libglib2.0-0 (>= 2.45.7), libgnome-desktop-3-17 (>= 3.17.92), libgsound0 (>= 1.0.1), libgtk-3-0 (>= 3.20.0), libgweather-3-15 (>= 3.13.91), dconf-gsettings-backend | gsettings-backend, geoclue-2.0
Description: Simple GNOME app with stopwatch, timer, and world clock support
Homepage: https://wiki.gnome.org/Apps/Clocks
Description-md5: bbf69cded4fb480ce6764edb86df0880
Tag: implemented-in::vala, interface::graphical, interface::x11,
 role::program, suite::gnome, uitoolkit::gtk, use::timekeeping,
 works-with::calendar, x11::application
Section: gnome
Priority: optional
Filename: pool/main/g/gnome-clocks/gnome-clocks_3.30.1-2_amd64.deb
Size: 347372
MD5sum: dba1c3c8891a56cbc07e52110ea7e0bd
SHA256: 544b4f0da256c2ba4cd7adbd4e8cd04c5ab711f5052c535b67e4e013e91b5d61
```
Example fetching package translations in german:
```
http://ftp2.de.debian.org/debian/dists/buster/main/i18n/Translation-de.bz2
```
Contains entries like:
```
Package: gnome-clocks
Description-md5: bbf69cded4fb480ce6764edb86df0880
Description-de: GNOME-Programm mit Unterstützung für Stoppuhren, Weltzeituhren und Zeitgeber
 GNOME Clocks ist eine einfache Anwendung zur Anzeige von Uhrzeit und Datum an
 mehreren verschiedenen Orten und zum Einrichten von Alarmen oder Zeitgebern.
 Eine Stoppuhr ist ebenfalls enthalten.
```

### Fetching mandatory .desktop file by package name
Install it
```
sudo apt install apt-file
```
Update it
```
sudo apt-file update
```
List desktop file of any package:
```commandline
$ apt-file list gnome-clocks | grep ".desktop"
gnome-clocks: /usr/share/applications/org.gnome.clocks.desktop
```