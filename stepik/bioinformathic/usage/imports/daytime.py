import datetime


current_date = datetime.date(*map(int, input().split()))

past_days = int(input())

next_day = current_date + datetime.timedelta(past_days)

print(next_day.year, next_day.month, next_day.day)