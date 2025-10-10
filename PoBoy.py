# Boudreaux & Thibodeaux's Po-Boy Shop Program

menu = {
    1: ("Catfish Poboy:", 14.95),
    2: ("Roast Beef Poboy:", 13.95),
    3: ("Sausage Poboy:", 12.95),
    4: ("Gumbo:", 4.95) 
}
choice, (item, price) = menu
salesTax = 0.0945

print("Boudreaux & Thibodeaux's Po-Boy Shop")

choice = int(input("What would you like to order? Type the appropriate number of the menu item: "))

for choice, (item, price) in menu.items():
    print(f"{choice}. {item}: ${price:.2f}")

if choice in menu:
    item, price = menu[choice]
    total = price + (price * salesTax)
    print(f"Your total is ${total:.2f}")
else:
    print("Invalid selection. Please restart the program and select a valid menu item.")
