num = input('Enter a number:\n')
num = int(num)
output = ''

if (num % 3) == 0:
    output += 'Fizz'

if (num % 5) == 0:
    output += 'Buzz'

if output == '':
    output = num

print(output)
