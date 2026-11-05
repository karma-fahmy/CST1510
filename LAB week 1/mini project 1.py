"""
RECORD CHECK  -  my version
===========================

Name  : Karmah abdelrahman mohamed lotfy abdellatif fahmy
Lane  : Cyber
Date  : 1/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = input("Enter an ID ")      
value = float(input("Enter a value "))
limit = float(input("Enter a limit "))

difference = value - limit
percentage = (value / limit) * 100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Value : {value:>10.2f}")
print(f"Limit : {limit:>10.2f}")
print(f"Diff : {difference:>+11.2f}")
print(f"percent : {percentage:>7.2f}%")

print("=" * 34)



