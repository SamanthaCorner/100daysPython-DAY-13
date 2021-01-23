"""
100 days of Python course
DAY 13
"""

# code below contains deliberate errors: identify them and add comments
# thereafter uncomment the block, correct then run and see that it executes

number = int(input("Which number do you want to check?"))

# common error to compare something in an if statement use "==" not "="
if number % 2 = 0:
    print("This is an even number.")
else:
    print("This is an odd number.")



year = input("Which year do you want to check?")

# common error where input is string and has not been converted to
# integer so that calculations can take place
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# logic error - line 36 should be "and" not "or"
for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
# not reading requirements - number should not be in a list
        print([number])
