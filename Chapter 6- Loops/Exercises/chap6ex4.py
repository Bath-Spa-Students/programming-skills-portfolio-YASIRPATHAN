# Exercise 4: Deli

sandwich_orders = ['tuna', 'blt', 'turkey', 'pastrami', 'pastrami', 'roast beef', 'pastrami']
finished_sandwiches = []

print("Welcome to the deli!")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)
