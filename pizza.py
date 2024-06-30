# Your code below:

topings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
print(topings)

prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(topings)
print(num_pizzas)

print( f"We sell {num_pizzas} different kinds of pizza!")

pizza_and_prices = [
  [2, "pepperoni"], 
  [6, "pineapple"], 
  [1, "cheese"], 
  [3, "sausage"], 
  [2, "olives"], 
  [7, "anchovies"], 
  [2, "mushrooms"]
]

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
print( f"{cheapest_pizza} is the cheapest pizza!")
priciest_pizza = pizza_and_prices[-1]
print( f"{priciest_pizza} is the most expensive pizza!")

pizza_and_prices.pop()
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)





