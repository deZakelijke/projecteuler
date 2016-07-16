# Problem 19 of Project Euler

# Monday is the first day of the week
sundays = 0
days = 2
months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

for  i in range(1,101):
    print(i+1900)
    days += months['January']
    if days%7 == 0:
        sundays += 1
    days += months['February']
    if i%4 == 0:
        days += 1
    if days%7 == 0:
        sundays += 1
    days += months['March']
    if days%7 == 0:
        sundays += 1
    days += months['April']
    if days%7 == 0:
        sundays += 1
    days += months['May']
    if days%7 == 0:
        sundays += 1
    days += months['June']
    if days%7 == 0:
        sundays += 1
    days += months['July']
    if days%7 == 0:
        sundays += 1
    days += months['August']
    if days%7 == 0:
        sundays += 1
    days += months['September']
    if days%7 == 0:
        sundays += 1   
    days += months['October']
    if days%7 == 0:
        sundays += 1   
    days += months['November']
    if days%7 == 0:
        sundays += 1   
    days += months['December']
    if days%7 == 0:
        sundays += 1   
print(sundays)

