import json

file = "Martlock_prices.json"

def main(file):
    with open(file, "r") as FILE:
        data = json.load(FILE)
    
    tiers = ["T1", "T2", "T3", "T4", "T5"]
    do_not = "@"

    most_worth = []
    worth = ["None", -float('inf')]
    worth2 = ["None", -float('inf')]
    for tier in tiers:
        for prices in data:
            if tier in prices["item_id"] and not do_not in prices["item_id"]:
                if prices["sell_price_min"] > worth[1]:
                    worth2 = worth
                    worth = [prices["item_id"], prices["sell_price_min"]]
        most_worth.append(worth2)
        most_worth.append(worth)
        worth = ["None", -float('inf')]
        worth2 = ["None", -float('inf')]
    
    for items in most_worth:
        print("-------")
        print(f"<;> {items[0]} : {items[1]}")
    print("-------")


main(file)