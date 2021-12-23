s = 'Monty Python'
print(s[0:4]) # Colon operator means from 0 to 4 
print(s[6:7]) # Second number is one after end of slice
print(s[6:20]) # if you go past string chacters it will stop at end
print(s[:2]) # missing beggining = assumes beginning of string
print(s[8:]) # missing end = assums to end of string
print(s[:]) # empty colon assumes whole string

# String concatenation
a = 'Hello'
b = 'World'
print(a+b) # no space between strings

c = a + ' ' + b
print(c) #prints with space but have to add it

#logic 
fruit = 'banana'
'n' in fruit

#String library
greet = 'Hello Bob'
greet = greet.lower() # .lower at end of object make string all lower
print(greet)
print('Hello There'.lower())

# Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr) 

# Prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))

# Parsing and Extracting
data = 'stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
sppos = data.find(' ')
host = data[atpos+1 : sppos]
print('Email host is: ',host)