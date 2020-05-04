# ---- Math Module --- ##
import math

# use the math module to determine the factorial of the number 7 and print the result
# expected outcome: 5040
print(math.factorial(7))

# use the math module to determine the square root of the number 27 and print the result
# expected outcome: 5.196152422706632
print(math.sqrt(27))

# use the math module to determine the largest integer less than or equal to 15.87 and print the result
# expected outcome: 15
print(math.floor(15.87))


# use the math module to determine the smallest integer integer greater than or equal to 15.87 and print the result
# expected outcome: 16
print(math.ceil(15.87))

# use the math module to determine e to the power of 4
# expected outcome: 54.598150033144236
print(math.exp(4))



## ---- Random Module --- ##
import random

# use the random module to print a random integer between 2 and 20, exclusive
print(random.randrange(2, 20))

# use the random module to print a random number from the range 1 to 100, inclusive
print(random.randrange(1, 100+1))

# use the random module to return a random floating point number
print(random.uniform(1 , 2))

# Create a list of 6 words. Then use the random module to return a random element from that list.
names = ['Dana', 'Cemal', 'Jessica', 'Mike', 'Billy', 'David']
print(random.choice(names))


## ---- OS Module --- ##
import os

# use the os module to create a hard link to C://myfile.txt at C://myPython/myfile.txt
# os.link('C://myfile.txt', 'C://myPython/myfile.txt')

# use the os module to delete the file C://myfile.txt
# os.remove('C://myfile.txt')

# use the os module to return the current working directory
# os.system('pwd')

# use the os module to change the root directory to C://home/
# os.chdir('C://home/')


## ---- Datetime Module --- ##
import datetime
x = datetime.datetime.now()
# use the datetime module to print the current year
print(x.year)

# use the datetime module to print the current month
print(x.month)

# use the datetime module to print the current day
print(x.day)

# use the datetime module to print the total number of seconds in 4 days
# expected outcome: 345600.0

d1 = datetime.timedelta(days=4)
print(d1.total_seconds())

# print today's date one year from now
d2 = datetime.datetime.now() + datetime.timedelta(days=365)
print(d2)

## ---- Lookup  --- ##
# You need to use the datetime library to account for time zone adjustments, but aren't sure which method(s) to use.
# You are taking an exam and can't google it. What Python function will allow you to look up and locate the method?
# Write your code below:
print(dir(datetime))
