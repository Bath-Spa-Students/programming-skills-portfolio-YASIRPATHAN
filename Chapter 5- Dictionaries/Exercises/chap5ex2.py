# Exercise 2: Glossary

# Define a glossary dictionary
glossary = {
    'variable': 'A name that is used to denote a value stored in memory.',
    'function': 'A block of organized, reusable code that is used to perform a single, related action.',
    'loop': 'A control structure that repeats a statement or group of statements while a given condition is true.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.'
}

# Print each word and its meaning
for term, definition in glossary.items():
    print(f"{term}: {definition}\n")
