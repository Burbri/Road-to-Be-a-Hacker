# For integers 1-100, 
# print "Fizz" if the integer is a multiple of 3
# and print "Buzz" if the integer is a multiple of 5.
# Print "FizzBuzz" if it is a multiple of both.


def fibuzz(n):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

for i in range(100):
    fibuzz(i+1)
