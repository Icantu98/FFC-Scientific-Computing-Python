T2 = '1:03'
T1 = "11:55 AM"

Date = "Teusday"

Date = Date.lower()
 

days = {
'monday':0,
'teusday':1,
'wednessday':2,
'thrusday':3,
'friday':4,
'saturday':5,
'sunday':6}

print(days[Date])
#print(days[4])
day = 3
for dayx, num in days.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    if num == day:
        print(dayx)