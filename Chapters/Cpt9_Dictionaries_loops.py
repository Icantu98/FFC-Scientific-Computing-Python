#Counting pattern

counts = dict()
print('Enter a line of text: ')
line = input('')    # get text from user

words = line.split()  #split each word

print('Words: ', words)  #print each word

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) +1 # puts words into a dictonary and counts them
print('Counts', counts)

##############

jjj = {'chuck':1, 'fred':42, 'jan':100}
for key in jjj:
    print(key,jjj[key])

# retreiving lists of Keys and Values
jjj = {'chuck':1, 'fred':42, 'jan':100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

# Two itteration variables
jjj = {'chuck':1, 'fred':42, 'jan':100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)
