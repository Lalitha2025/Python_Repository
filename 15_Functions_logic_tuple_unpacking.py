# return true if any  number is even in the list

list1 = [1,3,5,7,9,11]

def even_check(num1):
    y = False
    for x in num1:
        if (x %2 == 0):
            y=True
    return y

value= even_check(list1)
print(value)

#return all the even numbers in the list
list1 = [1,2,3,4,5,6,7,8]
def check_list_even(num_list):
    list2=[]
    for x in num_list:
        if(x%2 == 0):
            list2.append(x)
        else:
            pass
    return list2
list3 = []
list3 = check_list_even(list1)
print(list3)

list5 = [('a', 100), ('d',500), ('b',2000), ('c',400) ]
def emp_year(num_list):
    highest_hours = 0
    emp_name =''
    for emp, hours in num_list:
        if  hours > highest_hours:
            highest_hours = hours
            emp_name = emp
        else:
            pass
    return (emp_name, highest_hours)

emp_name, hours = emp_year(list5)
print(f'{emp_name} is the emp of the year with {hours} hours')





 


