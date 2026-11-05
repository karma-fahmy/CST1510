"""
RECORD CHECK  -  my version
===========================

Name  : Karmah abdelrahman mohamed lotfy abdellatif fahmy
Lane  : Cyber   
Date  :9/30/2026

Run it:   python template.py
"""


finish = False
check = ""
Num_over_limit = 0
while not finish:
    label = input("Enter a label: ")      
    try:
        value = float(input("value: "))     
    except ValueError:
        print("Invalid input for value. Please enter a number for value")

    try:
        limit = float(input("limit: "))     
    except ValueError:
        print("Invalid input for limit. Please enter a number for limit")

    difference = float(value) - float(limit)  
    try:
        percent = (float(value) / float(limit)) * 100       
    except ZeroDivisionError:
        print("Invalid input, limit cannot be equal to zero, please enter a different limit")

    status: str

    if percent >= 100: 
        status = "OVER LIMIT"
    elif  percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 33)
    print(f"   Record check  -  {label:>5}")
    print("=" * 33)
    print(f"Value : {value:>10.2f}")
    print(f"Limit : {limit:>10.2f}")
    print(f"Status : {status:>9}")
    print(f"Diff : {difference:>+11.2f}")
    print(f"percent : {percent:>7.2f}%")
    print("=" * 33)

    if status == "OVER LIMIT":
        Num_over_limit += 1

    try:
        check = input("Type 'quit' to exit or press Enter to continue: ").lower()
    except ValueError:
        print("Invalid input, please type 'quit' or press enter to continue: ")

    while check != "quit" and check != "":
        check = input("Invalid input, please type 'quit' or press Enter to continue: ").lower()

    
    if check == "quit":
            finish = True
            print(f"Number of records over limit: {Num_over_limit}")
            break










