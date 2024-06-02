# Dictionaries are unordered mapping for string objects
# key value pairing allows to grab data quickly without knowing the index position
# dictionaries  = {'key 1 ':value1, 'key 2' : value 2  }
# dictionaries can hold int, float, string, list, dictionaries also
# cannot be sorted, ex: supermarket can use dictionaries

my_dict = {'key1': 'one', 'key2': 'two', 'key3': 'three'}
print(my_dict['key1'])


supermarket = {'apples': 2.99, 'guava': 3.99, 'banana': 10.99}
print(supermarket['apples'])
# print all the key and values in dictionaries 1 way
for k, v in supermarket.items():
    print(k, v)
# print all the key and values in dictionaries 2 way
print(*supermarket.items(), sep='\n')

# clears, erases all the  key value pairs in dictionaries
supermarket.clear()
for k, v in supermarket.items():
    print(k, v)

# dictionaries can hold list and other dictionaries
multi_dict = {'key1': 10, 'key2': 2.99, 'key3': [0, 1, 2, 3, 4], 'key4': {'key1': 1, 'key2': 2}}
print(multi_dict['key4'])
# access dictionaries inside dictionaries
print(multi_dict['key4']['key1'])
# access lists inside dictionaries
print(multi_dict['key3'])
print(multi_dict['key3'][0])


