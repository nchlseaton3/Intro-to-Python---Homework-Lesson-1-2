# Pet calculator
# User input
pet_type = input("Enter pet type (dog/cat/bird/hamster): ").lower()
age = int(input("Enter your pet's age in human years: "))

# Conversion 
if pet_type == "dog" or pet_type == "cat":
    if age <= 2:
        pet_age = age * 12  # 1 year ~ 12, 2 years ~ 24
    else:
        pet_age = 24 + (age - 2) * 4
elif pet_type == "bird":
    pet_age = age * 9
elif pet_type == "hamster":
    pet_age = age * 25
else:
    print("Sorry, pet type not recognized!")
    exit()

# Receipt
print("\n=== PET AGE CONVERSION ===")
print(f"Pet Type: {pet_type.capitalize()}")
print(f"Human Age: {age} years")
print(f"Pet Age: {pet_age} pet years")

print(f"\nFun Fact: Your {pet_type} is like a {pet_age}-year-old human!")
