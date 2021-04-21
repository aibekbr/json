import requests
import json

r = requests.get("https://api.ratesapi.io/api/latest?symbols")
data = json.loads(r.text)
rates=data.get("rates")

list_n=list(rates.keys())

print(list_n)
print("--------")

from_currency=input("Enter from curency: ")
to_currency=input("Enter to currency: ")
amount=int(input("Enter an amount: "))

result=amount/rates.get(from_currency)*rates.get(to_currency)

print(f"{amount} {from_currency} =",(result),f" {to_currency}")


    