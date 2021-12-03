print("Day 1 - Python Print Function")
print("The funtion is declared like this:")
print("print('what to print single quotes')")
print('print("what to print double quotes")')
print("----------------------------------")
print("Hello world!\nHello World!")
print("Hello" + " Darwin")
print("Hello " + "Rafa")
print("Hello" + " " + "Karen")
print("Hello"+" Deeper")
print("""Hello triple quotes
because this is a large
huge string and is used to python
documentation""")
# By default print() automatically adds a "\n" to the end of each string before printing it
print('<div class="md-col">')
print('I\'m Dark')
print("--------------------------")
print("Primera línea\nSegunda Línea\n \tTercera Línea con 1 tab\n \t\tCuarta Línea con 2 tabs")
print("bong \a\a")
print("Octal 275 is a half: \275")
print("--------------------------")
print("C:\Windows\System32")
print("^\\d+(\\.\\d+)?")
print(r'^\d+(\.\d+)?') # better r "raw"c--escape free
print(70*"X")
print('\n') # blank line
print('')   # empty line
print("-" * 25)
import os
print("Hello " + os.getlogin() + '! How are you?')
print(f'Hola {os.getlogin()}! ¿Cómo estás?') # review f-strings
# print("My age is:" + 42) #TypeError
print("My age is: " + str(42))
