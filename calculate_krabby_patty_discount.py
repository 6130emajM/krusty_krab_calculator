# Welcome to the Krusty Krab's Discount Calculator!
print("🦀 Welcome to the Krusty Krab! 🦀")

# Step 1: Define the menu prices
menu_items = {
    "Krabby Patty": 3.99,
    "Kelp Fries": 2.49,
    "Coral Soda": 1.99,
    "Seafoam Shake": 2.99,
    "Golden Loaf": 4.25
}

# Display the menu
print("\nToday's Menu:")
for item, price in menu_items.items():
    print(f"{item}: ${price:.2f}")

# Step 2: Calculate the total cost
total_cost = sum(menu_items.values())

# Step 3: Apply a 10% discount
discount_rate = 0.10
discount_amount = total_cost * discount_rate
final_amount = total_cost - discount_amount

# Step 4: Display the results
print("\nYour Receipt:")
print(f"Original Total: ${total_cost:.2f}")
print(f"Discount Amount (10%): ${discount_amount:.2f}")
print(f"Final Total After Discount: ${final_amount:.2f}")

# Step 5: Thank the customer
print("\nThank you for dining at the Krusty Krab! Have a Bikini Bottom-tastic day!")
