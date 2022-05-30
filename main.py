import requests

response_cetus = requests.get("https://api.warframestat.us/pc/cetusCycle")
cetus_data = response_cetus.json()
cetus_status = f"\nIt is currently {cetus_data['state']} in Cetus and will change in {cetus_data['timeLeft']}\n"

response_cambion = requests.get("https://api.warframestat.us/pc/cambionCycle")
cambion_data = response_cambion.json()
cambion_status = f"It is currently {cambion_data['active']} in Cambion Drift and will change in {cambion_data['timeLeft']}\n"

response_darvo = requests.get("https://api.warframestat.us/pc/en/dailyDeals")
darvo_data = response_darvo.json()[0]
print(darvo_data)
darvo_deal = f"""Current Darvo Deal is the {darvo_data['item']} sold for {darvo_data['salePrice']} plat
at a {darvo_data['discount']}% discount and will change in {darvo_data['eta']}\n"""


print(cetus_status)
print(cambion_status)
print(darvo_deal)