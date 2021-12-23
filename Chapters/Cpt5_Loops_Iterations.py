# Indefinate loop
while True: # infinate loop with a break somewhere to escape it
    line = input('> ') #gets user to input a string
    if line[0] == '#': # if string has a "#" as first character it wont print
        continue        # Goes back to line 2
    if line == 'launch': # if input is 'quit'
        break           # stops while loop
    print(line)
print('Starting countdown.') # prints after while loop is killed

# Definate loop
for i in [5,4,3,2,1]: #list of things to do
    print(i)          # 5 things in list will print 5 times
print('Blastoff!')


friends = ['Daniel','Joel','Joe'] #makes a list of thins in a variable

for n in friends: # use variable n for the "for" loop for every item in variable friends
    print('Happy New Year', n) # outputs each time n is used for an item in friends
print('Done.')  
