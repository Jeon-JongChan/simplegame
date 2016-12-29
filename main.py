from tkinter import *
import table,gamemap,ball,obstacle

window = Tk()
window.title("For servival!")

my_table = table.Table(window)
my_map = gamemap.Gamemap(table = my_table,level = 0)
my_ball = ball.Ball(table = my_table,line = my_map)
my_obstacle = obstacle.Obstacle(table = my_table,line = my_map)
#버튼을 window 창에 붙임.
window.bind("<Up>",my_ball.move_up)
window.bind("<Down>",my_ball.move_down)
window.bind("<Right>",my_ball.move_right)
window.bind("<Left>",my_ball.move_left)

window.mainloop()
