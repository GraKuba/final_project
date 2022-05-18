import pandas as pd
import pprint

df = pd.read_csv("/Users/kubagrabarczyk/Desktop/final_project_db.csv", delimiter=";", on_bad_lines='skip')
# Does not work without "on_bad_lines='skip'"      ->      pandas.parser.CParserError: Error tokenizing data. C error:

#
# class DataFrame:
#     def __init__(self, city):
#         self.city = city
#
#     def chosen_city_data(self):
#         df = pd.read_csv("/Users/kubagrabarczyk/Desktop/final_project_db.csv", delimiter=";", on_bad_lines='skip')
#         return df[(df['Location'] == self.city)]
#
#     def list_available_positions(self):
#         ...
#
# city_data = DataFrame('New Delhi')
# print(city_data.chosen_city_data())
#
#
# city_data = df.loc[df['Location'] == 'New Delhi']

# job_positions = []
# for idx, row in city_data.iterrows():
#     if row['Job Title'] not in job_positions:
#         job_positions.append(row['Job Title'])
#
# print(job_positions)

print(df.columns)
number = df['Job Title'].value_counts()
print(number)

job_positions = []
        for idx, row in city_data.iterrows():
            if row['Job Title'] not in job_positions:
                job_positions.append(row['Job Title'])