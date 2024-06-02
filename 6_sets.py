# sets are unordered collection of unique elements
# no element can be presented more than once in a set
# sets are mutable

myset = set()
print(myset)
print(type(myset))
myset.add(0)
myset.add('abc')
print(myset)
myset.add(0)
print(myset)
mylist = [1,1,1,1,2,3,4,5,3,4,5,6,7,8,5,6,7,8,9,10]
newlist = set(mylist)
print(newlist)
print( set(mylist))
# sets are mutable elements can be added, deleted
newlist.remove(2)
print(newlist)