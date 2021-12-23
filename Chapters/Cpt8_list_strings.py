abc = 'With three words'
# .split() splits on spaces
stuff = abc.split() #splits each word into an item in a list
print(stuff)
print(stuff[0])

for w in stuff:
    print(w) #prints each word in new line

line = 'first;second;third'
line = line.split(';') # tells split() to split on ';'
print(line)

line = 'From stephen.marquad@uct.ac.za Sat Jan 5 09:14:16 2008'
line = line.split()
print(line)

for w in line:
    if "@" in w:
        print('Email address is:',w)

#easy way to get email
email = line[1]
email = email.split("@")
print('Host is', email[1])