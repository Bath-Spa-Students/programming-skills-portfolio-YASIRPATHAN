# Exercise 4: Guest List

# List of guests
guests = ['Amaan', 'zaid', 'tehami']

# Print invitation messages
for guest in guests:
    print(f"Dear {guest},\n\tYou are cordially invited to dinner at my place. Please join us!\n")

# Exercise 5: Change Guest List

# Print the guest who can't make it
guest_cant_make_it = guests[1]  # Assuming Leonardo da Vinci can't make it
print(f"Unfortunately, {guest_cant_make_it} can't make it to dinner.\n")

# Replace the guest who can't make it with a new guest
new_guest = 'malka'
guests[1] = new_guest

# Print second set of invitation messages
print(f"Updated invitation messages:\n")
for guest in guests:
    print(f"Dear {guest},\n\tYou are cordially invited to dinner at my place. Please join us!\n")

# Exercise 6: Shrinking Guest List

# Print message that only two people can be invited
print("Sorry, we can only invite two people for dinner.")

# Use pop() to remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, but we can't invite you to dinner.")

# Print invitation messages to remaining two guests
print("\nInvitation messages for remaining guests:\n")
for guest in guests:
    print(f"Dear {guest},\n\tYou are still invited to dinner at my place. Please join us!\n")

# Use del to remove the last two names from the list
del guests[1]
del guests[0]

# Print the empty list to confirm
print("Final guest list:", guests)
