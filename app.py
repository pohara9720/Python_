# VIRTUAL ENV
# virtualenv -p python3 .


from math import * # need this for more advanced math functions
from string import Template #for template strings
from Student import Student,Question

# STRINGS
print('hello')
phrase = 'hello Patrick'
# capitalize all
print(phrase.upper())
# lowercase all
print(phrase.lower())
# is it all upper?
print(phrase.isupper())
# is it all lower?
print(phrase.islower())
# How many characters
print(len(phrase))
# specific character
print(phrase[0])
# where is specific character?
print(phrase.index('l'))
# replace values 1 is value to remove 2 is value to be inserted
print(phrase.replace('hello','goodbye'))



# NUMBERS
number = 2.891
numbers = [1,2,3,4,4,5]
print(2.910)
# convert to string
print(str(number))
# absolute value
print(abs(-10)) 
#exponents 
print(pow(4,2))
# highest number in array
print(max(numbers))
# lowest number in array
print(min(numbers))
#round 
print(round(number))
#rounds down automatically
print(floor(number))
#rounds up automatically
print(ceil(number))
#square root
print(sqrt(81))

# Getting input from a user
# age = input('How old are you? ')
# print('You are ' + str(age))
# temp = Template('You are $age ! Nice to meet you')
# temp.substitute(age=age)
# print(temp)

# num1 = input('Enter a number: ')
# num2 = input('Enter another number: ')
# result = num1 + num2
# print result


#LISTS

friends = ['Steve','Ryan','Matt','Chris','Treye']
lucky_numbers =[12,43,90,3,32,76]
#access from back of array
print(friends[-1])
#length of array
print(len(friends))
#access from point of array onwards 
print(friends[2:])
# access all between values but not including last
print(friends[1:4])
# extend array similar to .concat() js
friends.extend(lucky_numbers)
print(friends)
# append similar to .push() js
friends.append('Sophie')
print(friends)
#insert param 1 index pos param 2 is value to be inserted
friends.insert(1,'Joson')
friends.insert(4,'Sophie')
print(friends)
#Remove values from array
friends.remove('Joson')
print(friends)
#How many recurrences are in array
print(friends.count('Sophie'))
#pop item off of last item in list
friends.pop()
print(friends)
#What index is value?
print(friends.index('Treye'))
print(friends.index(90))
#sort ascending
lucky_numbers.sort()
print(lucky_numbers)
#sort desceding
lucky_numbers.reverse()
print(lucky_numbers)
# copy array
clone = friends.copy()
print(clone)
# Empty array
friends.clear()
print(friends)

#TUPLES

#Tuples are immuntable cant be changed or modified
coordinates = (4,5)


#FUNCTIONS
def say_hello(name,age,location):
	print('Hello ' + name + ' you are ' + str(age) + ' and live in ' + location)

say_hello('Patrick',25,'Arizona')

def cube(x):
	return pow(x,3)

print(cube(3))

is_male = True
is_tall = True

if is_male:
	print('You are a male')
else:
	print('You are a female')

if is_male or is_tall:
	print('You are a male and or tall')
else:
	print('print you are neither male nor tall')

if is_male and is_tall:
	print('You are a male and tall')
else:
	print('You are not a male or tall')

if is_male and is_tall:
	print('You are a male and or tall')
elif is_male and not(is_tall):
	print('You are a short male')
elif not(is_male) and is_tall:
	print('You are a tall female')
else:
	print('print you are neither male nor tall')


def max_num(x,y,z):
	if x >= y and x >= z:
		return x
	elif y >= x and y >= z:
		return y
	else:
		return z

print(max_num(10,2,60))


# first = float(input('Enter number 1: '))
# operator = input('Enter operator: ')
# second = float(input('Enter number 2: '))

# if operator == '+':
# 	print(first + second)
# elif operator == '-':
# 	print(first - second)
# elif operator == '*':
# 	print(first * second)
# else:
# 	print(first / second)


#DICTIONARIES

#keys can be anything number string etc
# cannot be variable
months = {
	'Jan':'January',
	'Feb':'February',
	'Mar':'March',
	'Apr':'April',
	'May':'May',
	'Jun':'June',
	'Jul':'July',
	'Aug':'August',
	'Sep':'September',
	'Oct':'October',
	'Nov':'November',
	'Dec':'December'
}

# access a value
print(months['Nov'])
#access with get and give a default second param is default
#print(months['Apples']) #will break application
print(months.get('Apples','Not a valid key'))

i = 1

while i <= 10:
	print('Smaller than 10 ' + str(i))
	i = i + 1
print('Done with loop')

secret_word = 'giraffe'
guess = ''
guess_count = 0
guess_limit = 3
game_over = False

# while guess != secret_word and not(game_over):
# 	if guess_count < guess_limit:
# 		guess = input('Enter guess: ')
# 		guess_count += 1
# 	else:
# 		game_over = True

# if game_over:
# 	print('Game over you lose')
# else:
# 	print('You Win')

print(clone)
# can loop a string
for x in 'Patrick':
	print(x)
# normal looping of array
for x in clone:
	print(x)
# looping with a range DOES NOT INCLUDE THAT LAST NUMBER
for x in range(20,50):
	print(x)
# loop with indexes 
for x in range(len(clone)):
	print(clone[x])


#2 Dimensional lists

num_grid = [
	[1,2,3],
	[4,5,6],
	[7,8,9],
	[0]
]
print(num_grid[0][2])

for row in num_grid:
	for x in row:
		print(x)

def bomp(phrase):
	trans = ''
	for x in phrase:
		if x.lower() in 'ck':
			trans = trans + 'b'
		else:
			trans = trans + x
	return trans

print(bomp('We out here in compton keeping it cool'))

'''
This is how you comment out a bunch of shit
This is how you comment out a bunch of shit
This is how you comment out a bunch of shit
This is how you comment out a bunch of shit
but just use hashtags anyways
'''

# There is built in except cases for error catching 
try:
	# value = 10 / 0
	numeral = int(input('Enter number: '))
	print(numeral)
except ZeroDivisionError as err:
	#print own error
	print('Cant divide by zero!')
	#print the actual err
	print(err)
except ValueError as err:
	print('Invalid input')
	print(err)

#Opening files
#modes
# r = read
# w = write
# a = append # can only add to the end of file
# r+ = read and write
#open will open file
file = open('people.txt','r')
for person in file.readlines():
	print(person)
#readable() returns a boolean if you can read file
print(file.readable())
#read() gives info
print(file.read())
#readline() will read top line and consecutive lines after if used again
print(file.readline())
#readlines will put all lines into an array
print(file.readlines())
#shut access to file
file.close()

#writing to a file
file = open('people.txt','a')
file.write('Toby - Human Resources')

#can open html here
# file.open('index.html','w')
# file.write('<h1>Hello</h1>')

## built in modules
# https://docs.python.org/3/py-modindex.html

#CLASSES AND OBJECTS

#refer to student class in ./Student.py

student_1 = Student('Jim','Architect',3.5,True,['Building 101','Building 102','Building 201'])
print(student_1)
print(student_1.name)
print(student_1.major)
print(student_1.classes)

print(student_1.on_honor_roll())

question_prompts = [
	'What color are apples?\n(a)Red\n(b)Purple\n(c)Orange\n\n',
	'What color are bananas?\n(a)Teal\n(b)Magenta\n(c)Yellow\n\n',
	'What color are strawberries?\n(a)Yellow\n(b)Red\n(c)Blue\n\n',
]

questions = [
	Question(question_prompts[0],'a'),
	Question(question_prompts[1],'c'),
	Question(question_prompts[2],'b')
]



def run_test(qs):
	score = 0
	for x in qs:
		ans = input(x.prompt)
		if ans == x.answer:
			score += 1
	print('You got ' + str(score) + ' out of ' + str(len(qs)))

run_test(questions)



