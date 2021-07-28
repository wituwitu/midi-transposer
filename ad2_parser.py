import json

res = {}

with open("wytus.AD2Map", 'r') as f:
    for line in f.readlines():
        if line.startswith(" MAP_KeyMap_"):
            key = str(int(line[12:15]))
            val = int(line[18:-3])
            res[key] = val

with open("ad2_map.json", 'r') as f:
    ad2 = json.load(f)

for key in res.keys():
    if str(res[key]) in list(ad2['note'].keys()):
        res[key] = ad2['note'][str(res[key])]

with open("ad2_parsed.json", 'w') as f:
    json.dump(res, f, indent=2)

