import simplegui
import random

sides = {"Right":[1,0], "Left":[-1,0], "Up": [0,1],"Down": [0,-1]}
color = {0: "Red", 1: "Green", 2: "Blue", 3:"Yellow"}

buff = []



fps_counter = 0
fps = "??"

canv_widt = 800
canv_heig = 518

B = -2
O = -1
block_list = []

turn = 0

def fps_viewer():
    global fps, fps_counter
    fps = str(fps_counter)
    fps_counter = 0
    print fps

def load_imgs():
    global img_normal, img_crash, img_count, img_rainbow, img_Ryu, img_back
    img_normal, img_crash, img_count, img_rainbow = [], [], [], []
    for i in range(4):
        img_normal.append([])
        img_crash.append([])
        img_count.append([])
    img_rainbow.append([])
# images for normal gems
    img_normal[0] = simplegui.load_image('http://imageshack.us/a/img703/9500/za9i.png')
    img_normal[1] = simplegui.load_image('http://imageshack.us/a/img202/6861/8mx3.png')
    img_normal[2] = simplegui.load_image('http://imageshack.us/a/img39/9400/i967.png')
    img_normal[3] = simplegui.load_image('http://imageshack.us/a/img23/7307/8ziv.png')
# images for crash gems 
    img_crash[0] = simplegui.load_image('http://imageshack.us/a/img856/9440/5rzy.png')
    img_crash[1] = simplegui.load_image('http://imageshack.us/a/img706/5111/3wxr.png')
    img_crash[2] = simplegui.load_image('http://imageshack.us/a/img716/2875/uavg.png')
    img_crash[3] = simplegui.load_image('http://imageshack.us/a/img209/8376/pr0c.png')
# images for red counter gems    
    img_count[0].append(simplegui.load_image('http://imageshack.us/a/img30/701/8c7k.png'))
    img_count[0].append(simplegui.load_image('http://imageshack.us/a/img703/5185/637y.png'))
    img_count[0].append(simplegui.load_image('http://imageshack.us/a/img834/851/owpv.png'))
    img_count[0].append(simplegui.load_image('http://imageshack.us/a/img713/9972/v55l.png'))
    img_count[0].append(simplegui.load_image('http://imageshack.us/a/img22/4107/1mgz.png'))
# images for green counter gems    
    img_count[1].append(simplegui.load_image('http://imageshack.us/a/img809/9618/h2bb.png'))
    img_count[1].append(simplegui.load_image('http://imageshack.us/a/img194/3100/16i6.png'))
    img_count[1].append(simplegui.load_image('http://imageshack.us/a/img689/3425/7lx3.png'))
    img_count[1].append(simplegui.load_image('http://imageshack.us/a/img34/778/f8gf.png'))
    img_count[1].append(simplegui.load_image('http://imageshack.us/a/img62/8158/wbji.png'))
# images for blue counter gems 
    img_count[2].append(simplegui.load_image('http://imageshack.us/a/img30/9431/1ckc.png'))
    img_count[2].append(simplegui.load_image('http://imageshack.us/a/img689/5158/bi3v.png'))
    img_count[2].append(simplegui.load_image('http://imageshack.us/a/img844/1063/518y.png'))
    img_count[2].append(simplegui.load_image('http://imageshack.us/a/img837/4861/x07j.png'))
    img_count[2].append(simplegui.load_image('http://imageshack.us/a/img546/7747/zj6w.png'))   
# images for yellow counter gems     
    img_count[3].append(simplegui.load_image('http://imageshack.us/a/img9/4663/f887.png'))
    img_count[3].append(simplegui.load_image('http://imageshack.us/a/img855/5057/hbwu.png'))
    img_count[3].append(simplegui.load_image('http://imageshack.us/a/img834/6656/4l35.png'))
    img_count[3].append(simplegui.load_image('http://imageshack.us/a/img401/1011/jrs8.png'))
    img_count[3].append(simplegui.load_image('http://imageshack.us/a/img811/503/7bwl.png'))
# image for rainbow gem    
    img_rainbow[0] = simplegui.load_image('http://imageshack.us/a/img809/6231/z82b.png')
# Ryu
    img_Ryu = simplegui.load_image('http://imageshack.us/a/img401/5/nbzo.png')
# background
    img_back = simplegui.load_image('http://imageshack.us/a/img706/5250/9dtj.png')


class matrix:
    def __init__(self, rows_num, cols_num, xy):
        self.rows_num = rows_num
        self.cols_num = cols_num
        self.xy = [xy[0], xy[1]] # upper right point of the matrix inside the canvas
        self.matrix = []
        for i in range(1,rows_num +1):
            self.matrix.append([gem(B,B,B)])
            for j in range(1, cols_num):
                self.matrix[i-1].append(O)
            self.matrix[i-1].append(gem(B,B,B))
        self.matrix.append([gem(B,B,B) for cols in self.matrix[0]])
        
def draw_matrix(canvas):
    for gem in buff:
        canvas.draw_image(gem[0], (16, 16), (32, 32), gem[1], (32,32)) #gem[0] = img, gem[1] = xy pos
#        for i in range(1,self.rows_num):
#            for j in range(1,self.cols_num):
#                if self.matrix[i][j] <> O:
#                    canvas.draw_image(self.matrix[i][j].kind.img, (16, 16), (32, 32), self.matrix[i][j].xy, (32,32))

class player:
    def __init__(self, matrix):
        self.matrix = matrix
        self.block = block((gem(normal(1), [128,64],self)),(gem(normal(1), [128,32],self)))
        self.score = 0
        self.turn = -1
        self.pattern = 0
        self.fastdrop = False
        self.buffer = []



class normal:
    def __init__(self, color = 0):
        self.img = img_normal[color]
        self.points = 1
        self.color = color
            
    def __str__(self):
        return "Normal; Color: " + str(self.color)
        
class crash:
    def __init__(self, color = 0):
        self.img = img_crash[color]
        self.points = 1
        self.color = color
            
    def __str__(self):
        return "Crash; Color: " + str(self.color)    
        
class diamond:
    def __init__(self, color = None):
        self.img = img_rainbow[0]
        self.multiplier = 0.5
        self.color = 0
        
    def __str__(self):
        return "Diamond"
        
class counter:
    def __init__(self, color = 0, counter = 5):
        self.img = img_count[color][counter-1]
        self.value = counter
        self.color = color
        self.points = 1
            
    def __str__(self):
        return "Counter; Color: " + str(self.color)

class gem:
    def __init__(self, kind, xy, player = None):
        self.kind = kind
        self.player = player
        self.xy = xy
#        self.ij = self.get_ij()
        
    def __str__(self):
        s = []
        s.append("Class: Gem")
        s.append("Kind: " + str(self.kind))
        return str(s)
    
    def get_ij(self, offset = [0,0]):
        return [int((self.xy[1] + offset[1])/32),\
                int((self.xy[0] + offset[0])/32)]
    
    def get_xy(self, offset = [0,0]):
        return [((self.ij[1]*32)+ self.player.matrix.xy[0]),\
                ((self.ij[0]*32)+ self.player.matrix.xy[1])]
    
    def check_bot(self,p_m):
        return p_m.matrix[self.get_ij([0,32])[0]][self.get_ij([0,0])[1]] <> O
    
    def collision(self, side):
        if side == "Down":
            return self.player.matrix.matrix[self.get_ij([0,32])[0]][self.get_ij([0,0])[1]] == O
        elif side == "Left":
            return self.player.matrix.matrix[self.get_ij([0,32])[0]][self.get_ij([-32,0])[1]]== O
        elif side == "Right":
            return self.player.matrix.matrix[self.get_ij([0,32])[0]][self.get_ij([32,0])[1]] == O      
        elif side == "Up":
            return self.player.matrix.matrix[self.get_ij([0,-32])[0]][self.get_ij([0,0])[1]] == O
     
    def move(self, amount):
        self.xy[0] += amount[0]
        self.xy[1] += amount[1]
    

class block:
    def __init__(self, gem1, gem2):
        self.matrix = None
        self.core = gem1
        self.annex = gem2
        self.ang = 0
        self.passo = 1
            
    def draw_gem(self, canvas):
        canvas.draw_image(self.core.kind.img, (16, 16), (32, 32), [self.core.player.matrix.xy[0]+self.core.xy[0], self.core.player.matrix.xy[1]+self.core.xy[1]], [32,32])
        canvas.draw_image(self.annex.kind.img, (16, 16), (32, 32), [self.annex.player.matrix.xy[0]+self.annex.xy[0], self.annex.player.matrix.xy[1]+self.annex.xy[1]], [32,32])
        
    def __str__(self):
        s = []
        s.append("Core: " + str(self.core))
        s.append("Annex: " + str(self.annex))
        return str(s)
    
    def gravity(self, amount = 1):
        if (self.core.check_bot(self.matrix)) or (self.annex.check_bot(self.matrix)):
            self.core.xy = self.core.get_xy()
            self.annex.xy = self.annex.get_xy()
            self.matrix.matrix[self.core.ij[0]][self.core.ij[1]] = self.core
            self.matrix.matrix[self.annex.ij[0]][self.annex.ij[1]] = self.annex
            buff.append([self.core.kind.img, self.core.xy])
            buff.append([self.annex.kind.img, self.annex.xy])
            if self.core.player.matrix.matrix[2][4] == O:
                self.drop_next()                
        elif self.core.player.fastdrop:
            self.core.move([0, 8 - self.core.xy[1]%8])
            self.annex.move([0, 8 - self.annex.xy[1]%8])
        else:
            self.core.move([0, 1])
            self.annex.move([0, 1])
        self.core.ij = self.core.get_ij()
        self.annex.ij = self.annex.get_ij()

    def drop_next(self):
        global turn, ang, passo
        self.ang = 0
        self.passo = 1
        self.core.player.turn += 1
        if self.core.player.turn == turn:
            block_list.append([[kind[random.randrange(0,100)//90],random.randrange(4)], \
                               [kind[random.randrange(0,100)//90],random.randrange(4)]])
            turn += 1
        self.core = gem(block_list[self.core.player.turn][0][0](block_list[self.core.player.turn][0][1]),[128,64],self.core.player)
        self.annex = gem(block_list[self.annex.player.turn][1][0](block_list[self.core.player.turn][1][1]),[128,32], self.core.player)

    def flip(self):
        global ang, passo
        self.annex.xy[1] = (self.core.xy[1]) + (self.ang*32)
        if not (-1 < self.ang < 1):
            self.passo = self.passo*(-1)      
        self.ang += self.passo
        self.annex.xy[0] = (self.core.xy[0]) + (self.ang*32)

        
def update(canvas):
    global fps_counter
    fps_counter += 1
#    canvas.draw_text("FPS: "+ fps, [canv_widt - 100, canv_heig - 5], 24, "White")
#    draw_loading(canvas)
    draw_matrix(canvas)
    if p1.block.core.player.matrix.matrix[2][4] == O:
        p1.block.draw_gem(canvas)
    if p2.block.core.player.matrix.matrix[2][4] == O:
        p2.block.draw_gem(canvas)
    canvas.draw_image(img_back, (304, 211), (608, 422), (416,275), (608, 422))
    p1.block.gravity()
    p2.block.gravity()

    
    
def keydown(key):
    if key == simplegui.KEY_MAP["a"]:
        if p1.block.core.collision("Left") and p1.block.annex.collision("Left"):
            p1.block.core.move([-32,0])
            p1.block.annex.move([-32,0])
            p1.block.core.ij = p1.block.core.get_ij()
            p1.block.annex.ij = p1.block.annex.get_ij()
    elif key == simplegui.KEY_MAP["d"]:
        if p1.block.core.collision("Right") and p1.block.annex.collision("Right"):
            p1.block.core.move([32,0])
            p1.block.annex.move([32,0])
            p1.block.core.ij = p1.block.core.get_ij()
            p1.block.annex.ij = p1.block.annex.get_ij()
    elif key == simplegui.KEY_MAP["s"]:
        p1.fastdrop = True
    elif key == simplegui.KEY_MAP["z"]:
        p1.block.flip()
        
        
    if key == simplegui.KEY_MAP["left"]:
        if p2.block.core.collision("Left") and p2.block.annex.collision("Left"):
            p2.block.core.move([-32,0])
            p2.block.annex.move([-32,0])
            p2.block.core.ij = p2.block.core.get_ij()
            p2.block.annex.ij = p2.block.annex.get_ij()
#            print [gem_teste.ij, gem_teste2.ij]
    elif key == simplegui.KEY_MAP["right"]:
        if p2.block.core.collision("Right") and p2.block.annex.collision("Right"):
            p2.block.core.move([32,0])
            p2.block.annex.move([32,0])
            p2.block.core.ij = p2.block.core.get_ij()
            p2.block.annex.ij = p2.block.annex.get_ij()
    elif key == simplegui.KEY_MAP["down"]:
        p2.fastdrop = True
    elif key == simplegui.KEY_MAP["up"]:
        p2.block.flip()

        
        
def keyup(key):
    global fastdrop_p1, fastdrop_p2
    if key == simplegui.KEY_MAP["s"]:
        p1.fastdrop = False
    if key == simplegui.KEY_MAP["down"]:
        p2.fastdrop = False

        
        
def new_game():
    global m_p1, m_p2, p1, p2, gem1, gem2
    m_p1 = matrix(14, 7, [100,50])
    m_p2 = matrix(14, 7, [508,50])
    p1 = player(m_p1)
    p2 = player(m_p2)
    p1.block.matrix = m_p1
    p2.block.matrix = m_p2
    p1.block.drop_next()
    p2.block.drop_next()

    

    
load_imgs()        
kind = {0: normal, 1: crash, 2: diamond, 3: counter}




new_game()

frame = simplegui.create_frame("Super Puzzle Fighter", canv_widt, canv_heig, 1)
frame.set_draw_handler(update)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

FPStimer = simplegui.create_timer(1000, fps_viewer)
FPStimer.start()
  
frame.start()