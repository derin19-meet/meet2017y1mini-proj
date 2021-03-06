import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()

SQUARE_SIZE= 20
START_LENGTH= 5

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

snake=turtle.clone()
snake.shape("square")

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+= SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp_id=snake.stamp()
    stamp_list.append(stamp_id)

UP_ARROW="Up"
LEFT_ARROW= "Left"
DOWN_ARROW= "Down"
RIGHT_ARROW= "Right"
TIME_STEP= 100
SPACEBAR= "space"

UP=0
LEFT=1
DOWN=2
RIGHT=3

direction=UP

TOP_EDGE=250
LEFT_EDGE=-400
BOTTOM_EDGE=-250
RIGHT_EDGE= 400



def up():
    global direction
    direction=UP
    print("you pressed the up key")

def left():
    global direction
    direction= LEFT
    print("you pressed the left key")

def down():
    global direction
    direction= DOWN
    print("you pressed the down key")

def right():
    global direction
    direction= RIGHT
    print("you pressed the right key")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def make_food():
    min_x= -int(SIZE_X/2.5/SQUARE_SIZE)+1
    max_x= int(SIZE_X/2.5/SQUARE_SIZE)-1
    min_y= -int(SIZE_Y/2.5/SQUARE_SIZE)+1
    max_y= int(SIZE_Y/2.5/SQUARE_SIZE)-1

    food_x= random.randint(min_x, max_x)*SQUARE_SIZE
    food_y= random.randint(min_y, max_y)*SQUARE_SIZE

    food.goto(food_x, food_y)
    food_pos.append((food_x, food_y))
    f = food.stamp()
    food_stamps.append(f)
    

def move_snake():
    my_pos=snake.pos()
    x_pos= my_pos[0]
    y_pos= my_pos[1]

    if direction== UP:
        snake.goto(x_pos,y_pos+ SQUARE_SIZE)
        print("you moved up")
    elif direction== LEFT:
        snake.goto(x_pos-SQUARE_SIZE, y_pos)
        print("you moved left")
    elif direction== DOWN:
        snake.goto(x_pos,y_pos- SQUARE_SIZE)
        print("you moved down")
    elif direction== RIGHT:
        snake.goto(x_pos+ SQUARE_SIZE, y_pos)
        print("you moved right")

    my_pos= snake.pos()
    pos_list.append(my_pos)
    new_stamp= snake.stamp()
    stamp_list.append(new_stamp)
    

    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
   
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food")

        #turtle.write("+1 POINT")
        


        
        stamp_list.append(food_pos)
        pos_list.append(food_pos)

        
        

        
        
        

        make_food()
        
        

        

    
   
    if pos_list[-1] in pos_list[0:-1]:
        print("you have eaten yourself")
        quit()


    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    
   

    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge. game over")
        quit()

    if new_x_pos <= LEFT_EDGE:
        print("you hit the left edge. game over")
        quit()

    if new_y_pos >= TOP_EDGE:
        print("you hit the top edge. game over")
        quit()
        
    if new_y_pos <= BOTTOM_EDGE:
        print("you hit the bottom edge. game over")
        quit()

    turtle.ontimer(move_snake, TIME_STEP)

move_snake()

turtle.register_shape("trash.gif")
food=turtle.clone()
food.shape("trash.gif")

make_food()




        
            
            







        





    

    

    





        



    

    
