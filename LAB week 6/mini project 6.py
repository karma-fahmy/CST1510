"""
RECORD CHECK  -  my version
===========================

Name  :  Karmah abdelrahman mohamed lotfy abdellatif fahmy
Lane  :  Cyber
Date  :  11/4/2026

Run it:   python template.py
Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mini_project_records_sample.csv")


df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda p: (
    "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
))


#           **Threshold**
print(df) 


#           **Typical**
status_not_equal_OK = df[(df["status"] == "OVER LIMIT" ) | (df["status"] == "WARNING")]
print("\n",status_not_equal_OK)


#           **Excellent**
df.groupby("status")
print("\n",df["status"].value_counts())

df["status"].value_counts().plot(kind="bar")
plt.title("Status per Count")
plt.savefig("status_counts_mini_project.png")
plt.show()

