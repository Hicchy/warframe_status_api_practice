import requests


response_cetus = requests.get("https://api.warframestat.us/pc/cetusCycle")
cetus_data = response_cetus.json()
cetus_status = f"\nIt is currently {cetus_data['state']} in Cetus and will change in {cetus_data['timeLeft']}\n"



response_cambion = requests.get("https://api.warframestat.us/pc/cambionCycle")
cambion_data = response_cambion.json()
cambion_status = f"It is currently {cambion_data['active']} in Cambion Drift and will change in {cambion_data['timeLeft']}\n"
