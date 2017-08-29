def fizzbuzz(a):
    if a % 3 == 0 and a % 5 == 0:
        return 'FizzBuzz'
    if a % 3 == 0:
        return 'Fizz'
    if a % 5 == 0:
        return 'Buzz'
    else:
        return a

