from matplotlib import pyplot as plt
import numpy as np
import csv

plt.style.use("fivethirtyeight")

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    row = next(csv_reader)
    print(row["LanguagesWorkedWith"].split(';'))