import random
import time
import turtle
# module to perform basic 2D garphic operations.
# here used to create the turtle graphic screen.

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def intit_turtle():
    screen = turtle.Screen()      # Setting up the turtle screen as a variable.
    screen.setup(WIDTH, HEIGHT)   # Setting up the height and the weight of the turtle screen.
    screen.title('Turtle Racing') # Setting up the title name for the turtle screen.
    time.sleep(2)

def num_of_racers():
    while True:
        num = input("Enter the number of turtles that would be racing (2 - 10): ")
        if num.isdigit():
            num = int(num)
            if 2 <= num <= 10:
                break
            else: print("The number of racers can only be between 2 to 10.")
        else: 
            print("Enter a valid number.") 
            continue
    return num

def create_turtles(colors):    # creating turtle is automated by a loop as the num of turtles is variable.
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors): 
        # what enumerate does is that it gets the index as well as the key from the dict.
        # so here, colour will store each colour value from the colours dict.
        racer = turtle.Turtle() # setting up the actual turtle as a variable.
        racer.color(color)      # setting up the colour of each turtle.
        racer.shape('turtle')   # setting up the shape of the turtle as a 'turtle'. Default is 'arrow'.
        racer.left(90)          # this is done, as from default, the turtles face towards right of the screen.
        racer.penup()           # this is done so the the turtles don't draw a line while going back to their initail racing position.
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)          
        # setting up the postion for the turtles (Here, the starting point for the race).
        # the algorithm used is explained in the readme file.
        racer.pendown()
        turtles.append(racer)   # storing this turtle in the turtles dictonary
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            move_distance = random.randrange(1,20) 
            # difference btw randrange() and randint() is that randint is inclusive of endpoints and randrange is exlusive.
            racer.forward(move_distance)

            x, y = racer.pos()
            if y > ((HEIGHT // 2) - 20):
                return colors[turtles.index(racer)]
                # return has a inbuild break system.
                # here we are first getting the index of the turtle that won the game and then using the index in 'color' dict
                # to get the color of the turtle.

num_racers = num_of_racers()
intit_turtle()
random.shuffle(COLORS) # shuffles the colours dictonary.
colors = COLORS[:num_racers]
# using a additional '[]' after a dict works as a slice opertor.
# here the slice operator slices the dict according to the num of racers.

winner = race(colors).capitalize()
print(f"{winner} turtle won the race!")
time.sleep(3)


# THIS PROGRAM IS THE EXAMPLE OF A DYNAMIC PROGRAM (HOW?)