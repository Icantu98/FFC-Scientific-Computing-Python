name = input('Enter file name: ')
try:
    fhand = file = open(name, encoding="utf8")
except:
    print('File cant be opened. Check file extention or name')
    quit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) +1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print('Biggest word: ', bigword,'Highest count', bigcount)
