# Task 5:

from itertools import permutations

def permutation(str):
    Array = permutations(str)
    return list(Array)

word = input()
answer = permutation(word)

print(answer)