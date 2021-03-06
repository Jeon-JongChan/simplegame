import table

class Ball:
    def __init__(self,table,line,width = 10,height = 10,color = "green",x_speed = 0,y_speed = 0,level = 0,life = 1):
        self.width = width
        self.height = height
        self.color = color
        self.table = table
        self.line = line
        self.life = life
        self.level = 0
        self.limit_speed = 2
        self.hard = False
        
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.create_ball()
        
    def create_ball(self):
        self.level = self.table.level
        if  self.line.map_x_pos[self.level][0][0] == self.line.map_x_pos[self.level][0][1]: #첫 구간의 라인이 세로라인일 경우
            self.origin_x = int((self.line.map_x_pos[self.level][0][0] + self.line.map_x_pos[self.level][1][0])/2) +5
            if self.line.map_y_pos[self.level][0][1] == self.line.map_y_pos[self.level][1][1]:
                self.origin_y = self.line.map_y_pos[self.level][0][1] - self.height
            else:
                self.origin_y = self.line.map_y_pos[self.level][0][0] + self.height
        elif self.line.map_y_pos[self.level][0][0] == self.line.map_y_pos[self.level][0][1]: #첫 구간의 라인이 가로라인일 경우
            if self.line.map_x_pos[self.level][0][1] == self.line.map_x_pos[self.level][1][1]:
                self.origin_x = self.line.map_x_pos[self.level][0][1] - self.width
            else:
                self.origin_x = self.line.map_x_pos[self.level][0][0] + self.width
            self.origin_y = int((self.line.map_y_pos[self.level][0][0] + self.line.map_y_pos[self.level][1][0])/2) +5
        self.x_pos = self.origin_x
        self.y_pos = self.origin_y
        self.circle = self.table.draw_oval(self)
        
    def line_collision(self,x_pos,y_pos,width,height,x_speed,y_speed): #라인과 ball이 부딫칠 때
        count  = 0
        for i in range(0,len(self.line.map_x_pos[self.level])): #해당 레벨의 라인 수의 1/2만큼 진행 -> 트랙은 1쌍의 라인으로 구성
            if  self.line.map_x_pos[self.level][i][0] == self.line.map_x_pos[self.level][i][1]: #세로라인일 경우
                if y_pos > self.line.map_y_pos[self.level][i][0] and y_pos <  self.line.map_y_pos[self.level][i][1]:
                    ###세로라인의 길이를 넘지 않는  경우에만 진행
                    if i % 2 == 1: ##[level][0],[level][1] 순으로 라인이 그려져 공간이 구성 되므로
                                   ##나머지가 1이면 현재 배열과 이전 배열과 비교
                        if self.line.map_x_pos[self.level][i][0] < self.line.map_x_pos[self.level][i-1][0]:
                            #현재 라인의 x 축이 다음 배열보다 작으면 안쪽 라인
                            if x_pos + (x_speed + 1)> self.line.map_x_pos[self.level][i][0] and x_pos <  self.line.map_x_pos[self.level][i-1][1]:
                                #현 세로라인의 가로길이를 넘지않았을 경우에만 실행
                                if x_pos - (width + x_speed)< self.line.map_x_pos[self.level][i][0]:
                                    x_pos = self.line.map_x_pos[self.level][i][0] + (width + x_speed)
                                    count = 1
                                    #print('debug 1')
                        else:
                            if x_pos - (x_speed + 1)< self.line.map_x_pos[self.level][i][0] and x_pos >  self.line.map_x_pos[self.level][i-1][1]:
                                if x_pos + (width + x_speed)> self.line.map_x_pos[self.level][i][0]:
                                    x_pos = self.line.map_x_pos[self.level][i][0] - (width + x_speed)
                                    count = 1
                                    #print('debuf 2')

                    else:###나머지가 0 일 경우 현재배열과 다음 배열과 비교
                        if self.line.map_x_pos[self.level][i][0] < self.line.map_x_pos[self.level][i+1][0]:
                            if x_pos + (x_speed + 1)> self.line.map_x_pos[self.level][i][0] and x_pos <  self.line.map_x_pos[self.level][i+1][1]:
                                if x_pos - (width + x_speed) < self.line.map_x_pos[self.level][i][0]:
                                    x_pos = self.line.map_x_pos[self.level][i][0] + (width + x_speed)
                                    count = 1
                                    #print('debuf 3',i)

                        else:
                            if x_pos - (x_speed + 1)< self.line.map_x_pos[self.level][i][0] and x_pos >  self.line.map_x_pos[self.level][i+1][1]:
                                if x_pos + (width + x_speed)> self.line.map_x_pos[self.level][i][0]:     
                                    x_pos = self.line.map_x_pos[self.level][i][0] - (width + x_speed)
                                    count = 1
                                    #print('debuf 4')

            elif self.line.map_y_pos[self.level][i][0] == self.line.map_y_pos[self.level][i][1]: #가로라인일 경우
               if x_pos > self.line.map_x_pos[self.level][i][0] and x_pos <  self.line.map_x_pos[self.level][i][1]:
                   ### 가로라인의 길이를 넘지 않는 경우에만 진행
                    if i % 2 == 1: ##[level][0],[level][1] 순으로 라인이 그려져 공간이 구성 되므로
                                   ##나머지가 1이면 현재 배열과 이전 배열과 비교 
                        if self.line.map_y_pos[self.level][i][0] < self.line.map_y_pos[self.level][i-1][0]:
                            #현재 라인의 x 축이 다음 배열보다 작으면 안쪽 라인
                            if y_pos + (y_speed + 1) > self.line.map_y_pos[self.level][i][0] and y_pos <  self.line.map_y_pos[self.level][i-1][1]:
                                if y_pos - (y_speed + height) < self.line.map_y_pos[self.level][i][0]:
                                    y_pos = self.line.map_y_pos[self.level][i][0] + (height + y_speed)
                                    count = 2
                                    #print('debuf 5')
                        else:
                            if y_pos - (y_speed + 1)< self.line.map_y_pos[self.level][i][0] and y_pos >  self.line.map_y_pos[self.level][i-1][1]:
                                if y_pos + (y_speed + height) > self.line.map_y_pos[self.level][i][0]:
                                    y_pos = self.line.map_y_pos[self.level][i][0] - (height + y_speed)
                                    count = 2
                                    #print('debuf 6')

                    else:##나머지가 0 일 경우 현재배열과 다음 배열과 비교
                        if self.line.map_y_pos[self.level][i][0] < self.line.map_y_pos[self.level][i+1][0]:
                            if y_pos + (y_speed + 1)> self.line.map_y_pos[self.level][i][0] and y_pos <  self.line.map_y_pos[self.level][i+1][1]:
                                if y_pos - (y_speed + height) < self.line.map_y_pos[self.level][i][0]:
                                    y_pos = self.line.map_y_pos[self.level][i][0] + (height + y_speed)
                                    count = 2
                                    #print('debuf 7',i)
                        else:
                            if y_pos - (y_speed + 1)< self.line.map_y_pos[self.level][i][0] and y_pos >  self.line.map_y_pos[self.level][i+1][1]:
                                if y_pos + (y_speed + height)> self.line.map_y_pos[self.level][i][0]:
                                    y_pos = self.line.map_y_pos[self.level][i][0] -  (height + y_speed)
                                    count = 2
                                    #print('debuf 8')

        if count > 0:
            return x_pos,y_pos,count
        else:
            return x_pos,y_pos,count
    def restart_pos(self):
        self.x_pos = self.origin_x
        self.y_pos = self.origin_y
        self.x_speed = 0
        self.y_speed = 0

        x1 = self.x_pos
        x2 = self.x_pos+self.width
        y1 = self.y_pos
        y2 = self.y_pos+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)

    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0
        
    def move_right(self,master):
        if self.x_speed < self.limit_speed:
                    self.x_speed += 1

    def move_left(self,master):
        if self.x_speed > -self.limit_speed:
                    self.x_speed -= 1
    def move_up(self,master):
        if self.y_speed > -self.limit_speed:
                    self.y_speed -= 1
    def move_down(self,master):
        if self.y_speed < self.limit_speed:
                    self.y_speed += 1
    def move_ball(self):
        if self.y_pos + self.y_speed < 800 and self.y_pos - self.y_speed > 0 and self.x_pos - self.x_speed > 0 and self.x_pos + self.x_speed < 800 :
            self.x_pos,self.y_pos,collosion_state = self.line_collision(self.x_pos+self.x_speed,self.y_pos+self.y_speed,self.width,self.height,self.x_speed,self.y_speed)
            if collosion_state > 0 and self.hard:
                self.restart_pos()
            elif collosion_state > 0:
                self.x_speed = 0
                self.y_speed = 0
            else:
                self.x_pos += self.x_speed
                self.y_pos += self.y_speed
                x1 = self.x_pos
                x2 = self.x_pos+self.width
                y1 = self.y_pos
                y2 = self.y_pos+self.height
                self.table.move_item(self.circle, x1, y1, x2, y2)
        else:
            self.restart_pos()
