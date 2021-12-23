# newline
stuff = 'Hello\nWorld' # \n moves text to a new line
#print(stuff)

# File handle as a sequence
xfile = open('Test_data.txt') #create a handle for the data
for thing in xfile: #for loop to get out each line of data in the file
    print(thing) #print each line

# Counting lines in a file
fhand = open('Test_data.txt')
count = 0                       #sets count to 0
for line in fhand:
    count = count + 1
print('line count:', count)

# Reading the *Whole* file
fhand = open('Test_data.txt')
inp = fhand.read()     # .read() puts the data in ONE big string
print(len(inp))        # len() tells you how many char in a string
print(inp[:20])         # prints first 20 char

# Searching through a file
fhand = open('Test_data.txt')
for line in fhand:
    if line.startswith('it'): # .startwith('') seaches for a line that starts with something
        print(line)
        #Notice extra line that was pulled from data

fhand = open('Test_data.txt')
for line in fhand:
    line = line.rstrip()       #strips white space from data
    if line.startswith('it'): # .startwith('') seaches for a line that starts with something
        print(line)

# Skipping with continue
fhand = open('Test_data.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('it'): # .startwith('') seaches for a line that starts with something
        continue
    print(line)

# using "in"
fhand = open('Test_data.txt')
for line in fhand:
    if not 'import' in line: 
        continue
    print(line)

# Getting file names from User input
fname = input('Enter file name: ')
try:
    fhand = open(fname) #checks if file exists
except:
    print('File name cant be opened. Check file extension',fname) # Tells you if not
    quit()
count = 0
for line in fhand:
    line = line.rstrip()
    if 'Gender' in line: #Do something intersting if 'Gender' exists
        print(line)
        print('REEE')
        continue
    print(line)
