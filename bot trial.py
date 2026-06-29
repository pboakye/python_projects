
property_listings = [
    {"address": "123 Ahodwo Dabang", "price": 250000.00, "beds": 2},
    {"address": "789 East Legon", "price": 400000.00, "beds": 3},
    {"address": "456 Pine Crescent", "price": 550000.00, "beds": 4},
    {"address": "101 Palm Boulevard", "price": 300000.00, "beds": 3}
]

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
print("-- /n Summary of Search -- ")
print(f" Client Name : {buyer_name.upper()}")
print(f" Target Budget : $ {buyer_budget:}")
print(f"Required Bedrooms : {buyer_beds} Bedrooms")
print(" ------------------------------------------- ")
print(" Great!! I'm searching our Database for Matching Properties ...... ")
print("Matching Properties Found")
matches_found = 0
buyer_shortlist = []
for house in property_listings :
    if house ["price"] <= buyer_budget and house ["beds"] == buyer_beds:
        print(f" {house['address']} |Price: ${house['price']:,.2f} | Beds: {house['beds']}")
        matches_found +=1
if matches_found == 0:
    print("Sorry, No Properties Match Your Criteria Right Now. ")
    buyer_shortlist.append(house)
print("Saved Buyer Shortlist in Memory")
print(buyer_shortlist)








