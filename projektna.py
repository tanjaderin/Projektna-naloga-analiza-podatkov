import csv
import json
import os
import re
import sys

      

def vsebina_datoteke(mapa, ime_datoteke):
    path = os.path.join(mapa, ime_datoteke)
    with open(path, 'r', encoding='utf-8') as file_in:
        return file_in.read()


def zapisi_csv(seznam, imena_polj, stran, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in seznam:
            writer.writerow(slovar)
    return None

def shrani_vsebino(directory, ime_datoteke):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ime_datoteke)
    with open(path, 'w', encoding='utf-8') as dat:
        dat.write(vsebina_datoteke())
    return None

mapa_strani = r'C:\Users\tanja\Desktop\projektna'
stran = 'youtuberji.htm'
  



def bloki_iz_strani(dat):
    zecetek_konec = re.compile(
        r'<div style="width: 860px; background(.*?)<div style="clear: both;"',
        re.DOTALL)
    kanali = re.findall(zacetek_konec, dat)
    return kanali

def podatki_iz_bloka(blok):
    vzorec = re.compile(
        r'<div style="float: left; width: 80px;"><span style="color:#555;">(?P<objave>\d+)</span></div>'
        r'<span style="color:#555;">(?P<vpisani>\d+)</span> </div>'
        r'<span style="color:#555;">(?P<ogledi>\d+)</span> </div>'
        r'<div style="float: left; width: 50px; color:#888;">(?P<mesto>\d)</div>'
        r'<span style="font-weight: bold; color:#00bee7;">(?P<ocena>[AB]+[+-]*)</span> </div>'
        r'<a href=".*">(?P<kanal>.*?)</a>',
        re.DOTALL)
    podatki = re.search(vzorec, blok)
    slovar = podatki.groupdict()
    return slovar

def seznam_podatkov(mapa, ime_datoteke):
    dat = vsebina_datoteke(mapa, ime_datoteke)
    kanali = []
    for blok in bloki_iz_strani(dat):
        kanali.append(podatki_iz_bloka(blok))
    return kanali


polja = ["objave", "vpisani","ogledi", "mesto", "ocena", "kanal"]
podatki = seznam_podatkov(mapa_strani, stran)
zapisi_csv(podatki[0].keys(), polja, stran,'youtuberji.csv')
