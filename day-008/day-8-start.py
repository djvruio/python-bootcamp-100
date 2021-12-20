def greet():
    print(f"Hello Mickey")
    print(f"How do you do?")
    print("Isn't the weather nice today?")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Rafael")

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# positional arguments
greet_with("Karen", "Ecuador")
greet_with("Ecuador", "Karen")

# keyword arguments

greet_with(location="Pichincha", name="Guaguash")