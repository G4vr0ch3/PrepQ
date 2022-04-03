import ui_interface
import codecs
import string
import random

import geopandas as gpd

def wrt (name, infos, docpath, geo=""):
    with open("zones.json", "r", encoding='utf-8') as file:
        content = file.read()
        old = open("zones.json.old", "w")
        old.write(content)

    tnm = ''
    tnn = name
    tnn = tnn.split(' ')
    if (len(tnn[-1]) == 0):
        tnm.pop()

    for i in range(len(tnn)):
        tnm += tnn[i][0]

    while (testid(tnm)!=True):
        tnm += random.choice(string.ascii_letters)
        tnm = tnm.upper()

    fnam = tnm +".html"

    with open("zones.json", "w", encoding='utf-8') as file:
        newline = u'{"type":"Feature","id":"'+tnm+'","properties":{"name":"'+name+'", "infos":"'+infos+' - Ajoutée localement"},"geometry":{"type":"Polygon","coordinates":[['+geo+']]}}'
        content = content[:-5]
        content = content + ',\n' + '\n' + newline + '\n' + '\n' + ']}' + '\n'
        content.encode('utf-8')
        file.write(content)
        file.close()

    with open(docpath, "r", encoding='utf-8') as source:
        fnam = tnm +".html"
        typ = ftype(docpath)
        source = source.read()
        with open (fnam, "w", encoding='utf-8') as navPrep:
            if (typ == 'html'):
                navPrep.write(source)
            else:
                print(docpath)

def ftype(path):
    if (path[-4:] == 'html'):
        return 'html'
    elif (path[-3:] == 'pdf'):
        return 'pdf'
    else:
        return 'NoneType'


def testid(tnm):

    df = gpd.read_file("zones.json")
    for i in df["id"]:
        if tnm == i:
            return False
    return True
