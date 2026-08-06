
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
print(" \n Summary of Search -- ")
print(f" Client Name : {buyer_name.upper()}")
print(f" Target Budget : $ {buyer_budget:,.2f}")
print(f"Required Bedrooms : {buyer_beds} Bedrooms")
print(" ------------------------------------------- ")
print(" Great!! I'm searching our Database for Matching Properties ...... ")
print("Matching Properties Found")
matches_found = 0
def find_listings(listings,target_budget,target_beds):
    stretch_budget = target_budget * 1.10
    buyer_shortlist = []
    for house in listings :
     if house ["beds"] == target_beds:
         if house["price"] <= target_budget:
            print(f" Direct Match: {house['address']} |Price: ${house['price']:,.2f} | Beds: {house['beds']}")
            buyer_shortlist.append(house)
         elif house ["price"] <= stretch_budget:
             print(f" Stretch Budget Option: {house['address']} |Price: ${house['price']:,.2f} | Beds: {house['beds']}")
             buyer_shortlist.append(house)
     elif house["beds"] == target_beds +1 and house ["price"] <= stretch_budget:
         print(f" Upgrade Selection: {house['address']} |Price: ${house['price']:,.2f} | Beds: {house['beds']}")
         buyer_shortlist.append(house)
     elif house["beds"] == target_beds -1 and house ["price"] <= target_budget:
         print(f" Value Option (-1 Bed) : {house['address']} |Price: ${house['price']:,.2f} | Beds: {house['beds']}")
         buyer_shortlist.append(house)

    return buyer_shortlist
final_matches = find_listings(property_listings,buyer_budget,buyer_beds)


if len(final_matches) == 0:
    print("Sorry, No Properties Match Your Criteria Right Now. ")
else:
    print("Saved Buyer Shortlist in Memory")
    print(final_matches)








