import math
from datetime import date

# Get dates
today = date.today()
birth = date(2020, 8, 20)
due_date = date(2020, 9, 16)

# Calculate chronological age in weeks + days
day_age = today - birth
week_age = math.floor(day_age.days / 7)
weekday_remainder = day_age.days % 7

# Calculate chronological age in months (1 month ~ 30.417 days)
month_age = round(day_age.days / 30.417, 2)

# Calculate adjusted age in weeks + days
adjusted_days = today - due_date
adjusted_weeks = math.floor(adjusted_days.days / 7)
adjusted_remainder = adjusted_days.days % 7

# Calculate adjusted age in months
adjusted_months = round(adjusted_days.days / 30.417, 2)

# Print 'age report'
print("\nADELINE & JAMES AGE REPORT:\n")
print(f" * Adeline and James are {week_age} weeks and {weekday_remainder} day(s) old.")
print(f"   - This amounts to {day_age.days} total days.")
print(f"   - This is equivalent to {month_age} months.\n")
print(f" * Their adjusted age is {adjusted_weeks} weeks and {adjusted_remainder} day(s).")
print(f"   - This is equivalent to {adjusted_months} months.\n")
