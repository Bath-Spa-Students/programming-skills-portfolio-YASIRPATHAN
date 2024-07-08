# Exercise 3: Glossary 2

# Updated glossary with additional terms
glossary = {
    'variable': 'A name that is used to denote a value stored in memory.',
    'function': 'A block of organized, reusable code that is used to perform a single, related action.',
    'loop': 'A control structure that repeats a statement or group of statements while a given condition is true.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable collection of items in a particular order.',
    'set': 'A collection of unique items.',
    'method': 'A function that belongs to an object.',
    'class': 'A blueprint for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions, methods).'
}

# Print each word and its meaning using a loop
for term, definition in glossary.items():
    print(f"{term}: {definition}\n")
