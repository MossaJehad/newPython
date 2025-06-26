import pandas as pd

sales=[100, 99, 200, 120, 155]
label=['a', 'b', 'c', 'd', 'e']

series = pd.Series(sales, index=label)

employee_performance = {
	'Employee': ['Alaa', 'Mona', 'Khaled'],
	'Performance Score': [88, 92, 79]
}

df = pd.DataFrame(employee_performance)

######## SALES #######
print("Sales: ")
print(series)

####### HR #######
print("HR: ")
print(df)

