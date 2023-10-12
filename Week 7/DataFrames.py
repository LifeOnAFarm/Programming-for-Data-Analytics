# Python program
# Author: Seamus de Cleir

# Import the pandas library
import pandas as pd

# Create a dataframe from a csv file with no index column
df = pd.read_csv('Automobile_data.csv', index_col = 0)

# Print the first 5 rows of the dataframe and last 5 rows of the dataframe
print(df.head(5))
print(df.tail(5))

# Print the most expensive car's company name and price
selRow = df.nlargest(1, 'price')
print(selRow[['company', 'price']])

# Print all Toyota cars details
selRow = df.loc[df['company'] == 'toyota']
print(selRow)

# Count total cars per company
print(df['company'].value_counts())

# Sort all cars by Price column
print(df.sort_values(by = ['price']))

# Concatenate two data frames using the following conditions:
# Create two data frames using the following two Dicts, Concatenate those two data frames and create a key for each data frame.

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price':[23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500 , 58900]}
df1 = pd.DataFrame.from_dict(GermanCars)
df2 = pd.DataFrame.from_dict(japaneseCars)
df3 = pd.concat([df1, df2], keys = ['Germany', 'Japan'])
print(df3)


