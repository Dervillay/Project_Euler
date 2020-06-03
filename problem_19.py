from math import floor

# Find day of week using Zeller's rule:
# http://mathforum.org/dr.math/faq/faq.calendar.html#:~:text=Here's%20the%20formula%3A,29%2C%202064%20as%20an%20example.
# Where 0 is Sunday, 1 is Monday, ... 6 is Saturday
def day_of_week(day, month, year):
    if month > 2:
        month -= 2
    else:
        month += 10

    k = day
    m = month
    D = int(str(year)[-2:])
    C = int(str(year)[:2])

    if m > 10:
        D -= 1

    f = k + floor((13*m-1)/5) + D + floor(D/4) + floor(C/4) - 2*C
    f %= 7

    return f


# Sum num of Sundays on the first of each month from 1901 to 2000
sum = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if day_of_week(1, month, year) == 0:
            sum += 1

print(sum)



