#  Display menu
print("===RESTAURANT MENU===")
print("1. Pizza - $15.99")
print("2. Burger - $12.50")
print("3. Salad - $9.99")
print("4. Pasta - $13.75")
# Choice
choice = int(input("Enter your choice (1-4): "))
# Choice match
if choice == 1:
    food = "Pizza"
    price = 15.99
elif choice == 2:
    food = "Burger"
    price = 12.50
elif choice == 3:
    food = "Salad"
    price = 9.99
elif choice == 4:
    food = "Pasta"
    price = 13.75
else:
    print("Invalid choice!")
    exit()   

#Drink   

drink_choice = input("Would you like a drink? (+$2.50) (yes/no): ").lower()

if drink_choice == "yes":
    drink = True
    drink_price = 2.50
else:
    drink = False
    drink_price = 0
#  Tax
subtotal = price + drink_price
tax = subtotal * 0.08
total = subtotal + tax
# Receipt
print("\n=== YOUR ORDER ===")
print(f"Food: {food} - ${price:.2f}")
print(f"Drink: {'Yes' if drink else 'No'} - ${drink_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
