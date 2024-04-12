#ffizzbuzz

#  Write a program that prints the numbers from 1 to 100
x = 0
while x < 101:
    x += 1
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
#- For multiples of three print "Fizz" instead of the number
    elif x % 3 == 0:
        print("fizz")

 #  For the multiples of five print "Buzz" instead of the number
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
# For numbers which are multiples of both three and five print "FizzBuzz"




