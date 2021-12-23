def add_time(start, duration, Date = ''):
    new_time = '!'

    T1_hour = [] # Start hour
    T1_minute = [] # Start minute
    T2 = duration # Duration time
    T2_hour = [] # Duration hour
    T2_minute = [] # Duration minute
    meridiem = [] # gets the AM/PM of given time ####   0 = am : 1 = pm
    Tf_hour = [] # final time hour
    Tf_minute = [] # final time minute
    # Checks for AM/PM
    if start.__contains__('A') == True:
        meridiem = 0 # means AM
    else:
        meridiem = 1 # means PM
    # Gets length to set T1 correctly
    T1_hour = start[0:len(start)-6]
    T1_minute = start[len(start)-5:len(start)-3]
    # Gets length of duration to set T2 correctly
    T2_hour = T2[0:len(T2)-3]
    T2_minute = T2[len(T2)-2:]
    # Do Time additions
    # hours
    Tf_hour = int(T1_hour) + int(T2_hour) 
    # minutes
    Tf_minute = int(T1_minute) + int(T2_minute)

    # Time adgustment base 60
    if Tf_minute >= 60:
        Tf_minute = Tf_minute - 60
        Tf_hour = Tf_hour + 1
    if Tf_minute < 10: # sets formating for mintue
        Tf_minute = "{0:0=2d}".format(Tf_minute) # makes it so if its a single number adds a 0 before it
    
    meridiem_chg = 0 # number of meridiem changes
    day_chg = 0 # number of days gone past if asked for
    if Tf_hour >= 12:
        meridiem_chg = int(Tf_hour / 12) # ok
        Tf_hour =  Tf_hour %12 # Remainder is T_f hour
        meridiem = meridiem + meridiem_chg # to calculate AM/PM and days past
        if Tf_hour == 0:
            Tf_hour = 12
        if meridiem > 1:
            day_chg = int(meridiem/2)
            meridiem = meridiem%2 # Remainder gives 0/1 = AM/PM
    if meridiem == 1:
        meridiem = " PM"
    else:
        meridiem = " AM"
    ### IF DATE IS GIVEN
    day = ''
    days_dic = {
    'monday':0,
    'tuesday':1,
    'wednesday':2,
    'thursday':3,
    'friday':4,
    'saturday':5,
    'sunday':6}
    if len(Date)>0:
        x = days_dic[Date.lower()] # current date
        y = day_chg%7 # remainder is how many days past
        x = (x+y)%7 # just incase its into new week
        for name, num in days_dic.items(): # to get the date string out of the dictoanry 
            if num == x:
                day = name
    # OUTPUT CORRECT STRING ON DATE STUFF  
    if day_chg == 0:
        day_chg = ""
    elif day_chg == 1:
        day_chg = ' (next day)'
    else: 
        day_chg = ' (' + str(day_chg) + ' days later)'

    day = day.capitalize()
    # putting final time together
    Tf_hour = str(Tf_hour)
    Tf_hour = Tf_hour + ':'
    Tf_minute = str(Tf_minute)
    if len(Date) == 0:
        new_time = Tf_hour + Tf_minute + meridiem + day_chg
    else:
        new_time = Tf_hour + Tf_minute + meridiem +', '+ day + day_chg
    return new_time

print(add_time("8:16 PM", "466:02", "tuesday")) # expected = "6:18 AM (20 days later)"
print(add_time("2:59 AM", "24:00")) #  expected = "2:59 AM (next day)"
print(add_time("11:59 PM", "24:05")) #expected = "12:04 AM (2 days later)"
print(add_time("11:59 PM", "24:05", "Wednesday")) #expected = "12:04 AM, Friday (2 days later)"
print(add_time("11:59 PM", "24:05")) # expected = "12:04 AM (2 days later)"
print(add_time("11:40 AM", "0:25")) # expected = "12:05 PM"
#print('expected = "12:05 PM"')
print("made it to the end") 