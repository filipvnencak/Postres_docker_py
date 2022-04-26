import json




with open('demo_data.json',) as f:
    req = json.loads(f.read())

data = req['frinx-uniconfig-topology:configuration']['Cisco-IOS-XR-infra-policymgr-cfg:policy-manager']['policy-maps']['policy-map']

list = []


for x in data:
    if 'policy-map-rule' in x:
        x["policy-map-rule"] = True

    else: x ['policy-map-rule'] = False

    # print(x)
    list.append(x)
# print(type(list))


# print(type(array))
