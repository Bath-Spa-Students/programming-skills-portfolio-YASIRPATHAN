# Exercise 5: No Pastrami

sandwich_orders = ['tuna', 'blt', 'pastrami', 'turkey', 'pastrami', 'roast beef', 'pastrami']
finished_sandwiches = []
print("Sorry, the deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("Here are the remaining sandwiches to be made:")
for sandwich in sandwich_orders:
    print(sandwich)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)
