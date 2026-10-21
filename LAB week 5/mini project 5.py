"""
RECORD CHECK  -  my version
===========================

Name  :  Karmah abdelrahman mohamed lotfy abdellatif fahmy
Lane  :  Cyber
Date  :  10/21/2026

Run it:   python template.py
Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """stores the label, value and limit"""
        self.label = label
        self.value = value
        self.limit = limit


    def percent(self):
        """calculates and returns the percentage of how much the value is equal/more/less than the limit"""
        return (self.value / self.limit) * 100

    def status(self):
        """this method checks if the percentage using percent() is over the limit or under the limit, it also sends a warning if is is close to reaching the limit"""
        per = self.percent()
        if per >= 100:
            return "OVER LIMIT"
        elif per >= 90:
            return "WARNING"
        else:
            return "OK"
        
    def check_rec_overlimit(self):
        """check if value is over limit using status() and adds a 1 to the overall total count if the statment is true"""
        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1


    


def load_records(path):
        """Reads the variables label, value, limit lines from a file and return a list of dicts"""
        records = []
        with open(path) as k:
            for line_number, line in enumerate(k, start = 1):
                line = line.strip()
                if not line:
                    continue
                try: 
                    label, value, limit = line.split(",")
                    records.append(Record(label.strip(), float(value), float(limit)))
                except ValueError:
                    print("there is some corrupted lines in the file")
        return records




try:
    records = load_records("records_sample_miniProject.txt")
except FileNotFoundError:
    print("Error: records_sample.txt was not found.")
    records = []



for record in records:
    record.check_rec_overlimit()
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Value   : {record.value:>10.2f}")
    print(f"Limit   : {record.limit:>10.2f}")
    print(f"Percent : {record.percent():>9.2f}%")
    print(f"Status  : {record.status():>10}")
    print("=" * 34)


print(f"\nrecords over the limit: {Record.over_limit_count}")


