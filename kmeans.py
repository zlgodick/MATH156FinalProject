import pandas as pd
import numpy as np
import csv
import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, "Train.csv")
with open(file_path, mode='r') as csv_file:
    read = csv.reader(csv_file)
    matrix = [row for row in read]
X = pd.DataFrame(matrix)
X.head()


