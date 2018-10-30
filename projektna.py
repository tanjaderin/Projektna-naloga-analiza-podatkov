import csv
import json
import os
import re
import sys
import requests

with open(youtuberji.html) as datoteka:
    vsebina = datoteka.read()

def bloki(datoteka):
    zecet_konec = re.compile(
        r'<div style="width: 860px; background(.*?)<div style="clear: both;"',
        re.DOTALL)
    bloki = re.findall(zacetek_konec, stran)
    return bloki

def podatki(blok):
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
