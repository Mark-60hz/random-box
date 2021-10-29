import turtle as t
import random as rand
t.fillcolor('orange')
t.pensize(5)
t.turtlesize(10)
t.shape("square")

def fxn(x,y): 
  wn.addshape('scary.gif')
  t.shape('scary.gif') 

t.onclick(fxn)

wn = t.Screen()
wn.mainloop()
