# Exercise 1: Pizza Toppings

toppings = []
while True:
    topping = input("Enter a topping to add to your pizza (enter 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)

print("\nToppings for your pizza:")
for topping in toppings:
    print(topping)
