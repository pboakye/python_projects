print("--- Real Estate Assistant Bot ---")
print("Welcome! Let's Find Your Dream Home.")
buyer_name = input(" What's Your Name? ")
print(f"Thanks {buyer_name.upper()}! Let's get your requirements.")
while True:
    try:
        buyer_budget = float(input("What is Your Maximum Budget? (eg. $ 350000): "))
        break
    except ValueError:
        print(" Please Enter a valid number using only Digits and Decimals ")
while True:
    try:
        buyer_beds = int(input(" How Many Bedrooms Do You Need? eg. 1,2,3 "))
        break
    except ValueError:
        print(" Please Enter a whole Number eg. 1,2,3 ")





