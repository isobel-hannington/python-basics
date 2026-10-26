"""FizzBuzz: print the numbers 1 to 100, replacing multiples of 3 with
"fizz", multiples of 5 with "buzz" and multiples of both with "fizzbuzz".

The "both" check comes first. If it came after the check for 3, the
number 15 would print "fizz" and never reach the "fizzbuzz" branch.
"""

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
