import datetime

current_datetime = datetime.datetime.now()

print("Year: ", current_datetime.year)
print("Month: ", current_datetime.month)
print("Day: ", current_datetime.day)
print("Hour: ", current_datetime.hour)
print("Minute: ", current_datetime.minute)
print("Second: ", current_datetime.second)
print("Microsecond: ", current_datetime.microsecond)

current_date = datetime.datetime.now().date()

print("Date: ", current_date)

current_time = datetime.datetime.now().time()

specific_time = datetime.time(12, 30, 0)

print("Time: ", specific_time)

formatted_date = current_datetime.strftime('%d-%m-%Y %H:%M:%S')
print(formatted_date)

duration = datetime.timedelta(days=5, hours=3)

new_date = current_date + duration

print(new_date)


utc_time = datetime.datetime.now(datetime.timezone.utc)
print("Current UCT time: ", ut)