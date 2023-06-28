number_of_pages = int(input())
pages_hour = int(input())
number_of_days = int(input())

total_reading_time = number_of_pages // pages_hour
required_hours_per_day = total_reading_time // number_of_days

print(required_hours_per_day)