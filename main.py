import requests
from open_worlds import cambion_status
from open_worlds import cetus_status

response_darvo = requests.get("https://api.warframestat.us/pc/en/dailyDeals")
darvo_data = response_darvo.json()[0]
print(darvo_data)
darvo_deal = f"""Current Darvo Deal is the {darvo_data['item']} sold for {darvo_data['salePrice']} plat
at a {darvo_data['discount']}% discount and will change in {darvo_data['eta']}\n"""


print(cetus_status)
print(cambion_status)
print(darvo_deal)