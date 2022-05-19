import pandas as pd


class Functions:
    def __init__(self, city):
        self.city = city

    def chosen_city_data(self):
        df = pd.read_csv("/Users/kubagrabarczyk/Desktop/final_project_db.csv", delimiter=";", on_bad_lines='skip')
        city_data = df.loc[df['Location'] == self.city]
        return city_data

    def calculate_averages(self, group_by):
        city_data = Functions.chosen_city_data(self)
        city_data['Total Salary'] = city_data['Salary'] * city_data['Salaries Reported']
        salaries_reported = city_data.groupby(group_by)['Salaries Reported'].sum()
        total_salary = city_data.groupby(group_by)['Total Salary'].sum()
        position = salaries_reported.index.tolist()
        amount = salaries_reported.tolist()
        salary = total_salary.tolist()
        average = [i / j for i, j in zip(salary, amount)]
        averages = dict(zip(position, average))
        return averages


class DataFrame(Functions):
    def average_income(self):
        dt = Functions.calculate_averages(self, 'Job Title')
        return dt

    def highest_paying_companies(self):
        dt = Functions.calculate_averages(self, 'Company Name')
        highest_values = sorted(dt, key=dt.get, reverse=True)[:3]
        dct = {}
        for value in highest_values:
            dct[value] = dt[value]
        return dct

    def salary_in_comparison(self):
        ...

    def most_profitable_position(self):
        ...

        # todict = city_data.to_dict('records')
        # for idx in todict:
        #     print(idx)


data = DataFrame('Bangalore')

# AVERAGES
# positions_and_averages = data.average_income()
# print(positions_and_averages)

# HIGHEST PAYING COMPANIES
highest_paying = data.highest_paying_companies()
print(highest_paying)
