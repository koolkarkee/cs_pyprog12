numbers = [1, 2, 3, 4, 5]

converted = lambda x: 'even' if x%2 == 0 else 'odd'
print(list(map(converted, numbers)))
