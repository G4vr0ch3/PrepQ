import ui_interface
import codecs
import string
import random
import shutil

import geopandas as gpd

from datetime import date


def wrt (name, infos, docpath, geo=""):
    with open("zones/zones.json", "r", encoding='utf-8') as file:
        content = file.read()
        old = open("zones/zones.json.old", "w", encoding='utf-8')
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

    typ = ftype(docpath)
    fnam = "prepa/" + tnm + "." + typ

    shutil.copyfile(docpath, fnam)

    with open("zones/zones.json", "w", encoding='utf-8') as file:
        newline = u'{"type":"Feature","id":"'+tnm+'","properties":{"name":"'+name+'", "infos":"'+infos+' - Ajoutée localement", "filename":"'+tnm+'.'+typ+'"},"geometry":{"type":"Polygon","coordinates":[['+geo+']]}}'
        content = content[:-5]
        content = content + ',\n' + '\n' + newline + '\n' + '\n' + ']}' + '\n'
        content.encode('utf-8')
        file.write(content)
        file.close()

    return tnm


def ftype(path):
    if (path[-4:] == 'html'):
        return 'html'
    elif (path[-3:] == 'pdf'):
        return 'pdf'
    else:
        return 'NoneType'


def testid(tnm):

    df = gpd.read_file("zones/zones.json")
    df.head(2)

    for i in range(len(df)):
        if tnm == df["id"][i]:
            return False
    return True
