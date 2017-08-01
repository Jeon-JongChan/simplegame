import table

class Gamemap:
    def __init__(self,table,level = 0):
        self.level = level
        self.map_x_pos = []
        self.map_y_pos = []
        self.map_x_des = []
        self.map_y_des = []
        
        self.map_x_pos.append([[300,300],[500,500]]) #level 0
        self.map_y_pos.append([[0,800],[0,800]])     #level 0
        self.map_x_des.append([300,500])
        self.map_y_des.append([0,20])
        
        self.map_x_pos.append([[0,500],[0,300],  [300,300],[500,500],[300,800],[500,800]])   #level 1
        self.map_y_pos.append([[20,20],[110,110],[110,680],[20,580], [680,680],[580,580]])   #level 1
        self.map_x_des.append([780,800])
        self.map_y_des.append([580,680])
        
        self.map_x_pos.append([[20,800],[90,800], [20,20], [90,90],  [20,800], [90,800]])    #level 2
        self.map_y_pos.append([[20,20], [120,120],[20,680],[120,580],[680,680],[580,580]])   #level 2
        self.map_x_des.append([780,800])
        self.map_y_des.append([580,680])
        
        self.map_x_pos.append([[0,800],[0,750],  [800,800],[750,750],[0,750],  [50,800], [3,3],    [50,50],  [3,800],  [50,800]])    #level 3
        self.map_y_pos.append([[20,20],[120,120],[20,420], [120,320],[320,320],[420,420],[320,700],[420,600],[700,700],[600,600]])   #level 3
        self.map_x_des.append([780,800])
        self.map_y_des.append([600,700])
        
        self.map_x_pos.append([[0,800],[0,750],  [800,800],[750,750],[3,800],  [50,750], [3,3],    [50,50],  [3,700],  [50,650], [700,700],[650,650],[110,700],[180,650],[110,110],[180,180],[110,600],[180,600],[600,600],[600,600]])   #level 4
        self.map_y_pos.append([[20,20],[120,120],[20,700], [120,600],[700,700],[600,600],[170,700],[270,600],[170,170],[270,270],[170,550],[270,450],[550,550],[450,450],[320,550],[390,450],[320,320],[390,390],[320,390],[320,390]])   #level 4
        self.map_x_des.append([580,600])
        self.map_y_des.append([320,390])
        
        self.table = table
        self.draw_map()
        
    def draw_map(self):
        self.level = self.table.level
        self.map_line_num = len(self.map_x_pos[self.level])

        for i in range(0,self.map_line_num):
            self.table.draw_line(line = self,level = self.level,phase = i)

    
