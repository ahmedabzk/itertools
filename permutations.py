import itertools
letters = ['a','b','c','d']
numbers = [0,1,2,3,4]
names = ['Corey', 'Nicole']

# permutations are used to iterate over items where order does matter
result = itertools.permutations(letters,2)
for item in result:
    print(item)
