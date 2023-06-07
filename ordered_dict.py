items = [("BANANA FRIES", 12), ("POTATO CHIPS", 60), ("APPLE JUICE", 20), ("CANDY", 20)]

net_prices = {}

for item_name, price in items:
    if item_name not in net_prices:
        net_prices[item_name] = price
    else:
        net_prices[item_name] += price


for item_name, net_price in net_prices.items():
    print(item_name, net_price)
