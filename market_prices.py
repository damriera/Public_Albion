"""

-----
market_prices.py
-----

-----
Ce programme trie les informations récupérées par "get_market_prices.py".

Il va, dans le fichier "Martlock_prices" ne garder que les ressources de Martlock.

A utiliser apres "get_market_prices.py" pour plus d'efficacité avec "prices_checker".

-> l21 et l30, changer "Martlock" par le nom de la ville que vous voulez.
-----

"""
import json

file = "market_prices.json"
dump_file = "Martlock_prices.json"

def prices(file, dump_file):
    with open(file, "r") as FILE:
        data = json.load(FILE)
    
    tab = []

    for resources in data:
        if resources["city"] == "Martlock":
            tab.append(resources)

    dump_data(tab, dump_file)



def dump_data(data, file):
    with open(file, "w") as FILE:
        json.dump(data, FILE, indent=2)
        print("<;> good :3")

prices(file, dump_file)