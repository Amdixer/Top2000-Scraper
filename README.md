# Top2000-Scraper
Dit is een serie tools om automatisch de NPO Top2000 van NPO Radio 2 te kunnen downloaden. Vanwege auteursredenen heb ik geen links en mp3 bestanden gepost. De tool kijkt naar de actuele website van de Nederlandse Publieke Omroep en verzamelt de links daar. Werkt enkel voor 2020,2021 en 2022. Kan aangepast worden voor andere jaren, maar die hadden een iets andere indeling. (geen uitzending op de 25e voor 8.00) Op dit moment heb ik enkel de tijden voor 2022 bepaald.

Het eindresultaat is ~12.5 GB aan Top2000, opgedeeld per uur radio. In totaal is er ~30 GB schijfruimte nodig gezien de originele gedownloade bestanden nog eens 15+ GB innemen. Deze kunnen verwijderd worden nadat het Trim script klaar is.

## 01-Scraper.py
Draai dit script met Python 3. Dit zal de website van de NPO bezoeken en de links verzamelen. Verander de YEAR variabele om een ander jaar te pakken. Requirements:
- BeautifulSoup (bs4)
- urllib
- re
- csv
- tqdm
- os

## 02-Download.sh
Shell script om alle links te downloaden. Afhankelijk van het jaar, verander de gelinkte CSV file in lijn 6. Draai daarna met bash.

## 03-Trim.sh
Shell script om met gebruik van ffmpeg de bestanden te trimmen en per uur op te slaan als MP3. Dit script trekt de benodigde informatie uit de CSV file m.b.t. de tijden. Ik heb deze zelf enkel voor 2022 toegevoegd. Ik wilde dit proces in eerste instantie automatiseren door de jingle op te zoeken, echter zit er wat inconsistentie tussen de verschillende dagen m.b.t. jingles en doet Jeroen van Inkel een hele andere jingle. Dus dit was meer werk dan handmatig de tijden verzamelen.

De gegenereerde CSV file opbouw is:

DAG,BEGIN_UUR,EIND_UUR,CDN_URL,BEGIN_MUZIEK,EIND_MUZIEK,BEGIN_NIEUWS,EIND_NIEUWS

Waar de tijdstippen van de muziek en het nieuws zijn weergeven als HH:MM:SS.MS (zie 2022 als voorbeeld)
