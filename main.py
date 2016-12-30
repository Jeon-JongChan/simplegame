from tkinter import *
import table,gamemap,ball,obstacle

window = Tk()
window.title("For servival!")

my_table = table.Table(window,level = 0)
my_map = gamemap.Gamemap(table = my_table,level = my_table.level)
my_ball = ball.Ball(table = my_table,line = my_map,level = my_table.level)
my_obstacle = obstacle.Obstacle(table = my_table,ball = my_ball,level = my_table.level)


def game_flow():
    global level_state
    if my_obstacle.obstacle_ball_collision():
        my_ball.restart_pos()
    if my_ball.x_pos > my_map.map_x_des[my_map.level][0] and my_ball.x_pos < my_map.map_x_des[my_map.level][1]:
        if my_ball.y_pos > my_map.map_y_des[my_map.level][0] and my_ball.y_pos < my_map.map_y_des[my_map.level][1]:
            if my_table.level < 5:
                level_state = True
                my_ball.stop_ball()
                my_table.canvas.create_text(400,400,font = ("",40),text = "arrive!")
                my_table.canvas.create_text(400,450,font = ("",40),text = "next game -> spacebar")
                return 0
            else:
                my_table.canvas.create_text(400,400,font = ("",40),text = "you are alive!!")
                my_table.canvas.create_text(400,450,font = ("",40),text = "Finish")
                level_state = False
                window.after(1000, close_game)
                return 0
                
    my_ball.move_ball()
    my_obstacle.move_next()

    window.after(20, game_flow)

def next_level(master):
    global level_state
    if level_state:
        level_state = False
        my_table.canvas.delete(ALL)
        my_table.level += 1
        my_ball.create_ball()
        my_map.draw_map()
        my_obstacle.create_obstacle()
        game_flow()
        
def close_game():
    window.after(5000,)
    window.destroy()
    
#버튼을 window 창에 붙임.
window.bind("<Up>",my_ball.move_up)
window.bind("<Down>",my_ball.move_down)
window.bind("<Right>",my_ball.move_right)
window.bind("<Left>",my_ball.move_left)
window.bind("<space>",next_level)

level_state = False    
game_flow()

window.mainloop()
    
