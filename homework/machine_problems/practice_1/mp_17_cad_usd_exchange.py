# 17) Write a program in Python that converts from canadian dollars to US dollars. You will receive a decimal number corresponding to the amount in CAD and will answer with the corresponding amount in US dollars. Take the quotation of the dollar today.

from forex_python.converter import CurrencyRates

# Create a CurrencyRates object
c = CurrencyRates()

# Get the exchange rate from CAD to USD
conversion_rate = c.get_rate('CAD', 'USD')
print(f"1 CAD is equal to {conversion_rate} USD")
print(f"1 CAD is equal to {conversion_rate:.2f} USD")
amount_CAD_to_be_exchanged = float(input("Enter CAD you want to exchange to USD: "))
amount_USD = conversion_rate * amount_CAD_to_be_exchanged
print(f"You now have {amount_USD:.2f} USD")

conversion_rate = float(input("Enter the exchange rate from CAD to USD: "))
amount_CAD_to_be_exchanged = float(input("Enter the amount in CAD you want to exchange to USD: "))

amount_USD = conversion_rate * amount_CAD_to_be_exchanged
print(f"You now have {amount_USD:.2f} USD")

