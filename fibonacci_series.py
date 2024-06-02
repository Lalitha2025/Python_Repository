# fibonacci

# ask for number of values
def fionacci_number_input():
    count = int(input('enter how many numbers needed in series'))
    fibonacci_sequence_generator(count)
# print out values
def fibonacci_sequence_generator(num):
    f0 = 0
    f1 = 1
    f2 = 0
    print(f0)
    print(f1)
    x=3
    while x <= num  :
        f2 = f0+f1
        print(f2)
        f0 = f1
        f1 = f2
        x=x+1
fionacci_number_input()


