print("Boudreaux & Thibodeaux's Po-Boy Shop \n")
print("------------------------------------ \n")
print("1. Catfish Poboy: $14.95")
print("2. Roast Beef Poboy: $13.95")
print("3. Sausage Poboy: $12.95")
print("4. Gumbo: $4.95")
print("\n ------------------------------------- \n")

# Constants
CATFISH = 14.95
ROASTBEEF = 13.95
SAUSAGE = 12.95
GUMBO = 4.95

choice = int(input("What would you like to order? Type the appropriate number of the menu item: ")
# order_num = int(reply)

# Decision Structure
if choice == 1:
    total = CATFISH
elif choice == 2:
    total = ROASTBEEF
elif choice == 3:
    total = SAUSAGE
elif choice == 4:
    total = GUMBO
else:
    print("I'm sorry. That was not an appropriate choice.")
    total = 0

# Calculations
salesTax = 0.0945
subTotal = total + (total * salesTax)
print(f'Your total is ${subTotal:.2f}')
# print("Your total is ${tot:.2f)".format(tot=subTotal))
            
# menu = {
   # 1: ("Catfish Poboy:", 14.95),
   # 2: ("Roast Beef Poboy:", 13.95),
   # 3: ("Sausage Poboy:", 12.95),
   # 4: ("Gumbo:", 4.95) 
# }
# choice, (item, price) = menu
# salesTax = 0.0945

# print("Boudreaux & Thibodeaux's Po-Boy Shop")

# choice = int(input("What would you like to order? Type the appropriate number of the menu item: "))

# for choice, (item, price) in menu.items():
   # print(f"{choice}. {item}: ${price:.2f}")

#if choice in menu:
   # item, price = menu[choice]
   # total = price + (price * salesTax)
   # print(f"Your total is ${total:.2f}")
# else:
   # print("Invalid selection. Please restart the program and select a valid menu item.")
