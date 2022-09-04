import time

# List of special words
special_words = ['good', 'great', 'amazing', 'excellent', 'fine', 'pleasing', 'capital', 'acceptable', 'divine', 'splendid', 'satisfactory', 'superb', 'awesome'] 

name = str(input('Hi, who are you? '))

print ('Hello ' + name)

feeling = input ('How are you today? ')

print ('You are feeling ' + feeling + ' today!')

if feeling in special_words:
    print ('Good for you!')

maths = input ('Can I help you with a maths problem? ')

if maths == 'yes':
    operation = input ('Which of the following can I help you with:' '\n + \n - \n x \n / \n')

else:
    print ('Bye! ' + name)
    exit()

if operation == '+':
    plus1 = input('Please enter your first number: ')
    plus2 = input('Please enter your second number: ')
    plus1int = int(plus1)
    plus2int = int(plus2)
    print (name + str(', the answer is:') , (plus1int + plus2int))

elif operation == '-':
    minus1 = input('Please enter your first number: ')
    minus2 = input('Please enter your second number: ')
    minus1int = int(minus1)
    minus2int = int(minus2)
    print (name + str(', the answer is:') , (minus1int - minus2int))

elif operation == 'x':
    times1 = input('Please enter your first number: ')
    times2 = input('Please enter your second number: ')
    times1int = int(times1)
    times2int = int(times2)
    print (name + str(', the answer is:') , (times1int * times2int))

elif operation == '/':
    div1 = input('Please enter your first number: ')
    div2 = input('Please enter your second number: ')
    div1int = int(div1)
    div2int = int(div2)
    print (name + str(', the answer is:') , (div1int / div2int))
    
else:
    exit()
