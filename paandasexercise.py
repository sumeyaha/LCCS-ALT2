import statistics
import pandas


# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('pandasexercise.csv')

# Filter out the column, value_eur
# Compute and display the mean

Amt_1 = df['Amt_1']
print(Amt_1)
mean_value_Amt_1 = round(statistics.mean(Amt_1), 2)
print(mean_value_Amt_1)

Amt_2 = df['Amt_2']
print(Amt_2)
mean_value_Amt_2 = round(statistics.mean(Amt_2), 2)
print(mean_value_Amt_2)

Amt_3 = df['Amt_3']
print(Amt_3)
mean_value_Amt_3 = round(statistics.mean(Amt_3), 2)
print(mean_value_Amt_3)



 




