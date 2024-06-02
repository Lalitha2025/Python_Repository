# Tuples are IMMUTABLE, once an element is inside a tuple it cannot be changed
# tuples can hold multiple data type, Indexing and slicing are possible
# used when passing objects in programs , so they are not accidentally changed,data integrity
t = (1, 1, 2, 2, 2, 3, 3, 6, 4, 3, 5, 7, 2, 4, 7, 4)
# indexing
for x in range(0, 3):
    print(t[x])
print("length of tuple t is ", len(t))
print("the number of occurrence of 1 in tuple t is ", t.count(1))
# slicing
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12)
print(tup[0:12:2])
# find index
print(tup.index(0))
print(tup.count(12))
# nested tuple
nes_tup = (1, 2, 3, 4, 5, (6, 7, 8))
print(nes_tup[5][2])
