#Task 6: Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt


import string

file_names = [letter + '.txt' for letter in string.ascii_uppercase]

for file_name in file_names:
    with open(file_name, 'w') as f:
        f.write('This is the {} file.'.format(file_name))