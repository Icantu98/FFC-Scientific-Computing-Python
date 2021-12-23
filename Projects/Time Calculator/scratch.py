start = ["11:55 AM"]
duration = ['3:12']

#print(T1)
T1_hour = 1 # AM
T1_minute = 15
T2_hour = 2 # duration hour
T2_minute = 12 # duration min
meridiem = 0
Tf_hour = []
Tf_minute = []
meridiem_chg = 0 # need to change meridiem?

#### Current working code for T1

    if len(start) == 7:
        T1 = start[0:4] # T1 is a string at this point
        T1_hour = T1[0]
        T1_minute = T1[2:4]
    else:
        T1 = start[0:5]
        T1_hour = T1[0:1]
        T1_minute = T1[3:5]

    print('T1', T1_hour,T1_minute)
    print('T2: ',T2_hour,T2_minute)
    print('TF: ', Tf_hour,Tf_minute)
print(add_time("3:30 PM", "2:12")) # expected = "5:42 PM"
print(add_time("11:55 AM", "3:12")) # expected = "3:07 PM"
print(add_time("9:15 PM", "5:30")) # expected = "2:45 AM (next day)"
print(add_time("8:16 PM", "466:02")) # expected = "6:18 AM (20 days later)"
print(add_time("5:01 AM", "0:00")) # expected = "5:01 AM"

