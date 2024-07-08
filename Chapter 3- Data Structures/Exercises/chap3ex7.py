# Exercise 7: Seeing the World

# Step 1: Create a list of places to visit
places_to_visit = ['Tokyo', 'oman', 'turkey', 'Sydney', 'pakistan']

# Step 2: Print the list in its original order
print("Original order:")
print(places_to_visit)

# Step 3: Print the list in alphabetical order using sorted(), without modifying the actual list
print("\nAlphabetical order:")
print(sorted(places_to_visit))

# Step 4: Print the list to show it's still in its original order
print("\nStill in original order:")
print(places_to_visit)

# Step 5: Print the list in reverse alphabetical order using sorted(), without modifying the actual list
print("\nReverse alphabetical order:")
print(sorted(places_to_visit, reverse=True))

# Step 6: Print the list to show it's still in its original order
print("\nStill in original order:")
print(places_to_visit)

# Step 7: Reverse the order of the list using reverse()
places_to_visit.reverse()
print("\nReversed order:")
print(places_to_visit)

# Step 8: Reverse the order again to get back to the original order
places_to_visit.reverse()
print("\nBack to original order:")
print(places_to_visit)

# Step 9: Sort the list in alphabetical order using sort()
places_to_visit.sort()
print("\nSorted in alphabetical order:")
print(places_to_visit)

# Step 10: Sort the list in reverse alphabetical order using sort()
places_to_visit.sort(reverse=True)
print("\nSorted in reverse alphabetical order:")
print(places_to_visit)
