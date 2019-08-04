##Pseudo code

import turtle 

SQ=20


bowl=turtle.Turtle()
bowl.penup()
turtle.hideturtle()
def right ():
	bowl.direction='Right'
	print('you moved to the right')
	move()

def left ():
	bowl.direction='Left'
	print('you moved to the left')
	move()



turtle.direction='Left' 
turtle.onkeypress(right,'Right')
turtle.onkeypress(left,'Left')
turtle.listen()    


def move ():
    my_pos=bowl.pos()
    xpos=my_pos[0]
    ypos=my_pos[1]
    if turtle.direction=='Left':
        bowl.goto(xpos-SQ,ypos)
    elif turtle.direction=='Right':
        bowl.goto(xpos+SQ,ypos)
        print('obvious')
move()
turtle.mainloop()

