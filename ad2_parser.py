import json

ad2_parsed = {}

with open("wytus.AD2Map", 'r') as f:
    for line in f.readlines():
        if line.startswith(" MAP_KeyMap_"):
            key = str(int(line[12:15]))
            val = int(line[18:-3])
            ad2_parsed[key] = val

with open("maps/ad2_map.json", 'r') as f:
    ad2_map = json.load(f)

with open("maps/ad2_to_gm.json", 'r') as f:
    ad2_to_gm = json.load(f)

with open("maps/gm_map.json", 'r') as f:
    gm_map = json.load(f)

for key in ad2_parsed.keys():
    ad2_key = str(ad2_parsed[key])
    if ad2_key in list(ad2_map.keys()):
        ad2_name = ad2_map[ad2_key]
        gm_name = ad2_to_gm[ad2_name]
        try:
            ad2_parsed[key] = gm_map[gm_name]
        except KeyError:
            ad2_parsed[key] = 0

with open("maps/ad2_parsed.json", 'w') as f:
    json.dump(ad2_parsed, f, indent=2)
