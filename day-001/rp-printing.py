import os
print('My name is', os.getlogin(), 'and I am', 42)
print('My name is', os.getlogin(), 'and I am', 42, sep="**")
print('My name is', os.getlogin(), 'and I am', 42, sep="\n")
print('My name is', os.getlogin(), 'and I am', 42, sep='/')
print("Be careful joining element of a list or tuple")
lista = ['Dark is', 42, 'years old.', 1980]
print(lista)
print(*lista, "With Star operator")

# new block - comma separated values
print(1, 34.5, 'UIO', 'Dark Vader','comma-separated',1+8j, sep=',')
print('node', 'child', 'subchild', sep=' => ')

# new block end keyword argument
print('-' * 25)
print("Are you sure you want to do this? [y/n]", end='')
user_response = input()
print(user_response, end='')
print("Ok")

# new block - end keyword argument
print('-' * 25)
print('First sentence', end='. ')
print('Second sentence', end='. ')
print('Last sentence.')

# new block - mix keyword arguments
print('-' * 25)
print("Mercurio", "Venus", "Tierra", sep=", ", end=", ")
print("Marte", "Jupiter", "Saturno", sep=", ", end=", ")
print("Urano", "Neptuno", "Plutón", sep=", ")

# new block - end with arbitrary strings
print(25 * '-')
print('Printing in a nutshell', end='\n\t * ')
print("Calling print", end='\n\t\t * ')
print("Separating multiples arguments", end='\n\t * ')
print('Preventing line breaks')

# new block - printing a file firts option
# two new lines after each line of text
print(25 * '-')
with open('filetest.txt') as file_object:
    for line in file_object:
        print(line)

# new block - printing a file second option
print(25*'-')
with open('filetest.txt') as file_object:
    for line in file_object:
        print(line, end='')

# new block - printing file with rstrip()
print("\n","-" * 25)
with open('filetest.txt') as file_object:
    for line in file_object:
        print(line.rstrip())