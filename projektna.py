import csv
import os
import re
import sys
import requests
import orodja

mapa_strani = r'C:\Users\tanja\Documents\pr1\Projektna-naloga-analiza-podatkov'
stran = 'spletna_stran.html'


#podatki = seznam_podatkov(mapa_strani, stran)
#zapisi_csv(podatki, polja, 'youtuberji_sez.csv')



#with open('youtuberji.htm') as datoteka:
#    vsebina = datoteka.read()



vzorec_bloka = re.compile(
        r'<div style=\"width: 860px; background(.*?)<div style=\"clear: both;"',
        re.DOTALL)

vzorec_podatkov = re.compile(
    r'.*?<div style="float: left; width: 50px; color:#.*?">(?P<mesto>.*?)</div>.*?'
    r'<span style="font-weight: bold; color:#.*?;">(?P<ocena>.*?)</span>.*?'
    r'<a href=.*?>(?P<ime>.*?)</a>.*?'
    r'<sup><i style="color:#aaa; padding-left: 5px;" title="Category: (?P<kategorija>.*?)" class=".*?" aria-hidden="false"></i></sup>.*?'
    r'<div style="float: left; width: 80px;"><span style="color:#555;">(?P<objave>.*?)</span></div>.*?'
    r'<div style="float: left; width: 150px;">(?P<vpisani>.*?)</div>.*?'
    r'<div style="float: left; width: 150px;">.*?<span style="color:#555;">(?P<ogledi>.*?)</span>',
    flags = re.DOTALL)
 

url = ('https://socialblade.com/youtube/top/5000/mostsubscribed')
orodja.shrani_spletno_stran(url, 'zajeti_podatki')
vsebina = orodja.vsebina_datoteke('zajeti_podatki')
polja = ["mesto", "ocena", "ime", "kategorija", "objave", "vpisani","ogledi" ]

bloki = [] 
stevec = 0 

for ujemanje in re.findall(vzorec_bloka, vsebina):
    bloki.append(ujemanje)
    stevec += 1

slovar = []
prau = 0
for ujemanje in re.finditer(vzorec_podatkov, vsebina):
    prau +=1
    slovar.append(ujemanje.groupdict())
#.replace(",", "")
#for i in ["st", "nd", "th", "rd"]:
        #slovar["mesto"] = slovar["mesto"].replace(i, "")

def pocisti_podatke(seznam):
    for slovar in seznam:
        for i in ["st", "nd", "th", "rd"]:
            slovar["mesto"] = slovar["mesto"].replace(i,'')
        slovar["mesto"] = int(slovar["mesto"].replace(',', ''))
        slovar["ocena"] = slovar["ocena"]
        slovar["ime"] = slovar["ime"]
        slovar["kategorija"] = slovar["kategorija"]
        slovar["objave"] = int(slovar["objave"].replace(',', ''))
        slovar["vpisani"] = float(slovar["vpisani"].replace('M',''))
        slovar["ogledi"] = int(slovar["ogledi"].replace(',', ''))
    return seznam


print(prau)
print(stevec)

#orodja.zapisi_json(bloki, 'obdelani-podatki/bloki.json')
orodja.zapisi_csv(pocisti_podatke(slovar), polja, 'obdelani-podatki/podatki.csv')



