import os

def mymap(func, *seqs) :
    return [func(*args) for args in zip(*seqs)]

print(mymap(abs, [-2, -1, 0, 1, 2]))
print("==")
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
