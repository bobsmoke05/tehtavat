import requests

def hae_chuck_norris_vitsi():
    osoite = "https://api.chucknorris.io/jokes/random"
    try:
        vastaus = requests.get(osoite)
        vastaus.raise_for_status()
        data = vastaus.json()
        vitsi = data.get("value")
        if vitsi:
            print(vitsi)
    except requests.exceptions.RequestException as e:
        print(f"Virhe: {e}")
    except Exception as e:
        print(f"Virhe: {e}")

hae_chuck_norris_vitsi()