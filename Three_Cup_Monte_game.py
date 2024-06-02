from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def user_guess():
    guess= ''
    while guess not in ['0','1', '2']:
        guess = input('choose a value between 0, 1, 2\n')
    return int(guess)

def check_guess(mylist, num):
    if mylist[guess] == 'O':
        print('correct')
        print(mylist)
    else:
        print('Wrong')
        print(mylist)

# initiate a list
list1 = [' ', ' ' , 'O']
# shuffle the list
list1 = shuffle_list(list1)
# ask the user for guess
guess = user_guess()
# check guess
check_guess(list1, guess)


