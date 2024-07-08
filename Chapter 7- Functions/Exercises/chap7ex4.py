# Exercise 4: Large Shirts

def make_shirt(size="Large", message="I love Python"):
    """Prints a summary of the size and default message printed on a shirt."""
    print(f"Creating a {size} shirt with the message: {message}")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="Medium")

# Make a small shirt with a different message
make_shirt(size="Small", message="Python is awesome!")
