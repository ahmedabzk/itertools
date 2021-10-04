import itertools
letters = ['a','b','c','d']
numbers = [0,1,2,3,4]
names = ['Corey', 'Nicole']

# combinations are used to iterate over items where order does not matter
result = itertools.combinations(letters,2)
for item in result:
    print(item)


# combinations_with_replacement allows repeated items
