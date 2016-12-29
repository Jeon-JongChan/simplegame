import table,random,ball

class Obstacle:
    def __init__(self,table,ball,color = 'black',width = 10,height=10,level = 0):
        self.table = table
        self.ball = ball 
        self.color = color
        self.width = 10
        self.height = 10
        self.level = level
        self.speed = 1
        self.state = True
        
        self.x_pos = 0
        self.y_pos = 0
        self.obstacle_x_pos = []
        self.obstacle_y_pos = []
        self.obstacle_x_pos.append([310,310,310,310,310,310,310]) #level 0
        self.obstacle_y_pos.append([600,450,400,300,250,200,100]) #level 0
        self.obstacle_x_pos.append([100,200,310,310,310,310,700,750])
        self.obstacle_y_pos.append([30,30,200,300,400,500,600,600])
        self.obstacle_x_speed = []
        self.obstacle_y_speed = []
        self.obstacle_num = [7,8,9,10]
        self.obstacle = []
        self.creat_obstacle(self.level)

    def creat_obstacle(self,level):
        del self.obstacle_x_speed 
        del self.obstacle_y_speed
        self.obstacle_x_speed = []
        self.obstacle_y_speed = []
        for i in range(0,self.obstacle_num[level]):
            if i < len(self.obstacle_x_pos[level]):
                self.x_pos = self.obstacle_x_pos[level][i]
            if i < len(self.obstacle_y_pos[level]):
                self.y_pos = self.obstacle_y_pos[level][i]
            self.obstacle.append(self.table.draw_oval(self))
            self.speed = random.randint(5,15)
            self.obstacle_x_speed.append(self.speed)
            self.obstacle_y_speed.append(self.speed)
            
    def obstacle_line_collision(self,num):
        if self.obstacle_x_speed[num] > 0:
            self.obstacle_x_pos[self.level][num],self.obstacle_y_pos[self.level][num],collision_state = self.ball.line_collision(self.obstacle_x_pos[self.level][num]
                                                            ,self.obstacle_y_pos[self.level][num]
                                                            ,self.width
                                                            ,self.height
                                                            ,self.obstacle_x_speed[num]
                                                            ,self.obstacle_y_speed[num])
        else:
            self.obstacle_x_pos[self.level][num],self.obstacle_y_pos[self.level][num],collision_state = self.ball.line_collision(self.obstacle_x_pos[self.level][num]
                                                            ,self.obstacle_y_pos[self.level][num]
                                                            ,self.width
                                                            ,self.height
                                                            ,-self.obstacle_x_speed[num]
                                                            ,self.obstacle_y_speed[num])
        return collision_state
                                                                                                            
    def obstacle_ball_collision(self):
        for num in range(0,self.obstacle_num[self.level]):
            if abs(self.ball.x_pos - self.obstacle_x_pos[self.level][num]) < 13  and abs(self.ball.y_pos - self.obstacle_y_pos[self.level][num]) < 13 :
                print("debug1")
                return True
            
    def move_next(self):
        for num in range(0,self.obstacle_num[self.level]):
            if self.obstacle_x_pos[self.level][num] > 0 and self.obstacle_x_pos[self.level][num] < 800:
                self.obstacle_x_pos[self.level][num] += self.obstacle_x_speed[num]
                self.state = self.obstacle_line_collision(num)

            if self.state:
                x1 = self.obstacle_x_pos[self.level][num]
                x2 = self.obstacle_x_pos[self.level][num]+self.width
                y1 = self.obstacle_y_pos[self.level][num]
                y2 = self.obstacle_y_pos[self.level][num]+self.height
                self.table.move_item(self.obstacle[num], x1, y1, x2, y2)            
            else:
                x1 = self.obstacle_x_pos[self.level][num]
                x2 = self.obstacle_x_pos[self.level][num]+self.width
                y1 = self.obstacle_y_pos[self.level][num]
                y2 = self.obstacle_y_pos[self.level][num]+self.height
                self.table.move_item(self.obstacle[num], x1, y1, x2, y2)
                self.obstacle_x_speed[num] = -self.obstacle_x_speed[num]
                

        
        
