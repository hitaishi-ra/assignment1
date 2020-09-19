"""Assignment 1 (17/09/2020)

1)	Write a program to print your name, your place of stay, your stream of study, your college name in different lines.
"""
a = "Hitheshi"
b = "Pune"
c = "biotechnology"
d = "dypatil"
print(a)
print(b)
print(c)
print(d)
"""

2)	Raj was writing a python program to do the addition of multiple numbers. He chose one variable name as “def” to store a value of 5. But when he ran the script, the program gave an error. Could you provide a possible explanation?
"""
print("as 'def' is a keyword,we cant use it as a random variable ")

"""
3)	While running a program I was faced with an error several times.

if True:
print "Answer"
else:
print "No Answer"
This was the code that I was running. What can be the possible issue? 
"""
print("there was no paranthesis and indentation after the if and else statement")
"""

4)	What is the difference between single quote (’), double quotes (‘’) and triple quotes (‘’’)?
"""
print("you cannot use single inverted comma in between the sentence which is between single inerted comma and triiple inverted comma can use single and double inverted comma in the sentence" )
"""
5)	Write a program to print only the quotients of the following division:
	a)	19/2	(b)27/4	(c) 100/3	(d) 20/5
	
	"""
print(int(19/2))
print(int(27/4))
print(int(100/3))
print(int(20/5))

"""

6)	What modifications are required in above arithmetic operation so that we get the exact result. Explain your answer.
"""
print("we have to remove 'int' keyword so that we get the exact answer")

"""
7)	write a program to print the following sentence:
	“Python is an interactive language”
	Access the 5th, 11th, 13th , 18th and 23rd element. Which operator did you make use of? 
"""
a="Python is an interactive language"
print(a)
print(a[4],a[10],a[12],a[17],a[17],a[22])
print("square bracket[]")
"""
8)	Write a program to print a list containing
	A)	The name of 5 countries of your choice.
	B)	Access the 4th country name.
	C)	Print the first 2 countries.
	D)	Print the last two countries.
	E)	Update the list by adding 5 more countries and then print the updated list.
"""
countries = ['Japan','India',"china","germany","austria"]
print(countries[3])
print(countries[0:2])
print(countries[3:5])
countries +=['Italy','Sweden',"Iran","Iraq","Pakistan"]
print(countries)
"""
9)	Write a Python program to create a tuple.
"""
south_asia = ('Pakistan','India','Sri Lanka','China')
print(south_asia)
"""
10)	Write a Python program to create a tuple with different data types.
"""
numbers = (1,'two',3,'4',5)
print(numbers)
"""

11)	Write a Python program to add an item in a tuple.
"""
numbers += (7,8)
print(numbers)
"""

12)	Write a Python script to add a key to a dictionary.
"""
details = {'name' : 'Hiteshi','age':19}
print(details)
details['Gender']='F'
print(details)
"""

13)	Write a Python script to add a key to a dictionary."""