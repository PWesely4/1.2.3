#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
apple_fallen = 0
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
a_drawer = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def apple_fall():
  global apple_fallen
  apple.penup()
  apple.setheading(270)
  apple.forward(150)
  apple_fallen = 1
def before_apple_fall():
  global apple_fallen
  while apple_fallen == 0:
    a_drawer.penup()
    a_drawer.goto(10,10)
    a_drawer.color("white")
    a_drawer.write("A", font=("Arial", 74))
  
#-----function calls-----
wn.bgpic("background.gif")
draw_apple(apple)
before_apple_fall()
wn.onkeypress(apple_fall, "a")
wn.listen()
wn.mainloop()