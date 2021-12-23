fruit = 'banana'
letter = fruit[1] #gets 2nd letter of string
print(letter)
print(len(fruit))

x = 3
w = fruit[x - 1] #you can use expression as long as its and int
print(w)

#number out each character in a string
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#for loops are usually better for strings cause they will terminate themselves when it gets through the stirng
for letter in fruit:
    print(letter)

