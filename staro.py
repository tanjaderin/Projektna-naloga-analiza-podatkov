def bloki_iz_strani(ime_datoteke):
    vzorec_bloka = re.compile(
        r'<div style=\"width: 860px; background(.*?)<div style=\"clear: both;\".*?',
        re.DOTALL)
    kanali = re.findall(vzorec_bloka, ime_datoteke)
    return kanali

def podatki_iz_bloka(blok):
    vzorec_podatkov = re.compile(
    r'<div style="float: left; width: 50px; color:#888;">(?P<mesto>.*?).*?'
    r'<span style="font-weight: bold; color:#00bee7;">(?P<ocena>[AB]+[+-]*)</span>.*?'
    r'<a href=".*">(?P<ime>.*?)</a>.*?'
    r'<sup><i style="color:#aaa; padding-left: 5px;" title="Category: (?P<kategorija>.*?)" class=".*?" aria-hidden="false"></i></sup>.*?'
    r'<div style="float: left; width: 80px;"><span style="color:#...;">(?P<objave>\d+,?\d+?)</span></div>.*?'
    r'<div style="float: left; width: 150px;">\s*(?P<vpisani>\d+\.?\d*.).*?'
    r'<span style="color:#555;">(?P<ogledi>.*?)</span>',
    re.DOTALL)
    podatki = re.search(vzorec_podatkov, blok)
    #slovar = pocisti_podatke(podatki).groupdict()
    slovar = podatki.groupdict()
    return slovar


def seznam_podatkov(mapa, ime_datoteke):
    dat = vsebina_datoteke(mapa, ime_datoteke)
    kanali = []
    for blok in bloki_iz_strani(dat):
        kanali.append(podatki_iz_bloka(blok))
    return kanali