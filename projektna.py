import csv
import os
import re

mapa_strani = r'C:\Users\tanja\Desktop\projektna'
stran = 'youtuberji_2.htm'
   

def vsebina_datoteke(mapa, ime_datoteke):
    '''Return the contents of the file "directory"/"filename" as a string.'''
    path = os.path.join(mapa, ime_datoteke)
    with open(path, 'r', encoding='utf-8') as file_in:
        return file_in.read()

def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

def zapisi_csv(slovarji, imena_polj, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)



def bloki_iz_strani(dat):
    vzorec_bloka = re.compile(
        r'<div style="width: 860px; background(.*?)<div style="clear: both;"',
        re.DOTALL)
    kanali = re.findall(vzorec_bloka, dat)
    return kanali

def pocisti_podatke(podatki):
    s = podatki.groupdict()
    for i in ["st", "nd", "th", "rd"]:
        if i in s["mesto"]:
            s["mesto"] = s["mesto"].replace(i, "")
    s["mesto"] = int(s["mesto"].replace(",", ""))
    s["kanal"] = s["kanal"]
    s["objave"] = int(s["objave"].replace(",", ""))
    s["ocena"] = s["ocena"]
    s["vpisani"] = int(s["vpisani"].replace(",", ""))
    s["ogledi"] = int(s["ogledi"].replace(",", ""))
    return s

def podatki_iz_bloka(blok):
    vzorec = re.compile(
        r'<div style="float: left; width: 80px;"><span style="color:#555;">(?P<objave>.*?)</span></div>'
        r'<span style="color:#555;">(?P<vpisani>.*?)</span> </div>'
        r'<span style="color:#555;">(?P<ogledi>.*?)</span> </div>'
        r'<div style="float: left; width: 50px; color:#888;">(?P<mesto>.*?)</div>'
        r'<span style="font-weight: bold; color:#00bee7;">(?P<ocena>.*?)</span> </div>'
        r'<a href=".*">(?P<kanal>.*?)</a>',
        re.DOTALL)
    podatki = re.search(vzorec, blok)
    slovar =  pocisti_podatke(podatki).groupdict()
    return slovar


def seznam_podatkov(mapa, ime_datoteke):
    dat = vsebina_datoteke(mapa, ime_datoteke)
    kanali = []
    for blok in bloki_iz_strani(dat):
        kanali.append(podatki_iz_bloka(blok))
    return kanali




polja = ["objave", "vpisani","ogledi", "mesto", "ocena", "kanal"]
podatki = seznam_podatkov(mapa_strani, stran)
zapisi_csv(podatki, polja, 'youtuberji_sez.csv')




