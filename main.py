from tkinter import *
import table,gamemap,ball,obstacle

window = Tk()
window.title("For servival!")

my_table = table.Table(window)
my_map = gamemap.Gamemap(table = my_table,level = 1)
my_ball = ball.Ball(table = my_table,line = my_map,level = my_map.level)
my_obstacle = obstacle.Obstacle(table = my_table,ball = my_ball,level = my_map.level)

def game_flow():
    if my_obstacle.obstacle_ball_collision():
        print("debug")
        my_ball.restart_pos()
    if my_ball.x_pos > my_map.map_x_des[my_map.level][0] and my_ball.x_pos < my_map.map_x_des[my_map.level][1]:
        if my_ball.y_pos > my_map.map_y_des[my_map.level][0] and my_ball.y_pos < my_map.map_y_des[my_map.level][1]:
            my_ball.stop_ball()
    print(my_ball.x_pos)
    my_obstacle.move_next()

    window.after(20, game_flow)

game_flow() 
#버튼을 window 창에 붙임.
window.bind("<Up>",my_ball.move_up)
window.bind("<Down>",my_ball.move_down)
window.bind("<Right>",my_ball.move_right)
window.bind("<Left>",my_ball.move_left)
window.mainloop()
