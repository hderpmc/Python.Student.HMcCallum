# Boudreaux & Thibodeaux's Bakery
# Calculate total with 9.45% sales tax

taxRate = 0.0945

menu = {
    1: {"name": "Muffin", "price": 5.95},
    2: {"name": "King Cake Slice", "price": 4.95},
    3: {"name": "Croissant", "price": 3.95},
    4: {"name": "Scone", "price": 3.75},
}

def print_menu():
    print("Boudreaux & Thibodeaux's Bakery")
    for num, item in menu.items():
        print(f"{num}. {item['name']}: ${item['price']:.2f}")

def main():
    subtotal = 0.0
    print_menu()

    while True:
        user_input = input("\nWhat would you like to order? Type the appropriate number of the menu item or Done when order is complete: ").strip()

        if user_input.upper() == "DONE":
            break
        
        if not user_input.isdigit()
            print("I'm sorry that is not an appropriate response.")
            continue
        
        item = menu[item.num]

        while True:
            quantity_input = input("How many of that would you like to order? ").strip()
            if not quantity_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            quantity = int(quantity_input)
            if quantity <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
            
        subtotal += item["price"]* quantity
        print(f"You have ordered {quantity} {item['name'].lower()} (5) for $item['price']:.2f} each")

    total = subtotal * (1 + taxRate)
    print(f"\nYour total is ${total:.2f}")

if __name__ == "__main__":
    main()
