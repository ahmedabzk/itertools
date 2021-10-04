import itertools 
counter = itertools.count()
data = [100,200,300]
daily_data = list(zip(itertools.count(), data))
print(daily_data)

print(next(counter))
print(next(counter))
print(next(counter))
