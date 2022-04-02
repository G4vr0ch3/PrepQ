
def wrt (name, id, infos, docpath, geo=""):
    with open("zones.json", "r") as file:
        content = file.read()
        old = open("zones.json.old", "w")
        old.write(content)
    with open("zones.json", "w") as file:
        newline = '{"type":"Feature","id":"'+id+'","properties":{"name":"'+name+'", "infos":"'+infos+'"},"geometry":{"type":"Polygon","coordinates":[['+geo+']]}}'
        content = content[:-5]
        content = content + ',\n' + '\n' + newline + '\n' + '\n' + ']}' + '\n'
        file.write(content)
        file.close()
