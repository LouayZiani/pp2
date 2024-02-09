# Task 6:

def reverse(i):
    example = ''
    i = i[-1::-1]
    for j in i:
        example = example + j 
    print(example)
    
word = input()
result = reverse(word)
print(result)