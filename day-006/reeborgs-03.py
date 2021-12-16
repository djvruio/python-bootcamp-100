def turn_rigth():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_rigth()
    move()
    turn_rigth()
    move()
    turn_left()


number_of_hurdles =  6

while number_of_hurdles > 0  and at_goal() == False:
    jump()
    number_of_hurdles -= 1

# while not at_goal():
#    jump()