burger_prices = []
beverage_prices = []

burger_prices.append(int(input()))
burger_prices.append(int(input()))
burger_prices.append(int(input()))

beverage_prices.append(int(input()))
beverage_prices.append(int(input()))

cheapest_set = min(burger_prices) + min(beverage_prices) - 50
print(cheapest_set)