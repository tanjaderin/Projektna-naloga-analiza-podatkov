import csv
import os
import re
import sys
import requests
import orodja

mapa_strani = r'C:\Users\tanja\Documents\pr1\Projektna-naloga-analiza-podatkov'
stran = 'spletna_stran.html'


polja = ["mesto", "ocena", "kanal", "kategorija","objave", "vpisani","ogledi" ]
#podatki = seznam_podatkov(mapa_strani, stran)
#zapisi_csv(podatki, polja, 'youtuberji_sez.csv')



#with open('youtuberji.htm') as datoteka:
#    vsebina = datoteka.read()



vzorec_bloka = re.compile(
        r'<div style="width: 860px; background(.*?)<div style="clear: both;"',
        re.DOTALL)

vzorec_podatkov = re.compile(
    r'.*?<div style="float: left; width: 50px; color:#888;">(?P<mesto>.*?).*?'
    r'<span style="font-weight: bold; color:#.*?;">(?P<ocena>.*?)</span>.*?'
    #r'<a href=\".*\">(?P<ime>.*?)</a>.*?'
    r'<sup><i style="color:#aaa; padding-left: 5px;" title="Category: (?P<kategorija>.*?)" class=".*?" aria-hidden="false"></i></sup>.*?'
    r'<div style="float: left; width: 80px;"><span style="color:#555;">(?P<objave>.*?)</span></div>.*?'
    r'<div style="float: left; width: 150px;">(?P<vpisani>.*?).*?'
    r'<div style="float: left; width: 150px;">.*?<span style="color:#555;">(?P<ogledi>.*?)</span>',
    flags = re.DOTALL)
 
bloki = [] 
stevec = 0 

url = ('https://socialblade.com/youtube/top/5000/mostsubscribed')
orodja.shrani_spletno_stran(url, 'zajeti_podatki')
vsebina = orodja.vsebina_datoteke('zajeti_podatki')
polja = ["mesto", "ocena", "kategorija","objave", "vpisani","ogledi" ]

for ujemanje in re.findall(vzorec_bloka, vsebina):
    bloki.append(ujemanje)
    stevec += 1

def podatki_iz_bloka(blok):
    vzorec_podatkov = re.compile(
    r'.*?<div style="float: left; width: 50px; color:#888;">(?P<mesto>.*?).*?'
    r'<span style="font-weight: bold; color:#.*?;">(?P<ocena>.*?)</span>.*?'
    r'<a href=".*">(?P<ime>.*?)</a>.*?'
    r'<sup><i style="color:#aaa; padding-left: 5px;" title="Category: (?P<kategorija>.*?)" class=".*?" aria-hidden="false"></i></sup>.*?'
    r'<div style="float: left; width: 80px;"><span style="color:#555;">(?P<objave>.*?)</span></div>.*?'
    r'<div style="float: left; width: 150px;">(?P<vpisani>.*?).*?'
    r'<span style="color:#555;">(?P<ogledi>.*?)</span>',
    re.DOTALL)
    podatki = re.search(vzorec_podatkov, blok)
    #slovar = pocisti_podatke(podatki).groupdict()
    slovar = podatki.groupdict()
    return slovar

#slovar2 = []
#for blok in bloki:
#    slovar2.append(vzorec_podatkov.search(blok).groupdict())

slovar = []
prau = 0
for ujemanje in re.finditer(vzorec_podatkov, vsebina):
    prau +=1
    slovar.append(ujemanje.groupdict())


print(prau)

orodja.zapisi_json(bloki, 'obdelani-podatki/bloki.json')
orodja.zapisi_csv(slovar, polja, 'obdelani-podatki/podatki.csv')



