import requests 

BASE_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert_currency(base, target, amount):
    response = response.get(BASE_URL)
    data = response.json()

    if "rates" not in data:
        print("❌ Invalid Base Currency")
        return 
    
    rates = data["rates"]
    if target.upper() not in rates:
        print("❌ Invalid Target Currency")
        return
    
    converted_amount = amount * rates[target.upper()]
    print(f"\n💱 {amount} {base.upper()} = {converted_amount:.2f} {target.upper()}")

while True:
    base =  input("Enter base currency (e.g., USD) ")
    target = input("Enter target currency (e.g., INR) ")
    amount = float(input("Enter amount to convert: "))

    convert_currency(base, target, amount)

    if input("Do you want to convert another amount? (y/n): ").lower() != 'y':
        print("Exiting the currency converter. Goodbye!")
        break
