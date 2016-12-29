import table,random,gamemap

class Obstacle:
    def __init__(self,table,line,color = 'black',width = 10,height=10,level = 0,speed = 5):
        self.table = table
        self.line = line 
        self.color = color
        self.width = 10
        self.height = 10
        self.level = level
        
        self.x_pos = 0
        self.y_pos = 0
        self.obstacle_x_pos = [[300,300,300,300,300]]
        self.obstacle_y_pos = [[600,450,400,200,100]]
        self.obstacle_num = [5,6,7,8]
        self.obstacle = []
        self.creat_obstacle(self.level)

    def creat_obstacle(self,level):
        for i in range(0,self.obstacle_num[level]):
            if i < len(self.obstacle_x_pos[level]):
                self.x_pos = self.obstacle_x_pos[level][i]
            if i < len(self.obstacle_y_pos[level]):
                self.y_pos = self.obstacle_y_pos[level][i]
            self.obstacle.append(self.table.draw_oval(self))
""" 
    def move_next(self):
        for i in range(0,self.obstacle_num[level]):
            self.obstacle_x_pos[level][i] += speed
            if self.obstacle_x_pos[level][i] < self.line.
            """

        
        
