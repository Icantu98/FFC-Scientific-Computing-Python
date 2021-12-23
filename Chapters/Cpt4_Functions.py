def thing(): # "def" starts a function to be remembered. "thing()" is what you called it
    #Things in the indention are whats inside the fucntion
    print('Hello') 
    print('Fun')

#how to call the user made function
thing()
print('Zip')
thing()

# Adding Arguments to functions

def lang_greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        return('Bonjour')  #this one will return as a value for function when called
    else:
        print('Hello')

lang_greet('en')
lang_greet('es')
lang_greet('fr')

def greet():
    return "Hello" #what shows up when the fucntion is all done

print(greet(), 'Glenn')
print(greet(), 'Sally') 
print(lang_greet('fr'), 'Cloe')
