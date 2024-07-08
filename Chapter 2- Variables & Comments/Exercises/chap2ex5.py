# Cost of one USB stick
usb_price = 6

# Total amount of money she has
total_money = 67

# Calculate how many USB sticks she can buy
num_usb = total_money // usb_price

# Calculate the money left after buying the USB sticks
money_left = total_money % usb_price

# Print the results
print("Number of USB sticks she can buy:", num_usb)
print("Money left after buying USB sticks: £", money_left)
