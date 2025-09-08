from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "Ari's Diner"
owner_name = "Arianne Aguilar"

# Integer data type
year_since = 2025

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = True

# List data type
product_names = ["Truffle Mac n Cheese", "Baby Back Ribs", "Mashed Potatoes"]
beverages = ["Iced Tea", "Mango Shake"]

# Tuple data type
business_hours = ("10:00 AM", "9:00 PM")

# Dictionary data type
menu = {
    "Truffle Mac n Cheese": 379.00,
    "Baby Back Ribs": 399.00,
    "Mashed Potatoes": 150.00,
    "Iced Tea": 60.00,
    "Mango Shake": 80.00
}

# Set data type
common_allergens = {"gluten", "dairy", "soy"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Truffle Mac n Cheese']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Baby Back Ribs']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Mashed Poatoes']:.2f}", target="price3")
display(beverages[0], target="prod4")
display(f"₱{menu['Iced Tea']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['Mango Shake']:.2f}", target="price5")

# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")


# Display order type

display(f"Dine-in Available", target="orderType")
