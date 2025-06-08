import pygame
import random
import os

#遊戲初始化
pygame.init()
pygame.mixer.init()

#定義常數

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (30, 30, 30)
BLUE = (0,0,255)

size = (1200, 630)
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("TeTeTeTeTeTeTe Tetris!")
icon = pygame.image.load(os.path.join('Tetris','img','blocks','block 1.png')).convert()
pygame.display.set_icon(icon)

#聲音

music_volume = 5
music_volumes = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
sound_volume = 5
sound_volumes = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
pygame.mixer.music.load(os.path.join('Tetris','Music','Mozart - Rondo Alla Turca (Turkish March) (Electro Swing Remix) by Mr. Jazzek.mp3'))
pygame.mixer.music.play(-1)
button_sound = pygame.mixer.Sound(os.path.join('Tetris','Music','sound_effect','Button sound.mp3'))
one_line = pygame.mixer.Sound(os.path.join('Tetris','Music','sound_effect','one_line.mp3'))
two_line = pygame.mixer.Sound(os.path.join('Tetris','Music','sound_effect','two_line.mp3'))
three_line = pygame.mixer.Sound(os.path.join('Tetris','Music','sound_effect','three_line.mp3'))
four_line = pygame.mixer.Sound(os.path.join('Tetris','Music','sound_effect','four_line.mp3'))
drop_sound = pygame.mixer.Sound(os.path.join('Tetris','Music','sound_effect','drop.mp3'))
rotate_sound = pygame.mixer.Sound(os.path.join('Tetris','Music','sound_effect','rotate.mp3'))
level_up_sound = pygame.mixer.Sound(os.path.join('Tetris','Music','sound_effect','level_up.mp3'))
over_sound = pygame.mixer.Sound(os.path.join('Tetris','Music','sound_effect','game_over.mp3'))

#載入圖片

colors = []
fall_colors = []
for i in range(1,19):
    block = pygame.image.load(os.path.join('Tetris','img','blocks','block {0}.png'.format(i))).convert()
    colors.append(pygame.transform.scale(block,(30,30)))

    fall_block = pygame.image.load(os.path.join('Tetris','img','blocks','block {0}.png'.format(i))).convert()
    fall_block.set_alpha(100)#透明圖
    fall_colors.append(pygame.transform.scale(fall_block,(30,30)))

stop_place_img = pygame.image.load(os.path.join('Tetris','img','stop','stop_place.png')).convert()
stop_place_img = pygame.transform.scale(stop_place_img,(600,300))
continue_0_img = pygame.image.load(os.path.join('Tetris','img','stop','continue_0.png')).convert()
continue_0_img.set_colorkey(BLACK)
continue_0_img = pygame.transform.scale(continue_0_img,(160,160))
continue_1_img = pygame.image.load(os.path.join('Tetris','img','stop','continue_1.png')).convert()
continue_1_img.set_colorkey(BLACK)
continue_1_img = pygame.transform.scale(continue_1_img,(160,160))
continue_2_img = pygame.transform.scale(continue_1_img,(150,150))
restart_0_img = pygame.image.load(os.path.join('Tetris','img','stop','restart_0.png')).convert()
restart_0_img.set_colorkey(BLACK)
restart_0_img = pygame.transform.scale(restart_0_img,(160,160))
restart_1_img = pygame.image.load(os.path.join('Tetris','img','stop','restart_1.png')).convert()
restart_1_img.set_colorkey(BLACK)
restart_1_img = pygame.transform.scale(restart_1_img,(160,160))
restart_2_img = pygame.transform.scale(restart_1_img,(150,150))
quit_0_img = pygame.image.load(os.path.join('Tetris','img','stop','quit_0.png')).convert()
quit_0_img.set_colorkey(BLACK)
quit_0_img = pygame.transform.scale(quit_0_img,(160,160))
quit_1_img = pygame.image.load(os.path.join('Tetris','img','stop','quit_1.png')).convert()
quit_1_img.set_colorkey(BLACK)
quit_1_img = pygame.transform.scale(quit_1_img,(160,160))
quit_2_img = pygame.transform.scale(quit_1_img,(150,150))

game_place_img = pygame.image.load(os.path.join('Tetris','img','game_place.png')).convert()
game_place_img = pygame.transform.scale(game_place_img,(330,630))
background_img = pygame.image.load(os.path.join('Tetris','img','background.png')).convert()
background_img = pygame.transform.scale(background_img,(1200,630))
second_block_place_img = pygame.image.load(os.path.join('Tetris','img','second_block_place.png')).convert()
second_block_place_img = pygame.transform.scale(second_block_place_img,(210,210))
score_place_img = pygame.image.load(os.path.join('Tetris','img','score_place.png')).convert()
score_place_img = pygame.transform.scale(score_place_img,(210,120))
line_place_img = pygame.image.load(os.path.join('Tetris','img','lines_place.png')).convert()
line_place_img = pygame.transform.scale(line_place_img,(180,90))

entrance_butt_0_img = pygame.image.load(os.path.join('Tetris','img','entrance','entrance_play_0.png')).convert()
entrance_butt_0_img.set_colorkey(BLACK)
entrance_butt_0_img = pygame.transform.scale(entrance_butt_0_img,(360,90))
entrance_butt_1_img = pygame.image.load(os.path.join('Tetris','img','entrance','entrance_play_1.png')).convert()
entrance_butt_1_img.set_colorkey(BLACK)
entrance_butt_1_img = pygame.transform.scale(entrance_butt_1_img,(360,90))
entrance_butt_2_img = pygame.transform.scale(entrance_butt_1_img,(350,80))

info_background_img = pygame.image.load(os.path.join('Tetris','img','info','info_background.png')).convert()
info_background_img = pygame.transform.scale(info_background_img,(1100,550))

cancel_0_img = pygame.image.load(os.path.join('Tetris','img','entrance','cancel_0.png')).convert()
cancel_0_img.set_colorkey(BLACK)
cancel_0_img = pygame.transform.scale(cancel_0_img,(80,80))
cancel_1_img = pygame.image.load(os.path.join('Tetris','img','entrance','cancel_1.png')).convert()
cancel_1_img.set_colorkey(BLACK)
cancel_1_img = pygame.transform.scale(cancel_1_img,(80,80))
cancel_2_img = pygame.transform.scale(cancel_1_img,(70,70))

instruct_keyboard_img = pygame.image.load(os.path.join('Tetris','img','info','info_keyboard.png')).convert()
instruct_keyboard_img.set_colorkey(BLACK)
instruct_keyboard_img = pygame.transform.scale(instruct_keyboard_img,(960,480))

info_up_img = pygame.image.load(os.path.join('Tetris','img','info','info_up.png')).convert()
info_up_img.set_colorkey(WHITE)
info_up_img = pygame.transform.scale(info_up_img,(96,96))

info_down_img = pygame.image.load(os.path.join('Tetris','img','info','info_down.png')).convert()
info_down_img.set_colorkey(WHITE)
info_down_img = pygame.transform.scale(info_down_img,(96,96))

info_left_img = pygame.image.load(os.path.join('Tetris','img','info','info_left.png')).convert()
info_left_img.set_colorkey(WHITE)
info_left_img = pygame.transform.scale(info_left_img,(96,96))

info_right_img = pygame.image.load(os.path.join('Tetris','img','info','info_right.png')).convert()
info_right_img.set_colorkey(WHITE)
info_right_img = pygame.transform.scale(info_right_img,(96,96))

info_space_img = pygame.image.load(os.path.join('Tetris','img','info','info_space.png')).convert()
info_space_img.set_colorkey(WHITE)
info_space_img = pygame.transform.scale(info_space_img,(480,96))

info_esc_img = pygame.image.load(os.path.join('Tetris','img','info','info_esc.png')).convert()
info_esc_img.set_colorkey(WHITE)
info_esc_img = pygame.transform.scale(info_esc_img,(96,96))

title_img = pygame.image.load(os.path.join('Tetris','img','title.png')).convert()
title_img.set_colorkey(BLACK)
title_img = pygame.transform.scale(title_img,(660,210))

normal_0_img = pygame.image.load(os.path.join('Tetris','img','info','normal_0.png')).convert()
normal_0_img.set_colorkey(BLACK)
normal_0_img = pygame.transform.scale(normal_0_img,(240,240))
normal_1_img = pygame.image.load(os.path.join('Tetris','img','info','normal_1.png')).convert()
normal_1_img.set_colorkey(BLACK)
normal_1_img = pygame.transform.scale(normal_1_img,(240,240))
normal_2_img = pygame.transform.scale(normal_1_img,(220,220))

fixed_0_img = pygame.image.load(os.path.join('Tetris','img','info','fixed_0.png')).convert()
fixed_0_img.set_colorkey(BLACK)
fixed_0_img = pygame.transform.scale(fixed_0_img,(240,240))
fixed_1_img = pygame.image.load(os.path.join('Tetris','img','info','fixed_1.png')).convert()
fixed_1_img.set_colorkey(BLACK)
fixed_1_img = pygame.transform.scale(fixed_1_img,(240,240))
fixed_2_img = pygame.transform.scale(fixed_1_img,(220,220))

fixed_left_0_img = pygame.image.load(os.path.join('Tetris','img','info','fixed_left_0.png')).convert()
fixed_left_0_img.set_colorkey(BLACK)
fixed_left_0_img = pygame.transform.scale(fixed_left_0_img,(70,90))
fixed_left_1_img = pygame.image.load(os.path.join('Tetris','img','info','fixed_left_1.png')).convert()
fixed_left_1_img.set_colorkey(BLACK)
fixed_left_1_img = pygame.transform.scale(fixed_left_1_img,(70,90))
fixed_left_2_img = pygame.transform.scale(fixed_left_1_img,(60,80))

fixed_right_0_img = pygame.image.load(os.path.join('Tetris','img','info','fixed_right_0.png')).convert()
fixed_right_0_img.set_colorkey(BLACK)
fixed_right_0_img = pygame.transform.scale(fixed_right_0_img,(70,90))
fixed_right_1_img = pygame.image.load(os.path.join('Tetris','img','info','fixed_right_1.png')).convert()
fixed_right_1_img.set_colorkey(BLACK)
fixed_right_1_img = pygame.transform.scale(fixed_right_1_img,(70,90))
fixed_right_2_img = pygame.transform.scale(fixed_right_1_img,(60,80))

music_img = pygame.image.load(os.path.join('Tetris','img','info','music.png')).convert()
music_img.set_colorkey(BLACK)
music_img = pygame.transform.scale(music_img,(160,130))

sound_img = pygame.image.load(os.path.join('Tetris','img','info','sound.png')).convert()
sound_img.set_colorkey(BLACK)
sound_img = pygame.transform.scale(sound_img,(160,130))

tick_place_0_img = pygame.image.load(os.path.join('Tetris','img','info','tick_place_0.png')).convert()
tick_place_0_img.set_colorkey(BLACK)
tick_place_0_img = pygame.transform.scale(tick_place_0_img,(80,80))
tick_place_1_img = pygame.image.load(os.path.join('Tetris','img','info','tick_place_1.png')).convert()
tick_place_1_img.set_colorkey(BLACK)
tick_place_1_img = pygame.transform.scale(tick_place_1_img,(80,80))
tick_place_2_img = pygame.transform.scale(tick_place_1_img,(70,70))

tick_img = pygame.image.load(os.path.join('Tetris','img','info','tick.png')).convert()
tick_img.set_colorkey(BLACK)
tick_img = pygame.transform.scale(tick_img,(120,120))

fox_img = pygame.image.load(os.path.join('Tetris','img','info','purple_fox.png')).convert()
fox_img.set_colorkey(WHITE)
fox_img = pygame.transform.scale(fox_img,(225,275))

record_0_img = pygame.image.load(os.path.join('Tetris','img','info','record_0.png')).convert()
record_0_img.set_colorkey(BLACK)
record_0_img = pygame.transform.scale(record_0_img,(160,90))
record_1_img = pygame.image.load(os.path.join('Tetris','img','info','record_1.png')).convert()
record_1_img.set_colorkey(BLACK)
record_1_img = pygame.transform.scale(record_1_img,(160,90))
record_2_img = pygame.transform.scale(record_1_img,(150,80))

over_back = pygame.image.load(os.path.join('Tetris','img','game_over','over_back.png')).convert()
over_back.set_colorkey(BLACK)
over_back = pygame.transform.scale(over_back,(900,450))

game_over_img = pygame.image.load(os.path.join('Tetris','img','game_over','game_over.png')).convert()
game_over_img.set_colorkey(BLACK)
game_over_img = pygame.transform.scale(game_over_img,(250,130))

over_restart_0_img = pygame.image.load(os.path.join('Tetris','img','game_over','over_restart_0.png')).convert()
over_restart_0_img.set_colorkey(BLACK)
over_restart_0_img = pygame.transform.scale(over_restart_0_img,(180,90))
over_restart_1_img = pygame.image.load(os.path.join('Tetris','img','game_over','over_restart_1.png')).convert()
over_restart_1_img.set_colorkey(BLACK)
over_restart_1_img = pygame.transform.scale(over_restart_1_img,(180,90))
over_restart_2_img = pygame.transform.scale(over_restart_1_img,(170,80))

over_quit_0_img = pygame.image.load(os.path.join('Tetris','img','game_over','over_quit_0.png')).convert()
over_quit_0_img.set_colorkey(BLACK)
over_quit_0_img = pygame.transform.scale(over_quit_0_img,(180,90))
over_quit_1_img = pygame.image.load(os.path.join('Tetris','img','game_over','over_quit_1.png')).convert()
over_quit_1_img.set_colorkey(BLACK)
over_quit_1_img = pygame.transform.scale(over_quit_1_img,(180,90))
over_quit_2_img = pygame.transform.scale(over_quit_1_img,(170,80))

score_img = pygame.image.load(os.path.join('Tetris','img','game_over','score.png')).convert()
score_img.set_colorkey(BLACK)
score_img = pygame.transform.scale(score_img,(225,100))

lines_img = pygame.image.load(os.path.join('Tetris','img','game_over','lines.png')).convert()
lines_img.set_colorkey(BLACK)
lines_img = pygame.transform.scale(lines_img,(225,100))

level_img = pygame.image.load(os.path.join('Tetris','img','game_over','level.png')).convert()
level_img.set_colorkey(BLACK)
level_img = pygame.transform.scale(level_img,(225,100))

done_0_img = pygame.image.load(os.path.join('Tetris','img','info','done_0.png')).convert()
done_0_img.set_colorkey(BLACK)
done_0_img = pygame.transform.scale(done_0_img,(240,80))
done_1_img = pygame.image.load(os.path.join('Tetris','img','info','done_1.png')).convert()
done_1_img.set_colorkey(BLACK)
done_1_img = pygame.transform.scale(done_1_img,(240,80))
done_2_img = pygame.transform.scale(done_1_img,(230,70))

highest_img = pygame.image.load(os.path.join('Tetris','img','info','highest.png')).convert()
highest_img.set_colorkey(BLACK)
highest_img = pygame.transform.scale(highest_img,(430,70))


class Figure():
    x = 0
    y = 0

    figures = [
        [[8, 9, 10, 11], [2, 6, 10, 14]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10], [1, 2, 5, 9]],
        [[3, 5, 6, 7], [1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[5, 6, 9, 10]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        if self.type == 0 or self.type == 1 or self.type == 2 or self.type == 6:
            self.y = self.y-1
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
            

class Tetris():
    def __init__(self, height, width):
        self.level = 0
        self.score = 0
        self.state = "start"
        self.field = []
        self.fall_field = []
        self.height = height
        self.width = width
        self.x = 450
        self.y = 15
        self.zoom = 30  #格子大小
        self.figure = Figure(3,-1)
        self.second_figure = Figure(3,-1)
        self.lines = 0
        self.count_line = 0
        self.speed = 48
        
        for i in range(height+1):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)#field內0=無方塊
            self.fall_field.append(new_line)

    def new_figure(self):
        self.second_figure = Figure(3, -1)

    def intersects(self,x,y):
        intersection = False
        for i in range(4):#以4*4矩陣檢測，矩陣左上角為Figure的(0,0)
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + y > self.height - 1 or \
                            j + x > self.width - 1 or \
                            j + x < 0 or \
                            self.field[i + y][j + x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        score = 0
        for i in range(0, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 0, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        if lines == 1:
            score = 40
            one_line.play()
        elif lines == 2:
            score = 100
            two_line.play()
        elif lines == 3:
            score = 300
            three_line.play()
        elif lines == 4:
            score = 1200
            four_line.play()
        self.score += score
        self.lines += lines
        self.count_line += lines

    def go_space(self):
        while not self.intersects(self.figure.x,self.figure.y):
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        ff = False
        if self.intersects(self.figure.x,self.figure.y):
            self.figure.y -= 1
            ff = True
            self.freeze()
        return ff

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.figure = self.second_figure
        self.new_figure()
        drop_sound.play()
        if self.intersects(self.figure.x,self.figure.y):
            self.state = "gameover"
            over_sound.play()
        

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects(self.figure.x,self.figure.y):
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects(self.figure.x,self.figure.y):
            self.figure.rotation = old_rotation
        rotate_sound.play()
            
    def fall_pos(self):
        x = self.figure.x
        y = self.figure.y
        self.fall_field=[]
        for i in range(self.height+1):
            new_line = []
            for j in range(self.width):
                new_line.append(0)
            self.fall_field.append(new_line)
        while not self.intersects(x,y):
            y += 1
        y -= 1
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.fall_field[i + y][j + x] = self.figure.color
                    
    def level_up(self):
        if self.level < 9:
            if self.count_line >= (self.level*10+10):
                self.level += 1
                level_up_sound.play()
                self.count_line = 0
        elif 9 <= self.level < 16:
            if self.count_line >= 100:
                self.level += 1
                level_up_sound.play()
                self.count_line = 0
        elif 16 <= self.level < 19:
            if self.count_line >= (self.level-5)*11:
                self.level += 1
                level_up_sound.play()
                self.count_line = 0
        elif 19 <= self.level:
            if self.count_line >= 10:
                self.level += 1
                level_up_sound.play()
                self.count_line = 0
    def speed_detect(self):
        if self.level < 9:
            self.speed = (48-self.level*5)
        elif self.level == 9:
            self.speed = 6
        elif 10 <= self.level < 13:
            self.speed = 5
        elif 13 <= self.level < 16:
            self.speed = 4
        elif 16 <= self.level < 19:
            self.speed = 3
        elif self.level >= 19:
            self.speed = 2

class Button(): #img0為按鈕平常樣子，鼠標在上面變img1，按下去變img2
    state_idle = 'idle' #按鈕放開向上，鼠標沒停在按鈕上
    state_armed = 'armed' #按鈕按下，鼠標停在按鈕上
    state_disarmed = 'disarmed' #按著按鈕，鼠標移出按鈕
    state_disarmed2 = 'disarmed2' #沒按按鈕，鼠標停在按鈕上
    def __init__(self,screen,img0,img1,img2,centerx,centery):
        self.screen = screen
        self.img0 = img0
        self.img1 = img1
        self.img2 = img2
        self.centerx = centerx
        self.centery = centery
        
        self.img_0_rect = self.img0.get_rect()
        self.img_0_rect.center = (centerx,centery)
        self.img_1_rect = self.img1.get_rect()
        self.img_1_rect.center = (centerx,centery)
        self.img_2_rect = self.img2.get_rect()
        self.img_2_rect.center = (centerx,centery)
        
        self.state = Button.state_idle
        
        self.use = True #使用按鈕
    def handle_event(self,event):
        if self.use: #按鈕啟用
            #按下按鈕，返回True
            if event.type not in (pygame.MOUSEMOTION,pygame.MOUSEBUTTONUP,pygame.MOUSEBUTTONDOWN):
                return False
            collide_button = self.img_0_rect.collidepoint(pygame.mouse.get_pos())
            if  self.state == Button.state_idle and collide_button:
                self.state = Button.state_disarmed2
            elif self.state == Button.state_disarmed2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and collide_button:
                    self.state = Button.state_armed
                if not collide_button:
                    self.state = Button.state_idle
            elif self.state == Button.state_armed:
                if event.type == pygame.MOUSEBUTTONUP and collide_button:
                    #按成功
                    self.state = Button.state_idle
                    return True
                if event.type ==pygame.MOUSEMOTION and not collide_button:
                    self.state = Button.state_disarmed
            elif self.state == Button.state_disarmed:
                if collide_button:
                    self.state = Button.state_armed
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.state = Button.state_idle
            return False
        return False
    def draw(self):
        collide_button = self.img_0_rect.collidepoint(pygame.mouse.get_pos())
        if self.use == True:
            if  self.state == Button.state_idle and collide_button:
                self.state = Button.state_disarmed2
        if self.state == Button.state_armed or self.state == Button.state_disarmed:
            self.screen.blit(self.img2,self.img_2_rect)
        elif self.state == Button.state_disarmed2:
            self.screen.blit(self.img1,self.img_1_rect)
        else:
            self.screen.blit(self.img0,self.img_0_rect)
    
    def reset(self):#避免重開後按鈕還是亮著
        self.state = Button.state_idle
                

def img_draw(screen,img,centerx,centery):
    #只要是surface就能畫
    img_rect = img.get_rect()
    img_rect.center = (centerx,centery)
    screen.blit(img,img_rect)
    
class entrance_block(): #畫主畫面背景掉的方塊
    def __init__(self):
        self.figure = Figure(random.randint(1,37),random.randint(-50,-2))
    def draw(self,screen):
        for i in range(4): #畫墜落中的方塊
                for j in range(4):
                    p = i * 4 + j
                    if p in self.figure.image():
                        if i + self.figure.y>=0:
                            screen.blit(colors[self.figure.color],(30*(j+self.figure.x),30*(i+self.figure.y)))
    def detect(self):
        if self.figure.y > 21:
            self.figure = Figure(random.randint(1,37),random.randint(-50,-2))
    
    
    

#紀錄

with open('./Tetris/record.txt','r') as f:
    best_score=int(f.readline())
    best_lines=int(f.readline())
    best_level=int(f.readline())

#字體
font_name = os.path.join('Tetris','font','minecraft.ttf')
font = pygame.font.Font(font_name, 30)
font1 = pygame.font.Font(font_name, 50)
font2 = pygame.font.Font(font_name, 40)
font3 = pygame.font.Font(font_name,20)
font4 = pygame.font.Font(font_name,25)
font5 = pygame.font.Font(font_name, 45)
font6 = pygame.font.Font(font_name, 35)

#宣告 
all_screen_black = pygame.Surface((1200,630))
all_screen_black.fill(BLACK)
all_screen_black.set_alpha(150)
running = True
player_state = 'entrance'
clock = pygame.time.Clock()
fps = 60
game = Tetris(20, 10)
counter = 0
pressing_down = False
stop_continue = Button(screen,continue_0_img,continue_1_img,continue_2_img,423,300)
stop_continue.use = False
stop_restart = Button(screen,restart_0_img,restart_1_img,restart_2_img,600,300)
stop_restart.use = False
stop_quit = Button(screen,quit_0_img,quit_1_img,quit_2_img,780,300)
stop_quit.use = False
game_entrance = [entrance_block() for i in range(7)]



#主畫面按鈕
play_0_img,play_1_img,play_2_img = entrance_butt_0_img.copy(),entrance_butt_1_img.copy(),entrance_butt_2_img.copy()
text_play_0_1 = font5.render("Play", True, WHITE)
img_draw(play_0_img,text_play_0_1,180,45)
img_draw(play_1_img,text_play_0_1,180,45)
text_play_2 = font2.render("Play", True, WHITE)
img_draw(play_2_img,text_play_2,175,40)
entrance_play = Button(screen,play_0_img,play_1_img,play_2_img,600,315)

opt_0_img,opt_1_img,opt_2_img = entrance_butt_0_img.copy(),entrance_butt_1_img.copy(),entrance_butt_2_img.copy()
text_option_0_1 = font5.render("Option", True, WHITE)
img_draw(opt_0_img,text_option_0_1,180,45)
img_draw(opt_1_img,text_option_0_1,180,45)
text_option_2 = font2.render("Option", True, WHITE)
img_draw(opt_2_img,text_option_2,175,40)
entrance_opt = Button(screen,opt_0_img,opt_1_img,opt_2_img,600,435)

instruct_0_img,instruct_1_img,instruct_2_img = entrance_butt_0_img.copy(),entrance_butt_1_img.copy(),entrance_butt_2_img.copy()
text_instruct_0_1 = font5.render("Instruction", True, WHITE)
img_draw(instruct_0_img,text_instruct_0_1,180,45)
img_draw(instruct_1_img,text_instruct_0_1,180,45)
text_instruct_2 = font2.render("Instruction", True, WHITE)
img_draw(instruct_2_img,text_instruct_2,175,40)
entrance_instruct = Button(screen,instruct_0_img,instruct_1_img,instruct_2_img,600,555)

cancel = Button(screen,cancel_0_img,cancel_1_img,cancel_2_img,1120,70)
cancel.use = False

instruct_detect = False
play_detect = False
opt_detect = False

normal_mode = Button(screen,normal_0_img,normal_1_img,normal_2_img,360,240)
normal_mode.use = False

fixed_mode = Button(screen,fixed_0_img,fixed_1_img,fixed_2_img,840,240)
fixed_mode.use = False
fixed_level = 0
fixed_levels = [0,1,2,3,4,5,6,7,8,9,10,13,16,19]
fixed_left = Button(screen,fixed_left_0_img,fixed_left_1_img,fixed_left_2_img,755,470)
fixed_left.use = False
fixed_right = Button(screen,fixed_right_0_img,fixed_right_1_img,fixed_right_2_img,925,470)
fixed_right.use = False

music_left = Button(screen,fixed_left_0_img,fixed_left_1_img,fixed_left_2_img,400,150)
music_left.use = False
music_right = Button(screen,fixed_right_0_img,fixed_right_1_img,fixed_right_2_img,700,150)
music_right.use = False

sound_left = Button(screen,fixed_left_0_img,fixed_left_1_img,fixed_left_2_img,400,350)
sound_left.use = False
sound_right = Button(screen,fixed_right_0_img,fixed_right_1_img,fixed_right_2_img,700,350)
sound_right.use = False

tick_place = Button(screen,tick_place_0_img,tick_place_1_img,tick_place_2_img,300,500)
tick_place.use = False
tick_detect = True

record_butt = Button(screen,record_0_img,record_1_img,record_2_img,360,470)
record_butt.use = False

over_restart =  Button(screen,over_restart_0_img,over_restart_1_img,over_restart_2_img,350,450)
over_restart.use = False

over_quit =  Button(screen,over_quit_0_img,over_quit_1_img,over_quit_2_img,850,450)
over_quit.use = False

text_down_0 = font.render('Down',True,WHITE)
text_down_2 = font4.render('Down',True,WHITE)
img_draw(done_0_img,text_down_0,120,40)
img_draw(done_1_img,text_down_0,120,40)
img_draw(done_2_img,text_down_2,115,35)

record_detect = False
rec_done = Button(screen,done_0_img,done_1_img,done_2_img,600,450)
rec_done.use = False


#遊戲迴圈
while running:
    pygame.mixer.music.set_volume(music_volumes[music_volume])
    pygame.mixer.Sound.set_volume(button_sound,sound_volumes[sound_volume])
    pygame.mixer.Sound.set_volume(one_line,sound_volumes[sound_volume])
    pygame.mixer.Sound.set_volume(two_line,sound_volumes[sound_volume])
    pygame.mixer.Sound.set_volume(three_line,sound_volumes[sound_volume])
    pygame.mixer.Sound.set_volume(four_line,sound_volumes[sound_volume])
    pygame.mixer.Sound.set_volume(drop_sound,sound_volumes[sound_volume])
    pygame.mixer.Sound.set_volume(rotate_sound,sound_volumes[sound_volume])
    pygame.mixer.Sound.set_volume(level_up_sound,sound_volumes[sound_volume])
    pygame.mixer.Sound.set_volume(over_sound,sound_volumes[sound_volume])
    if player_state == 'entrance':
        screen.fill(BLACK)
        screen.blit(background_img,(0,0))
        screen.blit(all_screen_black,(0,0))
        screen.blit(all_screen_black,(0,0))
        
        for i in range(len(game_entrance)):#畫背景掉落
            game_entrance[i].draw(screen)
            game_entrance[i].figure.y+=1
            game_entrance[i].detect()
            
        img_draw(screen,title_img,600,135)

        entrance_play.draw()
        entrance_opt.draw()
        entrance_instruct.draw()
        
        if play_detect == True:
            if not record_detect:
                cancel.use = True
                normal_mode.use = True
                fixed_mode.use = True
                fixed_left.use = True
                fixed_right.use = True
                record_butt.use = True
            entrance_play.use = False
            entrance_opt.use = False
            entrance_instruct.use = False
            screen.blit(all_screen_black,(0,0))
            img_draw(screen,info_background_img,600,315)
            cancel.draw()
            normal_mode.draw()
            text_normal = font.render('Normal Mode',True,WHITE)
            img_draw(screen,text_normal,360,400)
            
            fixed_mode.draw()
            text_fixed = font.render('Fixed Mode',True,WHITE)
            img_draw(screen,text_fixed,840,400)

            fixed_level_back = pygame.Surface((170,80))
            fixed_level_back.fill(BLACK)
            text_fixed_level = font1.render(str(fixed_levels[fixed_level]),True,WHITE)
            img_draw(fixed_level_back,text_fixed_level,85,40)
            img_draw(screen,fixed_level_back,840,470)
            
            
            fixed_left.draw()
            
            fixed_right.draw()
            
            text_choose = font3.render('Choose Level',True,WHITE)
            img_draw(screen,text_choose,840,540)
            
            
            record_butt.draw()
            
            text_record = font3.render('Record',True,WHITE)
            img_draw(screen,text_record,360,540)
            
            
        if opt_detect == True:
            entrance_play.use = False
            entrance_opt.use = False
            entrance_instruct.use = False
            cancel.use = True
            music_left.use = True
            music_right.use = True
            sound_left.use = True
            sound_right.use = True
            tick_place.use = True
            screen.blit(all_screen_black,(0,0))
            img_draw(screen,info_background_img,600,315)
            cancel.draw()
            img_draw(screen,music_img,200,150)
            img_draw(screen,sound_img,200,350)
            music_back = pygame.Surface((300,80))
            music_back.fill(BLACK)
            sound_back = music_back.copy()
            text_music_vol = font1.render(str(music_volume*10)+'  %',True,WHITE)
            img_draw(music_back,text_music_vol,150,40)
            text_sound_vol = font1.render(str(sound_volume*10)+'  %',True,WHITE)
            img_draw(sound_back,text_sound_vol,150,40)
            img_draw(screen,music_back,550,150)
            img_draw(screen,sound_back,550,350)
            text_music = font.render('Background Music',True,WHITE)
            img_draw(screen,text_music,550,220)
            text_sound = font.render('Sound Effect',True,WHITE)
            img_draw(screen,text_sound,550,420)
            music_left.draw()
            music_right.draw()
            sound_left.draw()
            sound_right.draw()
            tick_place.draw()
            text_show_fall_pos = font6.render('Show the position blocks will fall to',True,WHITE)
            img_draw(screen,text_show_fall_pos,720,500)
            if tick_detect:
                img_draw(screen,tick_img,315,470)
            img_draw(screen,fox_img,950,250)
            text_fox_0 = font3.render('Presented By',True,WHITE)
            text_fox_1 = font3.render('7tail_Purple_Fox',True,WHITE)
            img_draw(screen,text_fox_0,950,400)
            img_draw(screen,text_fox_1,950,430)
        
        if instruct_detect == True:
            entrance_play.use = False
            entrance_opt.use = False
            entrance_instruct.use = False
            cancel.use = True
            screen.blit(all_screen_black,(0,0))
            img_draw(screen,info_background_img,600,315)
            cancel.draw()
            
            img_draw(screen,instruct_keyboard_img,600,315)
            img_draw(screen,info_up_img,850,315)
            img_draw(screen,info_down_img,850,420)
            img_draw(screen,info_left_img,745,420)
            img_draw(screen,info_right_img,955,420)
            img_draw(screen,info_space_img,450,420)
            img_draw(screen,info_esc_img,195,150)
            text_dir_vertical = font2.render('|',True,WHITE)
            img_draw(screen,text_dir_vertical,850,495)
            img_draw(screen,text_dir_vertical,745,345)
            img_draw(screen,text_dir_vertical,955,345)
            img_draw(screen,text_dir_vertical,850,240)
            img_draw(screen,text_dir_vertical,450,495)
            text_dir_horical = font2.render('-',True,WHITE)
            img_draw(screen,text_dir_horical,270,150)
            img_draw(screen,text_dir_horical,290,150)
            text_info_down = font4.render('Go down swiftly',True,WHITE)
            img_draw(screen,text_info_down,850,525)
            text_info_up = font4.render('Rotate',True,WHITE)
            img_draw(screen,text_info_up,850,200)
            text_info_left = font4.render('Go left',True,WHITE)
            img_draw(screen,text_info_left,745,305)
            text_info_right = font4.render('Go right',True,WHITE)
            img_draw(screen,text_info_right,958,305)
            text_info_space = font4.render('Go down immediately',True,WHITE)
            img_draw(screen,text_info_space,450,525)
            text_info_esc = font4.render('Pause',True,WHITE)
            img_draw(screen,text_info_esc,360,150)
            
        if record_detect ==True:
            cancel.use = False
            normal_mode.use = False
            fixed_mode.use = False
            fixed_left.use = False
            fixed_right.use = False
            rec_done.use = True
            screen.blit(all_screen_black,(0,0))
            img_draw(screen,over_back,600,315)
            record_black = pygame.Surface((225,100))
            record_black.fill(BLACK)
            img_draw(screen,record_black,350,330)
            img_draw(screen,record_black,600,330)
            img_draw(screen,record_black,850,330)
            img_draw(screen,score_img,350,230)
            img_draw(screen,lines_img,600,230)
            img_draw(screen,level_img,850,230)
            text_record_score = font2.render(str(best_score),True,WHITE)
            img_draw(screen,text_record_score,350,330)
            text_record_lines = font2.render(str(best_lines),True,WHITE)
            img_draw(screen,text_record_lines,600,330)
            text_record_level = font2.render(str(best_level),True,WHITE)
            img_draw(screen,text_record_level,850,330)
            rec_done.draw()
            img_draw(screen,highest_img,600,110)
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if instruct_detect == True:
                if cancel.handle_event(event):
                    instruct_detect = False
                    entrance_play.use = True
                    entrance_opt.use = True
                    entrance_instruct.use = True
                    cancel.use = False
                    
            if play_detect == True:
                if cancel.handle_event(event):
                    play_detect = False
                    entrance_play.use = True
                    entrance_opt.use = True
                    entrance_instruct.use = True
                    cancel.use = False
                    normal_mode.use = False
                    fixed_mode.use = False
                    fixed_left.use = False
                    fixed_right.use = False
                    record_butt.use = False
                elif normal_mode.handle_event(event):
                    player_state = 'normal_game'
                    play_detect = False
                    cancel.use = False
                    normal_mode.use = False
                    fixed_mode.use = False
                    fixed_left.use = False
                    fixed_right.use = False
                    record_butt.use = False
                elif fixed_mode.handle_event(event):
                    player_state = 'fixed_game'
                    play_detect = False
                    cancel.use = False
                    normal_mode.use = False
                    fixed_mode.use = False
                    fixed_left.use = False
                    fixed_right.use = False
                    record_butt.use = False
                elif fixed_left.handle_event(event):
                    fixed_level -= 1
                    if fixed_level < 0:
                        fixed_level = 0
                elif fixed_right.handle_event(event):
                    fixed_level += 1
                    if fixed_level > len(fixed_levels)-1:
                        fixed_level = len(fixed_levels)-1
                elif record_detect:
                    if rec_done.handle_event(event):
                        record_detect = False
                        rec_done.use = False
                        cancel.use = True
                        normal_mode.use = True
                        fixed_mode.use = True
                        fixed_left.use = True
                        fixed_right.use = True
                        record_butt.use = True
                        record_butt.reset()
                elif record_butt.handle_event(event):
                    record_detect = True
                    cancel.use = False
                    normal_mode.use = False
                    fixed_mode.use = False
                    fixed_left.use = False
                    fixed_right.use = False
                    record_butt.use = False
                    
                
            
            if opt_detect == True:
                if cancel.handle_event(event):
                    opt_detect = False
                    entrance_play.use = True
                    entrance_opt.use = True
                    entrance_instruct.use = True
                    cancel.use = False
                    music_left.use = False
                    music_right.use = False
                    sound_left.use = False
                    sound_right.use = False
                    tick_place.use = False
                elif music_left.handle_event(event):
                    music_volume -= 1
                    if music_volume < 0:
                        music_volume = 0
                elif music_right.handle_event(event):
                    music_volume += 1
                    if music_volume > len(music_volumes)-1:
                        music_volume = len(music_volumes)-1
                elif sound_left.handle_event(event):
                    sound_volume -= 1
                    if sound_volume < 0:
                        sound_volume = 0
                elif sound_right.handle_event(event):
                    sound_volume += 1
                    if sound_volume > len(sound_volumes)-1:
                        sound_volume = len(sound_volumes)-1
                elif tick_place.handle_event(event):
                    if tick_detect:
                        tick_detect = False
                    else:
                        tick_detect = True
                        
            
            if entrance_play.handle_event(event):
                play_detect = True
            if entrance_opt.handle_event(event):
                opt_detect = True
            if entrance_instruct.handle_event(event):
                instruct_detect = True
            
        
    elif player_state[-4:] == 'game':
        if player_state == 'normal_game':
            game.level_up()
            game.speed_detect()
        if player_state == 'fixed_game':
            game.level = fixed_levels[fixed_level]
            game.speed_detect()
        if game.state == 'start':
            counter += 1
        if counter > 1000000 :
            counter = 0
        #讓方塊往下
        if counter % (game.speed) == 0 or pressing_down:
            if game.state == "start":
                if game.go_down():#重製時間
                    counter = 0
        
        #事件偵測
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game.state == 'start':
                    if event.key == pygame.K_UP:
                        game.rotate()
                    if event.key == pygame.K_DOWN:
                        pressing_down = True
                    if event.key == pygame.K_LEFT:
                        game.go_side(-1)
                    if event.key == pygame.K_RIGHT:
                        game.go_side(1)
                    if event.key == pygame.K_SPACE:
                        game.go_space()
                        counter = 0 #重製時間
                if event.key == pygame.K_ESCAPE:
                    if game.state == 'stop':
                        game.state = 'start'
                    elif game.state == 'start':
                        game.state = 'stop'
                        stop_continue.reset()
                        stop_restart.reset()
                        stop_quit.reset()
            if event.type == pygame.KEYUP:  #放開按鍵
                if event.key == pygame.K_DOWN:
                    pressing_down = False
                
                
            if stop_continue.handle_event(event):
                game.state = 'start'
            if stop_restart.handle_event(event):
                game.__init__(20, 10)
                game.new_figure()
                counter = 0
            if stop_quit.handle_event(event):
                game.__init__(20, 10)
                player_state = 'entrance'
                entrance_play.use = True
                entrance_opt.use = True
                entrance_instruct.use = True
                entrance_play.reset()
                entrance_opt.reset()
                entrance_instruct.reset()
            if over_restart.handle_event(event):
                game.__init__(20, 10)
                game.new_figure()
                counter = 0
                over_restart.reset()
                over_quit.reset()
            if over_quit.handle_event(event):
                game.__init__(20, 10)
                player_state = 'entrance'
                entrance_play.use = True
                entrance_opt.use = True
                entrance_instruct.use = True
                entrance_play.reset()
                entrance_opt.reset()
                entrance_instruct.reset()
                over_quit.use = False
                over_restart.use = False
                over_restart.reset()
                over_quit.reset()
        
        
        #畫面顯示
        screen.fill(WHITE)
        screen.blit(background_img,(0,0))
        screen.blit(all_screen_black,(0,0))
        
        img_draw(screen,game_place_img,600,315)
        img_draw(screen,second_block_place_img,975,405)
        img_draw(screen,score_place_img,225,120)
        img_draw(screen,line_place_img,225,255)
        img_draw(screen,score_place_img,975,150)
        text_next = font2.render("Next:", True, WHITE)
        img_draw(screen,text_next,975,345)
        text_score = font.render("Score:", True, WHITE)
        img_draw(screen,text_score,225,100)
        text_scores = font4.render(str(game.score), True, WHITE)
        img_draw(screen,text_scores,225,140)
        text_lines = font.render('Lines:', True, WHITE)
        img_draw(screen,text_lines,225,240)
        text_lines = font4.render(str(game.lines), True, WHITE)
        img_draw(screen,text_lines,225,275)
        text_level = font.render("Level:", True, WHITE)
        img_draw(screen,text_level,975,130)
        text_levels = font.render(str(game.level), True, WHITE)
        img_draw(screen,text_levels,975,170)
        
        for i in range(4): #畫接下來的方塊
            for j in range(4):
                p = i * 4 + j
                if game.second_figure.type == 0:
                    sec_x = 915
                    sec_y = 360
                elif game.second_figure.type == 1:
                    sec_x = 930
                    sec_y = 375
                elif game.second_figure.type == 2:
                    sec_x = 900
                    sec_y = 375
                elif game.second_figure.type == 3:
                    sec_x = 930
                    sec_y = 405
                elif game.second_figure.type == 4:
                    sec_x = 900
                    sec_y = 405
                elif game.second_figure.type == 5:
                    sec_x = 930
                    sec_y = 405
                elif game.second_figure.type == 6:
                    sec_x = 915
                    sec_y = 375
                if p in game.second_figure.image():
                    screen.blit(colors[game.second_figure.color],(sec_x+game.zoom*j,sec_y + game.zoom * i))
        
        #畫遊戲區域
        for i in range(game.height):
            for j in range(game.width): #畫格子
                pygame.draw.rect(screen, GRAY, 
                                [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:    #畫已掉下去的方塊
                    screen.blit(colors[game.field[i][j]],(game.x + game.zoom * j, game.y + game.zoom * i))
                if tick_detect:
                    if game.fall_field[i][j] > 0: #畫掉下去的位置
                        screen.blit(fall_colors[game.fall_field[i][j]],(game.x + game.zoom * j, game.y + game.zoom * i))
        
        for i in range(4): #畫墜落中的方塊
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    if i + game.figure.y>=0:
                        screen.blit(colors[game.figure.color],(game.x+game.zoom*(j + game.figure.x),game.y + game.zoom * (i + game.figure.y)))
                        

        if game.state == 'start':
            game.fall_pos()
            stop_continue.use = False
            stop_restart.use = False
            stop_quit.use = False
            over_restart.use = False
            over_quit.use = False
        
        if game.state == 'stop':
            screen.blit(all_screen_black,(0,0))
            img_draw(screen,stop_place_img,600,300)
            text_pause = font.render("Pause",True,WHITE)
            img_draw(screen,text_pause,600,200)
            text_restart = font3.render("Resrart",True,WHITE)
            img_draw(screen,text_restart,600,405)
            text_continue = font3.render("Continue",True,WHITE)
            img_draw(screen,text_continue,420,405)
            text_quit = font3.render("Quit",True,WHITE)
            img_draw(screen,text_quit,780,405)
            
            stop_continue.use = True
            stop_continue.draw()
            stop_restart.use = True
            stop_restart.draw()
            stop_quit.use = True
            stop_quit.draw()
            
        
        if game.state == "gameover":
            screen.blit(all_screen_black,(0,0))
            img_draw(screen,over_back,600,315)
            img_draw(screen,game_over_img,600,110)
            over_restart.use = True
            over_restart.draw()
            over_quit.use = True
            over_quit.draw()
            over_black = pygame.Surface((225,100))
            over_black.fill(BLACK)
            img_draw(screen,over_black,350,330)
            img_draw(screen,over_black,600,330)
            img_draw(screen,over_black,850,330)
            img_draw(screen,score_img,350,230)
            img_draw(screen,lines_img,600,230)
            img_draw(screen,level_img,850,230)
            text_over_score = font2.render(str(game.score),True,WHITE)
            img_draw(screen,text_over_score,350,330)
            text_over_lines = font2.render(str(game.lines),True,WHITE)
            img_draw(screen,text_over_lines,600,330)
            text_over_level = font2.render(str(game.level),True,WHITE)
            img_draw(screen,text_over_level,850,330)
            
            if player_state == 'normal_game':
                if game.score > best_score:
                    best_score = game.score
                if game.lines > best_lines:
                    best_lines = game.lines
                if game.level > best_level:
                    best_level = game.level
            
    #遊戲更新
    pygame.display.flip()
    clock.tick(fps)

#紀錄

with open('./Tetris/record.txt','w') as f:
    f.writelines(str(best_score)+'\n')
    f.writelines(str(best_lines)+'\n')
    f.writelines(str(best_level)+'\n')

pygame.quit()