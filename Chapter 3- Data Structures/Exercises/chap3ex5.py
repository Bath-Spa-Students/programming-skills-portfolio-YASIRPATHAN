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
new_guest = 'Nikola Tesla'
guests[1] = new_guest

# Print second set of invitation messages
print(f"Updated invitation messages:\n")
for guest in guests:
    print(f"Dear {guest},\n\tYou are cordially invited to dinner at my place. Please join us!\n")
