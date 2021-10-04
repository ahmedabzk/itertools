import itertools 

# ziplongest
data = [100,200,300]
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

# cycle
counter = itertools.cycle(("On", "Off"))
print(next(counter))
print(next(counter))
print(next(counter))

# repeat
square = map(pow, range(10),itertools.repeat(2))
print(list(square))

# starmap
sq = itertools.starmap(pow, [(0,2), (1,2), (2,2)])
print(list(sq))