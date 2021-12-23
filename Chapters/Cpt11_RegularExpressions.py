# Regular expressions aka "regex, regexp" 
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

#using regex
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): # ^ means has to be at the beggining
        print(line)

# wildcard characters
# . matches any character
# * means many times
# ^x.*: means Match the start of the line, match any chacacter, manytimes
#\S means match any non-whitespace character
