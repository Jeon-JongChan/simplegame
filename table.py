from tkinter import *

class Table:
    def __init__(self,window,level = 0,color = "white", line_color = "black",
                 width = 800,height = 800):
        self.width = width
        self.height = height
        self.color = color
        self.level = level
        self.canvas = Canvas(window, bg=self.color,height = self.height,
                             width = self.width)
        self.canvas.pack()
        
    def draw_oval(self, oval): #원을 그리는 함수
        x1 = oval.x_pos
        x2 = oval.x_pos + oval.width
        y1 = oval.y_pos
        y2 = oval.y_pos + oval.height
        c = oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)
    
    def draw_line(self, line,level,phase): # 맵 선을 그려주는 함수
        x1 = line.map_x_pos[level][phase][0]
        x2 = line.map_y_pos[level][phase][0]
        y1 = line.map_x_pos[level][phase][1]
        y2 = line.map_y_pos[level][phase][1]
        return  self.canvas.create_line(x1,x2,y1,y2,width = 3,fill = "black")
    
    def move_item(self,item,x1,y1,x2,y2): # 객체를 이동시킨다.
        self.canvas.coords(item, x1, y1, x2, y2)
