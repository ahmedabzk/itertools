import itertools
letters = ['a','b','c','d']
numbers = [0,1,2,3,4]
names = ['Corey', 'Nicole']

# combines different items
result = itertools.chain(letters, numbers, names)
for item in result:
    print(item)
