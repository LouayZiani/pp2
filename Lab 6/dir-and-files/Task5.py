# Task 5: Write a Python program to write a list to a file.



filename = input("Enter file name: ")
lista = input("Enter list you would like to add: ")
my_list = [values for values in lista.split()]

with open(filename, "w") as file:
    for item in my_list:
        file.write(item + "\n")

print("List written to", filename)