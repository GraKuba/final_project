import pandas as pd
import functools


class DataFrame:
    def __init__(self, city):
        self.city = city

    def chosen_city_data(self):
        df = pd.read_csv("/Users/kubagrabarczyk/Desktop/final_project_db.csv", delimiter=";", on_bad_lines='skip')
        city_data = df.loc[df['Location'] == self.city]
        return city_data

    def average_income(self):
        city_data = DataFrame.chosen_city_data(self)
        # number = city_data['Job Title'].value_counts()
        # positions = number.index.tolist()
        # amounts = number.tolist()
        # positions_and_amounts = dict(zip(positions, amounts))
        job_titles = []
        salaries = []
        for idx, row in city_data.iterrows():
            job_title = row['Job Title']
            job_titles.append(job_title)
            salary = row["Salary"]
            salaries.append(salary)
        positions_and_salaries = dict(zip(job_titles, salaries))
        return positions_and_salaries


data = DataFrame('Pune')

positions_and_averages = data.average_income()
print(positions_and_averages)

