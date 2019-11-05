def vsebina_datoteke(mapa, ime_datoteke):
    path = os.path.join(mapa, ime_datoteke)
    with open(path, 'r', encoding='utf-8') as dat:
        return dat.read()

def pripravi_imenik(ime_datoteke):
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


def bloki_iz_strani(ime_datoteke):
    vzorec_bloka = re.compile(
        r'<div style=\"width: 860px; background(.*?)<div style=\"clear: both;\".*?',
        re.DOTALL)
    kanali = re.findall(vzorec_bloka, ime_datoteke)
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