import table

class Ball:
    def __init__(self,table,line,width = 10,height = 10,color = "green",x_speed = 6,y_speed = 6,level = 0):
        self.width = width
        self.height = height
        self.color = color
        self.table = table
        self.line = line
        self.level = level
    
        self.x_speed = x_speed
        self.y_speed = y_speed
        if  self.line.map_x_pos[level][0][0] == self.line.map_x_pos[level][0][1]: #첫 구간의 라인이 세로라인일 경우
            self.x_pos = int((self.line.map_x_pos[level][0][0] + self.line.map_x_pos[level][1][0])/2)
            self.y_pos = self.line.map_y_pos[level][0][1] - self.height
        elif self.line.map_y_pos[level][0][0] == self.line.map_y_pos[level][0][1]: #첫 구간의 라인이 가로라인일 경우
            self.x_pos = self.line.map_x_pos[level][0][1] - self.height
            self.y_pos = int((self.line.map_y_pos[level][0][0] + self.line.map_y_pos[level][1][0])/2)

        self.circle = self.table.draw_oval(self)
    def line_collision(self,x_pos,y_pos,width,height): #라인과 ball이 부딫칠 때
        count  = 0
        for i in range(0,len(self.line.map_x_pos[self.level])): #해당 레벨의 라인 수의 1/2만큼 진행 -> 트랙은 1쌍의 라인으로 구성
            if  self.line.map_x_pos[self.level][i][0] == self.line.map_x_pos[self.level][i][1]: #세로라인일 경우
                if y_pos > self.line.map_y_pos[self.level][i][0] and y_pos <  self.line.map_y_pos[self.level][i][1]:
                    ###세로라인의 길이를 넘지 않는  경우에만 진행
                    if i % 2 == 1: ##[level][0],[level][1] 순으로 라인이 그려져 공간이 구성 되므로
                                   ##나머지가 1이면 현재 배열과 이전 배열과 비교
                        if self.line.map_x_pos[self.level][i][0] < self.line.map_x_pos[self.level][i-1][0]:
                            #현재 라인의 x 축이 다음 배열보다 작으면 안쪽 라인
                            if x_pos < self.line.map_x_pos[self.level][i][0]:
                                x_pos = self.line.map_x_pos[self.level][i][0] + 1
                                count = 1
                        else:
                            if x_pos + width > self.line.map_x_pos[self.level][i][0]:
                                print(self.level)
                                x_pos = self.line.map_x_pos[self.level][i][0] - width
                                count = 1

                    else:###나머지가 0 일 경우 현재배열과 다음 배열과 비교
                        if self.line.map_x_pos[self.level][i][0] < self.line.map_x_pos[self.level][i+1][0]:
                            if x_pos < self.line.map_x_pos[self.level][i][0]:
                                x_pos = self.line.map_x_pos[self.level][i][0] + 1
                                count = 1

                        else:
                            if x_pos + self.width > self.line.map_x_pos[self.level][i][0]:
                                x_pos = self.line.map_x_pos[self.level][i][0] + width
                                count = 1

            elif self.line.map_y_pos[self.level][i][0] == self.line.map_y_pos[self.level][i][1]: #가로라인일 경우
               if x_pos > self.line.map_x_pos[self.level][i][0] and x_pos <  self.line.map_x_pos[self.level][i][1]:
                   ### 가로라인의 길이를 넘지 않는 경우에만 진행
                    if i % 2 == 1: ##[level][0],[level][1] 순으로 라인이 그려져 공간이 구성 되므로
                                   ##나머지가 1이면 현재 배열과 이전 배열과 비교 
                        if self.line.map_y_pos[self.level][i][0] < self.line.map_y_pos[self.level][i-1][0]:
                            #현재 라인의 x 축이 다음 배열보다 작으면 안쪽 라인
                            if y_pos < self.line.map_y_pos[self.level][i][0]:
                                y_pos = self.line.map_y_pos[self.level][i][0] + 1
                                count = 1
                        else:
                            if y_pos + height > self.line.map_y_pos[self.level][i][0]:
                                y_pos = self.line.map_y_pos[self.level][i][0] - width//2
                                count = 1

                    else:##나머지가 0 일 경우 현재배열과 다음 배열과 비교
                        if self.line.map_y_pos[self.level][i][0] < self.line.map_y_pos[self.level][i+1][0]:
                            if self.y_pos < self.line.map_y_pos[self.level][i][0]:
                                self.y_pos = self.line.map_y_pos[self.level][i][0] + 1
                                count = 1
                        else:
                            if self.y_pos + self.height > self.line.map_y_pos[self.level][i][0]:
                                self.y_pos = self.line.map_y_pos[self.level][i][0] + 1
                                count = 1

        if count == 1:
            return x_pos,y_pos,False
        else:
            return x_pos,y_pos,True
    
    def move_right(self,master):
        if self.x_pos + self.x_speed < 800: #오른쪽 끝에 부딫치지 않을 때
            self.x_pos,self.y_pos,collosion_state = self.line_collision(self.x_pos,self.y_pos,self.width,self.height)
            if collosion_state:
                self.x_pos = self.x_pos + self.x_speed   
            x1 = self.x_pos
            x2 = self.x_pos+self.width
            y1 = self.y_pos
            y2 = self.y_pos+self.height
            self.table.move_item(self.circle, x1, y1, x2, y2)

    def move_left(self,master):
        if self.x_pos - self.x_speed > 0: #왼쪽 끝에 부딫치지 않을 때
            self.x_pos,self.y_pos,collosion_state = self.line_collision(self.x_pos,self.y_pos,self.width,self.height)
            if collosion_state:
                self.x_pos = self.x_pos - self.x_speed
            x1 = self.x_pos
            x2 = self.x_pos+self.width
            y1 = self.y_pos
            y2 = self.y_pos+self.height
            self.table.move_item(self.circle, x1, y1, x2, y2)
        
    def move_up(self,master): 
        if self.y_pos - self.y_speed > 0: #위쪽 끝에 부딫치지 않을 때
            self.x_pos,self.y_pos,collosion_state = self.line_collision(self.x_pos,self.y_pos,self.width,self.height)
            if collosion_state:
                self.y_pos = self.y_pos - self.y_speed
            x1 = self.x_pos
            x2 = self.x_pos+self.width
            y1 = self.y_pos
            y2 = self.y_pos+self.height
            self.table.move_item(self.circle, x1, y1, x2, y2)
        
    def move_down(self,master):
        if self.y_pos + self.y_speed < 800: #아래쪽 끝에 부딫치지 않을 때
            self.x_pos,self.y_pos,collosion_state = self.line_collision(self.x_pos,self.y_pos,self.width,self.height)
            if collosion_state:
                self.y_pos = self.y_pos + self.y_speed
            x1 = self.x_pos
            x2 = self.x_pos+self.width
            y1 = self.y_pos
            y2 = self.y_pos+self.height
            self.table.move_item(self.circle, x1, y1, x2, y2)