# Movie ticket 
# User input
name = input("Enter your name: ")
age = int(input("Enter your age:"))
tickets = int(input("How many tickets?"))
# Age/price
if age < 13:
 ticket_price = 8
 ticket_type = "Child"

elif age <= 64:
 ticket_price = 12
 ticket_type = "Adult"

else:
 ticket_price = 9 
 ticket_type = "Senior" 
# Calculate
total_cost = tickets * ticket_price
# Receipt

print("\n=== MOVIE TICKET RECEIPT ===")
print(f"Customer: {name}")
print(f"Ticket Type: {ticket_type} (${ticket_price:.2f} each)")
print(f"Quantity: {tickets}")
print(f"Total Cost: ${total_cost:.2f}")
print("Thank you for your purchase!")
