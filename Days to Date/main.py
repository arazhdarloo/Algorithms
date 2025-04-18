days = int(input("enter days count: "))

year = days // 365
month = (days % 365) // 30
day = (days % 365) % 30

print(f"count of years = {year}, months = {month}, days = {day}")