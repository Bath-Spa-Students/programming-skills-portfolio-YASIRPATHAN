# Exercise 3: T-Shirt

def make_shirt(size, message):
    """Prints a summary of the size and message printed on a shirt."""
    print(f"Creating a shirt of size {size} with the message: {message}")

# Call the function using positional arguments
make_shirt("Large", "I love Python")

# Call the function using keyword arguments
make_shirt(size="Medium", message="Hello, World!")
