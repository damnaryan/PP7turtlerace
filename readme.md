## This is a learning project.
I am making this project to learn python.So, instead of learing the syntax first, I am building this project to learn while I am building this. I have made notes within the code as comments, of every new concept I get to know.
##### Source of learning: https://www.youtube.com/watch?v=NpmFbWO6HPU&list=WL
### About this project:
THIS IS A GOOD INTERMIDATE LEVEL PROJECT. At least for me, it is. Instead of a text based program, this is full fletched graphic game. With animations and stuff! Here, the users define the number of turtles, that would be racing. And at the end print the colour of the winning turtle.

### [ IN PROGRESS ]

## Learnings:

##### Learning the turtle module:
- racer = turtle.Turtle() # setting up the turtle as a variable.
- racer.forward(100)      # moves the turtle forward by 100 pixels.
- racer.right(90)         # turns the turtle right by 90 degrees.
- racer.left(90)          # turns the turtle left by 90 degrees.
- racer.backward(100)     # moves the turtle backward by 100 pixels.
- racer.shape('round')    # change the icon shape (round, turtle, arrow are some valid shapes).
- racer.color('cyan')     # change the colour of the turtle.
- racer.speed(5)          # change the speed of the turtle.
- racer.penup()/.pendown()# toggle the pen for the turtle.
##### Algorithm for setting the intial race position of the turtles:
Step 1- Dividing x-axis in (num+1) parts where 'num' is the number of turtles the user initaitised. This will give the spacing required between each turtle. [NOTE: Dividing by num+1 parts because it won't result in placing the first or the last turtle at the border.]
Step 2- Progressively adding the spacing to negative half of how long the x-axis is.
Step 3- Placing the turtle at each sucession.


Turtle doc file: https://docs.python.org/3/library/turtle.html