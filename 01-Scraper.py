from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv
from tqdm import tqdm
import os

YEAR = 2021
CSV_FN = f"Top2000-{YEAR}.csv"
DAYS = [f"https://www.nporadio2.nl/uitzendingen?date={d}-12-{YEAR}" for d in range(25,32)]

DAYS_AND_HOURS = [[25+int(i/12),0+(i*2)%24,2+(i*2)%24] for i in range(84)]


ALLE_UITZENDINGEN = []
for DAY in DAYS:
    DAG_UITZENDINGEN = []
    # Load webpage
    html = urlopen(DAY)
    soup = BeautifulSoup(html, 'html.parser')
    #Find links and filter for uitzendingen.
    links = soup.find_all('a')
    for link in links:
        ref = link.get('href')
        if ref != None:
            if '/uitzendingen' in ref:
                DAG_UITZENDINGEN.append("https://www.nporadio2.nl"+ref)
    ALLE_UITZENDINGEN += DAG_UITZENDINGEN[::-1]

CDN_URLS = []
for URL in tqdm(ALLE_UITZENDINGEN):
    html = urlopen(URL)
    soup = BeautifulSoup(html, 'html.parser')
    # Regular expression 
    # pattern    = r'http[^ ]*?\.mp3'

    pattern     = r'https://entry\.cdn\.npoaudio\.nl/handle/.*?\.mp3'
    pattern_alt = r"https://content\.omroep\.nl/.*?\.mp3"
    pattern     = pattern + "|" + pattern_alt
    link = re.search(pattern, str(soup))
    # If a link is found, append
    if link:
        CDN_URLS.append(link.group())
    else:
        print("Fail:",URL,link)

if len(CDN_URLS) == 12*7:
    print("Alle uitzendingen zijn gevonden. Je kunt nu de audio gaan downloaden.")
    lines = []
    if not os.path.isfile(CSV_FN):
        with open(CSV_FN,'w+') as f:
            for i in range(len(CDN_URLS)):
                f.write(f"{DAYS_AND_HOURS[i][0]},{DAYS_AND_HOURS[i][1]},{DAYS_AND_HOURS[i][2]},,,,,\n")
            pass
    with open(CSV_FN,'r') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            lines.append(row)
    with open(CSV_FN,'w+') as f:
        writer = csv.writer(f)
        for i in range(len(CDN_URLS)):
            lines[i][3] = CDN_URLS[i]
            writer.writerow(lines[i])