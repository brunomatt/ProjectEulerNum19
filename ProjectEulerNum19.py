#You are given the following information, but you may prefer to do some research for yourself.
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
answers = []
leap_days = 0
for k in range(1901, 2001):
    if k % 4 == 0:
        leap_days += 1
total_days = (365 * 100) + 364 + leap_days # from 1 Jan 1900 to 31 Dec 2000
days_since_start = [k for k in range(0, total_days + 1)]

for i in range(1,total_days, 7):
    days_since_start[i] = "M"
for i in range(2,total_days, 7):
    days_since_start[i] = "T"
for i in range(3,total_days, 7):
    days_since_start[i] = "W"
for i in range(4,total_days, 7):
    days_since_start[i] = "R"
for i in range(5,total_days, 7):
    days_since_start[i] = "F"
for i in range(6,total_days, 7):
    days_since_start[i] = "S"
for i in range(7,total_days, 7):
    days_since_start[i] = "U"

days_since_start[-1] = "S"

twentieth_century = days_since_start[366:]

firsts_of_month = [366]

def pass_year():
    if len(firsts_of_month) > 2:
        firsts_of_month.append(firsts_of_month[-1] + 31)  # Dec
    firsts_of_month.append(firsts_of_month[-1] + 31) # Jan
    firsts_of_month.append(firsts_of_month[-1] + 28) # Feb
    firsts_of_month.append(firsts_of_month[-1] + 31) # March
    firsts_of_month.append(firsts_of_month[-1] + 30) # April
    firsts_of_month.append(firsts_of_month[-1] + 31) # May
    firsts_of_month.append(firsts_of_month[-1] + 30) # June
    firsts_of_month.append(firsts_of_month[-1] + 31)  # July
    firsts_of_month.append(firsts_of_month[-1] + 31)  # Aug
    firsts_of_month.append(firsts_of_month[-1] + 30)  # Sept
    firsts_of_month.append(firsts_of_month[-1] + 31)  # Oct
    firsts_of_month.append(firsts_of_month[-1] + 30)  # Nov

def pass_leap_year():
    firsts_of_month.append(firsts_of_month[-1] + 31) # Dec
    firsts_of_month.append(firsts_of_month[-1] + 31) # Jan
    firsts_of_month.append(firsts_of_month[-1] + 29) # Feb on leap year
    firsts_of_month.append(firsts_of_month[-1] + 31) # March
    firsts_of_month.append(firsts_of_month[-1] + 30) # April
    firsts_of_month.append(firsts_of_month[-1] + 31) # May
    firsts_of_month.append(firsts_of_month[-1] + 30) # June
    firsts_of_month.append(firsts_of_month[-1] + 31)  # July
    firsts_of_month.append(firsts_of_month[-1] + 31)  # Aug
    firsts_of_month.append(firsts_of_month[-1] + 30)  # Sept
    firsts_of_month.append(firsts_of_month[-1] + 31)  # Oct

for i in range(1,26): #this runs through 1901 - 2000
    pass_year()
    pass_year()
    pass_year()
    pass_leap_year()

pass_year() # runs through 2000 up until 31 Dec 2000

for i in firsts_of_month:
    if twentieth_century[i] == "U":
        answers.append(i)

print(len(answers))