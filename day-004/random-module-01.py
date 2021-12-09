import random

print(random.seed(1))

# get the state of the generator
state = random.getstate()
print(f'state: {state}')

print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))

# restore the state to a point before the sequence was generated
random.setstate(state)

print('Generating the same identical sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))