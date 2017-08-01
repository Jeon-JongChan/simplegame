from tkinter import *
import table,gamemap,ball,obstacle

def start_menu():
    i = 0
    for btn_text in button_text :
        def cmd(x = btn_text):
            click(x)
        button.append(Button(main,text = btn_text,width = 15,height = 2 , command = cmd))
        button[i].grid(row = i,column = 0,)
        i += 1
        
def click(x):
    global key
    
    key = x
        
    main.destroy()
    start_game()

def collision_check():
    global life
    global life_state
    
    if my_obstacle.obstacle_ball_collision():
        if life_state == False:
            if life == 0:
                life = my_ball.life
                my_table.canvas.itemconfig(my_ball.circle,fill = "green")
                my_ball.limit_speed = 2
                my_ball.restart_pos()
            elif life == 1:
                my_table.canvas.itemconfig(my_ball.circle,fill = "red")
                my_ball.limit_speed = 7
                life -= 1
            elif life == 2:
                my_table.canvas.itemconfig(my_ball.circle,fill = "blue")
                my_ball.limit_speed = 5
                life -= 1
            life_state = True
        else:
            life_state = True
    else:
        life_state = False
            
def game_flow():
    global level_state

    collision_check()
    
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
    
def start_game():
    global my_table
    global my_map
    global my_ball
    global my_obstacle
    
    my_table = table.Table(window,level = 0)
    my_map = gamemap.Gamemap(table = my_table,level = my_table.level)
    my_ball = ball.Ball(table = my_table,line = my_map,level = my_table.level)
    my_obstacle = obstacle.Obstacle(table = my_table,ball = my_ball,level = my_table.level)

    if key == button_text[0]:
        my_ball.life = 2
    elif key == button_text[1]:
        my_ball.life = 1
    elif key == button_text[2]:
        my_obstacle.max_speed = 7
        my_ball.life = 0
        my_ball.hard = True
    elif key == button_text[3]:
        my_obstacle.max_speed = 10
        my_ball.life = 0
        my_ball.hard = True
        
    global life
    life = my_ball.life

    #버튼을 window 창에 붙임.
    window.bind("<Up>",my_ball.move_up)
    window.bind("<Down>",my_ball.move_down)
    window.bind("<Right>",my_ball.move_right)
    window.bind("<Left>",my_ball.move_left)
    window.bind("<space>",next_level)
    
    game_flow()
    level_state = False
    
window = Tk()
window.title("For servival!")

main = Frame(window)
main.pack()

button_text = ["Easy","Nomal","Hard","go to the hell"]
button = []

start_menu()
global my_table
global my_map
global my_ball
global my_obstacle

global life_state

life_state = False
    
window.mainloop()
    
