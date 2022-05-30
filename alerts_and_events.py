import requests

response_fissures = requests.get("https://api.warframestat.us/pc/en/fissures")
fissures_data = response_fissures.json()


def get_fissures():
    for fissure in fissures_data:
        print(f"""{fissure['node']}, {fissure['missionType']}, {fissure['tier']}, against {fissure['enemy']}, expires in {fissure['eta']}\n""")