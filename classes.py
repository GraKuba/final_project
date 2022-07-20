import pandas as pd
pd.options.mode.chained_assignment = None


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
        rounded_average = [round(num) for num in average]
        averages = dict(zip(position, rounded_average))
        return averages


class DataFrame(Functions):
    def average_income(self):
        dt = Functions.calculate_averages(self, 'Job Title')
        return [dt]

    def highest_paying_companies(self):
        dt = Functions.calculate_averages(self, 'Company Name')
        highest_values = sorted(dt, key=dt.get, reverse=True)[:3]
        dct = {}
        for value in highest_values:
            dct[value] = dt[value]
        return dct

    def salary_in_comparison(self):
        city_data = Functions.chosen_city_data(self)
        average_income = DataFrame.average_income(self)[0]
        highest_paying = DataFrame.highest_paying_companies(self)
        company_names = list(highest_paying.keys())
        highest_salaries = []
        for company_name in company_names:
            company_data = city_data.loc[city_data['Company Name'] == company_name]
            company_data['TotalSalary'] = company_data['Salary'] * company_data['Salaries Reported']
            salaries_reported = company_data.groupby('Job Title')['Salaries Reported'].sum()
            total_salary = company_data.groupby('Job Title')['TotalSalary'].sum()
            position = salaries_reported.index.tolist()
            amount = salaries_reported.tolist()
            print(amount)
            salary = total_salary.tolist()
            print(salary)
            average = [i / j for i, j in zip(salary, amount)]
            averages = company_name, dict(zip(position, [(sum((average)) / len(average))]))
            highest_salaries.append(averages)
        salary_comparison = []
        for idx in highest_salaries:
            for position_1 in average_income:
                for position in idx[1]:
                    if position_1 == position:
                        temp = {idx[0]: round((idx[1][position] / average_income[position_1]), 2)}
                        salary_comparison.append(temp)
        return salary_comparison

    def most_profitable_position(self):
        city_data = Functions.chosen_city_data(self)
        highest_payed_positions = city_data.loc[city_data.groupby('Job Title')['Salary'].idxmax(), :]
        company_name = highest_payed_positions['Company Name'].tolist()
        position = highest_payed_positions['Job Title'].tolist()
        salary = highest_payed_positions['Salary'].tolist()
        rounded_salary = [round(num) for num in salary]
        dct = {i: {j: k} for i, j, k in zip(company_name, position, rounded_salary)}
        return [dct]


data = DataFrame('Mumbai')

# AVERAGES
# positions_and_averages = data.average_income()
# print(positions_and_averages)

# HIGHEST PAYING COMPANIES
# highest_paying = data.highest_paying_companies()
# print(highest_paying)

# SALARY IN COMPARISON
# print(data.salary_in_comparison())

# MOST PROFITABLE POSITION AT A COMPANY
# print(data.most_profitable_position())


# todict = data.to_dict('records')
# for idx in todict:
#     print(idx)
