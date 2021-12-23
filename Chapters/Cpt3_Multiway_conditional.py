#Example 1
astr = 'Hello Bob' # all userinputs are strings
try:
    istr = int(astr) #tries to convert a string to an integer
except: #if it returns a traceback try this
    istr = -1 #sets istr to a value
print('First', istr)

astr = '123' #all userinputs are strings
try:
    istr = int(astr) #tries to convert a string to an integer
except: # if traceback try this
    istr = -1 #sets istr to a value
print('Second', istr)

#Example 2
rawstr = input('Enter a number: ') #input string fromuser
try:
    ival = int(rawstr) #checks if is a number
except:
    ival = -1 # if its not set to a value for error display later
if ival > 0:
    print('Good job!')
else: #display error
    print('Not a number')