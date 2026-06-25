# Day 18 - itertools module
import itertools

# count, cycle, repeat
for i in itertools.islice(itertools.count(1), 5):
    print(i)  # 1 2 3 4 5

# chain
result = list(itertools.chain([1, 2], [3, 4], [5]))
print(result)  # [1, 2, 3, 4, 5]

# combinations and permutations
items = ['a', 'b', 'c']
print(list(itertools.combinations(items, 2)))
print(list(itertools.permutations(items, 2)))

# groupby
data = [('a', 1), ('a', 2), ('b', 3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
