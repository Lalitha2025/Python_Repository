# lists are ordered sequence that can hold variety of object types, also lists are
# mutable which means they can be changed
# lists support indexing and slicing, lists can be nested

my_list = ['this', 'is', 'to', 'understand', 'lists']
print(my_list[0])
# multiple data types can be one list
variety_datatype = ['strings', 1, 12.2]
print(variety_datatype[0])
print(variety_datatype[1])
print(variety_datatype[2])

# lists can be added
print(my_list + variety_datatype)
new_list = my_list + variety_datatype
print(new_list)

# print all the list
print(new_list[1:])
# print last value in the list
print(new_list[-1:])

# list are mutable that means changeable unlike strings
print(new_list)
new_list[0] = 0
new_list[1] = 1
new_list[2] = 2
print(new_list)

# print list in reverse
print(list(reversed(new_list)))

# append() function allows to add a value at the end of the list
new_list.append('six')
print(new_list)
# pop() function to remove element from end of list, default vale is -1
new_list.pop()
print(new_list)
new_list.pop(0)
print(new_list)
# sorting the list
new_list = ['a', 'c', 'e', 'b','d']
new_list.sort()
print(new_list)
new_list = [5,3,2,1,4,6]
new_list.sort()
print(new_list)
# reverse a list
print(new_list)
new_list.reverse()
print(new_list)

# slicing a list
new_list = [ 1,2,3,4,5,6]
print(new_list[1:len(new_list)-1])
#print all the list
for i in range(5):
    print(i,new_list[i])

    ##interchange 1st and last element
    onelist = [1, 2, 3, 4, 5]
    print(onelist)
    a = onelist[0]
    onelist[0] = onelist[-1]
    onelist[-1] = a
    print(onelist)

    ## max and min value in list
    twolist = [5, 3, 1, 4, 2]
    threelist = twolist
    print(max(twolist))
    print(min(twolist))
    threelist.sort()
    print("The min and max value in the list are: ", threelist[0], threelist[-1])

    ## check if an element exists in list
    list4 = ['a','c','v','f','g','b']
    if 'a' in list4:
        print("value a exist in  list4 ")
    else:
        print("value a does not exist in  list4 ")

## clear out a list
## clear out a list
list4= [1,2,3,4,5]
print(list4.clear())
print(list4)




