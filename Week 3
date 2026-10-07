"""
RECORD CHECK  -  my version
===========================

Name  : Karmah Abdelrahman Mohamed Lotfy Abdellatif Fahmy
Lane  : Cyber
Date  : 10/7/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def print_report(label, value, limit, difference, percent, status):
    """This function prints the entire report"""
    print()
    print("=" * 33)
    print(f"   Record check  -  {label:>5}")
    print("=" * 33)
    print(f"Value : {value:>10.2f}")
    print(f"Limit : {limit:>10.2f}")
    print(f"Diff : {difference:>+11.2f}")
    print(f"percent : {percent:>7.2f}%")
    print(f"Status : {status:>9}")
    print("=" * 33)

def status_of(percent):
    """this function checks if the percentage is over the limit or under the limit, it also sends a warning if is is close to reaching the limit"""
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return status


def check(value, limit):
    """This function calculates and returns the difference and percentage between value and limit"""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


finish = False
check_exit = ""
Number_of_over_limit = 0
while not finish:
    label = input("Enter a label ")      
    value = float(input("Enter a value "))     
    limit = float(input("Enter a limit "))


    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    check_exit = input("Type 'quit' to exit or press Enter to continue: ")
    if status == "OVER LIMIT":
                Number_of_over_limit = Number_of_over_limit + 1

    if check_exit == "quit":
            finish = True
            print(f"Number of records over limit: {Number_of_over_limit}")
            break

