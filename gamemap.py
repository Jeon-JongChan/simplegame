import table

class Gamemap:
    def __init__(self,table,level = 0):
        self.level = level
        self.map_x_pos = []
        self.map_y_pos = []
        #맵 구성시 항상 작은 숫자가 [][][0]에 와야된다!
        self.map_x_pos.append([[300,300],[500,500]])
        self.map_y_pos.append([[0,800],[0,800]])

        self.table = table
        self.map_line_num = len(self.map_x_pos[self.level])

        for i in range(0,self.map_line_num):
            self.table.draw_line(line = self,level = self.level,phase = i)
