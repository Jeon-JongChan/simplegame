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
        self.obstacle_check = 11
        self.max_speed = 5
        
        self.x_pos = 0
        self.y_pos = 0
        #각 장애물마다 랜덤하게 속도를 주기위해 만든 리스트
        self.r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        self.obstacle_num = [5,8,11,21,29]
        self.obstacle = []
        self.obstacle_x_pos = []
        self.obstacle_y_pos = []
        self.obstacle_x_pos.append([310,310,310,310,310]) #level 0
        self.obstacle_y_pos.append([600,450,400,300,250]) #level 0
        self.obstacle_x_pos.append([100,200,310,310,310,310,700,750])#level 1
        self.obstacle_y_pos.append([30,30,200,300,400,500,600,600])#level 1
        self.obstacle_x_pos.append([200,400,700,210,460,510,600,20,20,650,700])#level 2
        self.obstacle_y_pos.append([30,30,30,590,590,590,590,300,500,30,590])#level 2
        self.obstacle_x_pos.append([60,200,400,450,700,760, 740,600,440,400,250,60,10, 60,200,400,680,710, 50,700,700])#level 3
        self.obstacle_y_pos.append([30,30,30,30,30,200, 330,330,330,330,330,330,590, 610,610,610,610,610, 30,610,690])#level 3
        self.obstacle_x_pos.append([60,200,500,550,720,760,760,  740,600,520,300,150,25,40,  150,230,400,630,660, 200,300,600,120,  500,550,400,400,50,50])#level 4
        self.obstacle_y_pos.append([30,30,30,30,30,160,590,  600,600,600,600,600,690,450,  180,180,180,180,350, 460,460,460,410,  330,330,330,380,30,110])#level 4

        self.create_obstacle()
        self.obstacle_x_speed = [[self.r[0],self.r[1],self.r[2],self.r[3],self.r[4]]]
        self.obstacle_y_speed = [[0,0,0,0,0]]
        
        self.obstacle_x_speed.append([0,0,self.r[0],self.r[1],self.r[2],self.r[3],0,self.r[7]])
        self.obstacle_y_speed.append([self.r[4],self.r[5],0,0,0,0,self.r[6],self.r[7]])
        
        self.obstacle_x_speed.append([0,0,0,0,0,0,0,self.r[7],self.r[8],self.r[9],self.r[10]])
        self.obstacle_y_speed.append([self.r[0],self.r[1],self.r[2],self.r[3],self.r[4],self.r[5],self.r[6],0,0,self.r[9],self.r[10]])

        self.obstacle_x_speed.append([0,0,0,0,0, self.r[5], 0,0,0,0,0,0,self.r[12], 0,0,0,0,0,self.r[18],self.r[19],self.r[20]])
        self.obstacle_y_speed.append([self.r[0],self.r[1],self.r[2],self.r[3],self.r[4], 0,self.r[6],self.r[7],self.r[8],self.r[9],self.r[10],self.r[11],0, self.r[13],self.r[14],self.r[15],self.r[16],self.r[17],self.r[18],self.r[19],self.r[20]])

        self.obstacle_x_speed.append([0,0,0,0,0, self.r[5],self.r[6], 0,0,0,0,0,0,self.r[13], 0,0,0,0,self.r[18], 0,0,0, self.r[12],  0,0,0,self.r[23],self.r[24],self.r[25]])
        self.obstacle_y_speed.append([self.r[0],self.r[1],self.r[2],self.r[3],self.r[4],0,0,  self.r[6],self.r[7],self.r[8],self.r[9],self.r[10],self.r[11],0,  self.r[14],self.r[15],self.r[16],self.r[17],0,  self.r[17],self.r[18],self.r[19],0,  self.r[20],self.r[21],self.r[22],self.r[23],self.r[24],self.r[25]])

    def create_obstacle(self):
        self.level = self.table.level
        self.obstacle = []
        for i in range(0,self.obstacle_num[self.level]):
            if i < len(self.obstacle_x_pos[self.level]):
                self.x_pos = self.obstacle_x_pos[self.level][i]
            if i < len(self.obstacle_y_pos[self.level]):
                self.y_pos = self.obstacle_y_pos[self.level][i]
            self.obstacle.append(self.table.draw_oval(self))
                                   
        for i in range(0,len(self.r)):
            self.r[i] = random.randint(2,self.max_speed)

                       
            
    def obstacle_line_collision(self,num):
        if self.obstacle_x_speed[self.level][num] >= 0 and self.obstacle_y_speed[self.level][num] >= 0:
            self.obstacle_x_pos[self.level][num],self.obstacle_y_pos[self.level][num],collision_state = self.ball.line_collision(self.obstacle_x_pos[self.level][num]
                                                            ,self.obstacle_y_pos[self.level][num]
                                                            ,self.width
                                                            ,self.height
                                                            ,self.obstacle_x_speed[self.level][num]
                                                            ,self.obstacle_y_speed[self.level][num])
        elif self.obstacle_x_speed[self.level][num] < 0 and self.obstacle_y_speed[self.level][num] >= 0:
            self.obstacle_x_pos[self.level][num],self.obstacle_y_pos[self.level][num],collision_state = self.ball.line_collision(self.obstacle_x_pos[self.level][num]
                                                            ,self.obstacle_y_pos[self.level][num]
                                                            ,self.width
                                                            ,self.height
                                                            ,-self.obstacle_x_speed[self.level][num]
                                                            ,self.obstacle_y_speed[self.level][num])
        elif self.obstacle_x_speed[self.level][num] >= 0 and self.obstacle_y_speed[self.level][num] < 0:
            self.obstacle_x_pos[self.level][num],self.obstacle_y_pos[self.level][num],collision_state = self.ball.line_collision(self.obstacle_x_pos[self.level][num]
                                                            ,self.obstacle_y_pos[self.level][num]
                                                            ,self.width
                                                            ,self.height
                                                            ,self.obstacle_x_speed[self.level][num]
                                                            ,-self.obstacle_y_speed[self.level][num])
        elif self.obstacle_x_speed[self.level][num] < 0 and self.obstacle_y_speed[self.level][num] < 0:
            self.obstacle_x_pos[self.level][num],self.obstacle_y_pos[self.level][num],collision_state = self.ball.line_collision(self.obstacle_x_pos[self.level][num]
                                                            ,self.obstacle_y_pos[self.level][num]
                                                            ,self.width
                                                            ,self.height
                                                            ,-self.obstacle_x_speed[self.level][num]
                                                            ,-self.obstacle_y_speed[self.level][num])
        return collision_state
                                                                                                            
    def obstacle_ball_collision(self):
        for num in range(0,self.obstacle_num[self.level]):
            if abs(self.ball.x_pos - self.obstacle_x_pos[self.level][num]) < self.obstacle_check  and abs(self.ball.y_pos - self.obstacle_y_pos[self.level][num]) < self.obstacle_check :
                return True
            
    def move_next(self):
        for num in range(0,self.obstacle_num[self.level]):
            if self.obstacle_x_pos[self.level][num] > 0 and self.obstacle_x_pos[self.level][num] < 800:
                self.obstacle_x_pos[self.level][num] += self.obstacle_x_speed[self.level][num]
                self.obstacle_y_pos[self.level][num] += self.obstacle_y_speed[self.level][num]
                self.state = self.obstacle_line_collision(num)
           
            if self.state > 0:
                if num < self.obstacle_num[self.level] - self.level:
                    x1 = self.obstacle_x_pos[self.level][num]
                    x2 = self.obstacle_x_pos[self.level][num]+self.width
                    y1 = self.obstacle_y_pos[self.level][num]
                    y2 = self.obstacle_y_pos[self.level][num]+self.height
                    self.table.move_item(self.obstacle[num], x1, y1, x2, y2)
                    self.obstacle_x_speed[self.level][num] = -self.obstacle_x_speed[self.level][num]
                    self.obstacle_y_speed[self.level][num] = -self.obstacle_y_speed[self.level][num]
                else:
                    if self.state == 1:
                        self.obstacle_x_speed[self.level][num] = -self.obstacle_x_speed[self.level][num]
                    elif self.state == 2:
                        self.obstacle_y_speed[self.level][num] = -self.obstacle_y_speed[self.level][num]
                    x1 = self.obstacle_x_pos[self.level][num]
                    x2 = self.obstacle_x_pos[self.level][num]+self.width
                    y1 = self.obstacle_y_pos[self.level][num]
                    y2 = self.obstacle_y_pos[self.level][num]+self.height
                    self.table.move_item(self.obstacle[num], x1, y1, x2, y2)
            else:
                if num < self.obstacle_num[self.level] - self.level:
                    x1 = self.obstacle_x_pos[self.level][num]
                    x2 = self.obstacle_x_pos[self.level][num]+self.width
                    y1 = self.obstacle_y_pos[self.level][num]
                    y2 = self.obstacle_y_pos[self.level][num]+self.height
                    self.table.move_item(self.obstacle[num], x1, y1, x2, y2)
                else:
                    # 공이 왼쪽 벽에 부딪쳤을 때:
                    if(self.obstacle_x_pos[self.level][num] <= 3):
                        self.obstacle_x_pos[self.level][num] = 3
                        self.obstacle_x_speed[self.level][num] = -self.obstacle_x_speed[self.level][num]
                    # 공이 오른쪽 벽에 부딪쳤을 때:
                    if(self.obstacle_x_pos[self.level][num] >= (self.table.width - (self.width - 3))):
                        self.obstacle_x_pos[self.level][num] = (self.table.width - (self.width - 3))
                        self.obstacle_x_speed[self.level][num] = -self.obstacle_x_speed[self.level][num]
                    # 공이 위쪽 벽에 부딪쳤을 때:
                    if(self.obstacle_y_pos[self.level][num] <= 3):
                        self.obstacle_y_pos[self.level][num] = 3
                        self.obstacle_y_speed[self.level][num] = -self.obstacle_y_speed[self.level][num]
                    # 공이 아래쪽 벽에 부딪쳤을 때:
                    if(self.obstacle_y_pos[self.level][num] >= (self.table.height - (self.height - 3))):
                        self.obstacle_y_pos[self.level][num] = (self.table.height - (self.height - 3))
                        self.obstacle_y_speed[self.level][num] = -self.obstacle_y_speed[self.level][num]

                    x1 = self.obstacle_x_pos[self.level][num]
                    x2 = self.obstacle_x_pos[self.level][num]+self.width
                    y1 = self.obstacle_y_pos[self.level][num]
                    y2 = self.obstacle_y_pos[self.level][num]+self.height
                    self.table.move_item(self.obstacle[num], x1, y1, x2, y2)
            
        
        
