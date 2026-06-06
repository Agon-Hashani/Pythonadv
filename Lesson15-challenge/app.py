import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather_tokyo_data.csv')

print(df.info())

df['full_date'] = pd.to_datetime(df['year'].astype(str) + '/' + df["day"], format='%Y/%m/%d')

df['temperature'] = df['temperature'].str.replace(r'\([^)]*\)', "", regex=True)

df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

df = df.dropna()

df = df.sort_values(by="full_date")

print(df.info())

mean_temperature = df['temperature'].mean()
print(f"The average temperature for the entire dataset is {mean_temperature} C")

mean_temp_by_month = df.groupby(df["full_date"].dt.month)["temperature"].mean()
print("\n The mean temperature for each month is:\n", mean_temp_by_month)

plt.figure(figsize=(10, 6))
plt.bar(mean_temp_by_month.index, mean_temp_by_month.values)
plt.title('Mean Temperature by Month')
plt.xlabel("Month")
plt.ylabel('Mean Temperature (°C)')
plt.xticks(range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


hottest_day = df[df["temperature"] == df['temperature'].max()]
print(f"\n The hottest day recorded:\n{hottest_day}")

Coldest_day = df[df["temperature"] == df['temperature'].min()]
print(f"\n The coldest day recorded:\n{Coldest_day}")

plt.figure(figsize=(12, 6))
plt.plot(df['full_date'], df['temperature'])
plt.title('Temperature Trends')
plt.xlabel("Date")
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

df['season'] = df['full_date'].dt.month.apply(get_season)

seasonal_temperature = df.groupby('season')['temperature'].mean()

plt.figure(figsize=(10, 6))
plt.plot(seasonal_temperature.index, seasonal_temperature.values, marker = 'o', linestyle='-', color='skyblue', linewidth=2)
plt.title('Season Average Temperature')
plt.xlabel("Season")
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()