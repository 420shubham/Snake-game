from turtle import Turtle, Screen

MOVE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    
    def __init__(self):
        self.seg_list=[]
        self.create_snake()
        self.head= self.seg_list[0]

        
    def create_snake(self):
        x_axis=0
        for self.i in range(3):
            self.t=Turtle(shape="square")
            self.t.speed(0)
            self.t.pu()
            self.t.color("white")
            self.t.goto(x=x_axis,y=0)
            x_axis-=20
            self.seg_list.append(self.t)

    def move(self):
        for seg_num in range(len(self.seg_list)-1,0,-1):
            x_cor=self.seg_list[seg_num-1].xcor()
            y_cor=self.seg_list[seg_num-1].ycor()
            self.seg_list[seg_num].goto(x_cor,y_cor)
        self.head.fd(MOVE)

    def extend(self):
        new_seg=Turtle("square")
        new_seg.penup()
        new_seg.speed(0)
        new_seg.color("white")
        new_seg.goto(x=self.seg_list[-1].xcor(),y=self.seg_list[-1].ycor())
        self.seg_list.append(new_seg)
            
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    