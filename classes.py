import pandas as pd


class DataFrame:
    def __init__(self, city):
        self.city = city

    def chosen_city_data(self):
        df = pd.read_csv("/Users/kubagrabarczyk/Desktop/final_project_db.csv", delimiter=";", on_bad_lines='skip')
        city_data = df.loc[df['Location'] == self.city]
        return city_data

    def average_income(self):
        city_data = DataFrame.chosen_city_data(self)
        city_data['Total Salary'] = city_data['Salary'] * city_data['Salaries Reported']
        salaries_reported = city_data.groupby('Job Title')['Salaries Reported'].sum()
        total_salary = city_data.groupby('Job Title')['Total Salary'].sum()
        position = salaries_reported.index.tolist()
        amount = salaries_reported.tolist()
        salary = total_salary.tolist()
        average = [i / j for i, j in zip(salary, amount)]
        averages = dict(zip(position, average))
        return averages

    def highest_paying_companies(self):
        ...

    def salary_in_comparison(self):
        ...

    def most_profitable_position(self):
        ...

        # todict = city_data.to_dict('records')
        # for idx in todict:
        #     print(idx)


data = DataFrame('New Delhi')

positions_and_averages = data.average_income()
print(positions_and_averages)
