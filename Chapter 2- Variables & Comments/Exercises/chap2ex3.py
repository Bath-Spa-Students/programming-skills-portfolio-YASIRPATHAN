# Assign a name to a variable with whitespace characters
name = "\t\n  John Doe  \n\t"

# Print the name with whitespace displayed
print("Original name with whitespace:")
print(f"'{name}'")

# Print the name using lstrip() to remove leading whitespace
print("\nName with leading whitespace removed:")
print(f"'{name.lstrip()}'")

# Print the name using rstrip() to remove trailing whitespace
print("\nName with trailing whitespace removed:")
print(f"'{name.rstrip()}'")

# Print the name using strip() to remove both leading and trailing whitespace
print("\nName with both leading and trailing whitespace removed:")
print(f"'{name.strip()}'")
