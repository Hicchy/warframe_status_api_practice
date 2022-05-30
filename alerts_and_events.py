import requests

response_fissures = requests.get("https://api.warframestat.us/pc/en/fissures")
fissures_data = response_fissures.json()


def get_fissures():
    for fissure in fissures_data:
        print(f"""{fissure['node']}, {fissure['missionType']}, {fissure['tier']}, against {fissure['enemy']}, expires in {fissure['eta']}\n""")


response_darvo = requests.get("https://api.warframestat.us/pc/en/dailyDeals")
darvo_data = response_darvo.json()[0]
darvo_deal = f"""\nCurrent Darvo Deal is the {darvo_data['item']} sold for {darvo_data['salePrice']} plat
at a {darvo_data['discount']}% discount and will change in {darvo_data['eta']}\n"""