import turtle as t
import random as rand
t.fillcolor('orange')
t.pensize(5)
t.turtlesize(10)
t.shape("square")
def spot_clicked(x,y):
  change_position()
  update_score()
def change_position():
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  t.hideturtle()
  t.goto(new_xpos,new_ypos)
  t.showturtle()
t.onclick(spot_clicked)

def fxn1(x,y): 
  wn.addshape('scary1.gif')
  t.shape('scary1.gif')
def fxn2(x,y):
  wn.addshape('scary2.gif')
  t.shape('scary2.gif')
  
def fxn3(x,y):
  wn.addshape('scary3.gif')
  t.shape('scary3.gif')

t.onclick(fxn1)
t.onclick(fxn2)
t.onclick(fxn3)

wn = t.Screen()
wn.mainloop()
