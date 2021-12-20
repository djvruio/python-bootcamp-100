#Write your code below this line 👇

def prime_checker(number):
    modulos = []
    if number > 1:
        for x in range(1, number + 1):
            if number % x == 0:
                modulos.append("divisible")
            else:
                modulos.append("non divisible")
       
        if modulos.count("divisible") > 2:
            print(f"{number} It's not a prime number.")
        else:
            print(f"{number} It's a prime number.")
    else:
        print("You should enter a number greater than 1.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

for i in range(1, 101):
    prime_checker(i)