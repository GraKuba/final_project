import pandas as pd
import numpy as np
import csv
import pprint

data_1 = pd.read_csv("/Users/kubagrabarczyk/Desktop/final_project_db.csv", on_bad_lines='skip')
# Does not work without "on_bad_lines='skip'"      ->      pandas.parser.CParserError: Error tokenizing data. C error:
print(data_1.head())

file_path = '/Users/kubagrabarczyk/Desktop/final_project_db.csv'
db = []
with open(file_path, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        db.append(line)

# pprint.pprint(db)

