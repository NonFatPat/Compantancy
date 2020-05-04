# declare 3 variables with one assignment statement and assign each one an integer value
a, b, c = 1, 2, 3

# convert each of your previous variables to float objects
float(a)
float(b)
float(c)

# convert each of your previous variables to string objects
str(a)
str(b)
str(c)

# Print the result of dividing 783.56 by 123.2 and ensure that the answer results in an integer
# expected outcome: 6
result = 783.56/123.2
print(int(result))

# Determine if 2019 is a leap year and print the result.
# expected outcome: 3
year = 2019 % 4
print(year)

# print the calculated length of myFirstString.
# expected outcome: 35
myFirstString = 'I love working with Python so much!'
print(len(myFirstString))

# Create a string value and print it with the first letter of each word capitalized using a Python method.
cap = 'the brown fox'
print(cap.title())

# Create a string value and determine if the string consists of only lowercase characters. Print the results.
# expected outcome: True or False
cap = 'the brown fox'
print(cap.islower())

# Use the given variable to construct a python statement that counts how many times the word pizza is used. Print the final count.
# expected outcome: 3
commercial = 'In the Little Ceasars pizza commercial the character says, "pizza, pizza"!'
print(commercial.count('pizza'))

# Use the given username and phone to create a message that lets the user know that you will be calling
# at a specified number for your appointment. Use the format method to insert data into the printed message.
# expected outcome: Hi, Allen. I will call you at 888-555-0011 for our appointment.
username = 'Allen'
phone = 8885550011
phones =str(phone)
num = ('{}-{}-{}'.format(phones[:3], phones[3:6], phones[6:]))
print('Hi, %s. I will call you at %s for our appointment.' % (username, num))






