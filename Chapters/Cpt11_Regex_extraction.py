import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # any stirng that is 1 or more digits 
print(y) # prints 2 19 42

y = re.findall('[AEIOU]+',x) #one or more uppercase AEIOU
print(y) # none match

x = 'From: Uisng the : character'
y = re.findall('^F.+:',x) # First character F, one or more characters last character is :
print(y) # greedy match gives you longest string
y = re.findall('^F.+?:',x) # ? means non greedy. Choose shorter of the strings
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\\S+@\\S+',x) #at least one non-whitespace character, @ inbetween, then at least one non-whitespace character 
print(y)
y = re.findall('From (\\S+@\\S+)',x) #fine tuning matches with from but only returns inside ()
print(y)
y = re.findall('@([^ ]*)',x) # look untill youfind @ extratct stuff in (), [] means non-blank chracter, * many of them
print(y)
y = re.findall('From .*@([^ ])*',x)
print(y)

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1: 
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

x = 'We just received $10.00 for cookies.'
y = re.findall('\\$[0-9.]+',x) # \$ to look for $ symbol in string 
print(y)