
#create a list with every value in the string
str1 = 'abcdefghijkl'
list1=[]
# using enumerate
for x,y in enumerate(str1):
    list1.append(y)
print(list1)

list1.clear()
for x in range(len(str1)):
    list1.append(str1[x])
print(list1)

list1.clear()
x=0
while x<len(str1):
    list1.append(str1[x])
    x=x+1
print(list1)

list1.clear()
for x in str1:
    list1.append(x)
print(list1)

