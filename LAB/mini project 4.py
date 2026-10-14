"""
RECORD CHECK  -  my version
===========================

Name  :  Karmah abdelrahman mohamed lotfy abdellatif fahmy
Lane  :  Cyber
Date  :  10/14/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



def load_records(path):
    """Reads the variables label, value, limit lines from a file and return a list of dicts"""
    records = []
    with open(path) as k:
        for line in k:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records

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
    print(f"Number of records over limit: {Number_of_over_limit}\n")



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



records = []

with open("to_text_file_records.txt", "w") as k:
    k.write("")


try: 
    records = load_records("records_sample_miniProject.txt")
except FileNotFoundError:
    print("This file is not found")

count = 0
Number_of_over_limit = 0

for report in records:
    difference, percent = check(records[count]["value"], records[count]['limit'])
    status = status_of(percent)
    print_report(records[count]['label'], records[count]['value'], records[count]['limit'], difference, percent, status)

    with open("to_text_file_records.txt", "a") as k:
            file_records = f"{records[count]['label']}: {status}\n"
            k.write(file_records)
   
    if status == "OVER LIMIT":
        Number_of_over_limit = Number_of_over_limit + 1

    count += 1
























# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.



#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
