# string interpolation is adding a variable to a string that should be printed
print('string interpolation')

# .format()
print('This is dot {}'.format('format'))
print(' this is to {} {} {}'.format('print', 'multiple', 'values'))
print(' this is to {0} {1} {2}'.format('print', 'multiple', 'values'))
print(' this is to {0} {0} {0}'.format('print', 'multiple', 'values'))
print(' this is to {a} {b} {c}'.format(a='print', b='multiple', c='values'))

# float formatting {value:width.precision f}, width is number of white space to be printed
# before value and precision is number of numbers after decimal point to be printed
# or total length of value
a = 777/100
print('the value of a is {}'.format(a))
print(' the value of a is {a:1.1f}'.format(a=a))
print(' the value of a is {a:10.1f}'.format(a=a))

# f-strings (formatted string literals method of string interpolation
print(f'this is f{'-strings'}')
print(f'this is to print {a}')
name = 'lalitha'
age = 29
print(f'using f-strings to print name = {name} and age =  {age}')

