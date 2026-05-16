import pandas as pd
from pandas.conftest import ascending
from pandas.core.algorithms import duplicated

df = pd.read_csv('avgIQpercountry.csv')

# print(df.info())

first_rows = df.head()
# print(first_rows)

country_data = df['Country']
# print(country_data)

subset = df[['Country', 'Average IQ']]

# print(subset)

filtered_df = subset[subset['Average IQ'] > 100]
# print(filtered_df)

null_mask = df.isnull()

null_count = null_mask.sum()

print("\nCount of null values in each column: ")
print(null_count)

df.dropna(inplace=True)

print("\nDataSet information after removing null value: ")
print(df.info)

duplicated_count = df.duplicated().sum()
print("\nCount of duplicated rows: ")
print(duplicated_count)

avg_ig_per_continent = df.grupeby('Continent')['Average IQ'],mean()
print(avg_ig_per_continent)

sorted_avg_iq_per_continent = avg_ig_per_continent.sort_values(ascending = False)
print(sorted_avg_iq_per_continent)

