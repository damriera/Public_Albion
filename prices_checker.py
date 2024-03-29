"""

-----
prices_checker.py
-----

-----
Ce programme est fait pour regarder les prix des ressources à Martlock

*!* Les prix affichés sont ceux des prix de vente minimum *!*

Le nom des ressources sont de la sorte:
T1_ -> T8_
ROCK ; WOOD ; HIDE ; ORE ; FIBER

Pour voir le prix des resources enchantés, ajouter:
_LEVEL0@0
a la fin du nom de la ressource, remplacer 0 par le niveau d'enchantement.

Si <;> oopsie est affiché, alors la récupération des donnée a eu un problème...
-----

"""
import json

file = "Martlock_prices.json"

def check(file):
    with open(file, "r") as file:
        data = json.load(file)
    
    print("<;> Resource name ?")
    arg = str(input())

    while arg != "q":
        for resources in data:
            if resources["item_id"] == arg:
                if resources["sell_price_min_date"] == "0001-01-01T00:00:00":
                    print("<;> oopsie :3")
                else :
                    print(f"Price : {resources['sell_price_min']}\n")
        print("<;> Resource name ?")
        arg = str(input())

    print("<;> bye bye...")             

check(file)