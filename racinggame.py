from pygame import*
from random import*

font.init()
mixer.init()

mixer.music.load("theme.mp3")
mixer.music.play(-1)
volume=1
mixer.music.set_volume(volume)
clock = time.Clock()

sw=800
sh=600

mode="main"
money=0
distance=0.00
player_score=0
price=0
buttonb="button.png"
buttonb2="button2.png"
icon=image.load("icon.png")
menu_arrow1="button arrow.png"
menu_arrow1_m_one="button arrow2.png"

menu_arrow2="button arrow1.png"
menu_arrow2_m_one="button arrow12.png"

standart_x,standart_y=(sw/2)-100,(sh/2)-80
screen=display.set_mode((sw,sh))
display.set_caption("CARS")
display.set_icon(icon)

def screen_mode():
    global background,ready
    if mode=="main":
        back="background_main.png"
    elif mode=="menu":
        back="background_menu.png"
    elif mode=="choose":
        back="background_choose_option.png"
    elif mode=="game":
        ready=True
        back="background_game.png"
    elif mode=="lost":
        back="background_lost.jpg"
    background = transform.scale(image.load(back), (sw, sh))

class Running_obj(sprite.Sprite):
    def __init__(self,filename,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(filename),(w,h))
        self.w=w
        self.h=h
        self.x=x
        self.y=y
        self.rect=self.image.get_rect(topleft=(x,y))
        self.kmph=7
        self.previous_y=None

    def go_up(self,obj):
        global mode
        if obj.speed<=10 and self.rect.y<sh:
            self.rect.y-=5
        if self.rect.colliderect(Rect(obj.rect.center[0], obj.rect.center[1], 1, 1)) and obj.speed > 10:
            mode = "lost"

        var=[randint(245,250),randint(410,430)]
        var2=[]
        var2
        x=randint(-800,-10)
        for _ in range(randint(10,50)):
            var2.append(x)
            x-=randint(400,600)

        if obj.speed>10:
            self.rect.y+=9.8+obj.speed/50
        if obj.speed>=30 and self.rect.y>sh+randint(100,1000):
            self.rect.x=choice(var)
            self.rect.y=choice(var2)
            var2.remove(self.rect.y)
            shuffle(var2)
            
        for i in var2:
            i+=randint(100,500)
            shuffle(var2)
            
        keys=key.get_pressed()
        if obj.speed>10 and keys[K_UP]:
            self.rect.y+=3
            
    def lets_go(self):
        screen.blit(self.image,self.rect)
        keys=key.get_pressed()
        self.rect.y+=3
        if keys[K_DOWN]:
            if self.kmph>=5:
                self.kmph-=2

        if keys[K_UP]:
            self.rect.y+=self.kmph
            if self.kmph<50:
                self.kmph+=1
        if not keys[K_UP] and self.kmph>5:
            self.rect.y+=self.kmph
            self.kmph-=self.kmph/50

        if self.rect.bottom>=sh+900:
            self.rect.y=-900

road1=Running_obj("road.png",350,900,(sw/2)-175,-1800) 
road=Running_obj("road.png",350,900,(sw/2)-175,0) 
road2=Running_obj("road.png",350,900,(sw/2)-175,-900)

grass1=Running_obj("grass.jpg",235,900,0,0)
grass2=Running_obj("grass.jpg",235,900,0,-900)
grass3=Running_obj("grass.jpg",235,900,0,-1800)
grass4=Running_obj("grass.jpg",225,900,575,0)
grass5=Running_obj("grass.jpg",225,900,575,-900)
grass6=Running_obj("grass.jpg",225,900,575,-1800)
gras_sq=[grass1,grass2,grass3,grass4,grass5,grass6]

skins_npc=["npc car1.png","npc car2.png","npc car3.png","npc car4.png","npc car5.png","npc car6.png","npc car7.png","npc car8.png","npc car10.png"]
npc=sprite.Group()

nums=[400,500,600]
co_x=[245,420]
co_y=[]

a=randint(0,400)
for i in range(10):
    co_y.append(a)
    a+=choice(nums)

for i in range(len(skins_npc)):
    npc_car=Running_obj(skins_npc[i],120,200,choice(co_x),choice(co_y))
    npc.add(npc_car)
    co_y.remove(npc_car.rect.y)

class BUTTON():
    def __init__(self,text,filename,filename2,w,h,x,y,click_sound=None):
        self.text=text
        self.image=transform.scale(image.load(filename),(w,h))
        self.image2=transform.scale(image.load(filename2),(w,h))
        self.w=w
        self.h=h
        self.x=x
        self.y=y
        self.rect=self.image.get_rect(topleft=(x,y))
        self.mouse_on=False
        if click_sound:
            self.sound=mixer.Sound(click_sound)

    def draw(self):
        if self.mouse_on:
            current=self.image2
        else:
            current=self.image
        screen.blit(current,(self.rect.topleft))

        font1=font.Font(None,30)
        t=font1.render(self.text,True,(0,0,0))
        t_rect=t.get_rect(center=self.rect.center)
        screen.blit(t,t_rect)

    def check_mouse(self,mouse_pos):
        self.mouse_on=self.rect.collidepoint(mouse_pos)

    def clicksound(self):
        self.sound.play()

    def change(self,list_of_cars):
        if list_of_cars[-1].x!=standart_x:
            for i in list_of_cars:
                i.x-=standart_x

    def change2(self,list_of_cars):
        if list_of_cars[0].x!=standart_x:
            for i in list_of_cars:
                i.x+=standart_x

play_button=BUTTON("PLAY",buttonb,buttonb2,140,80,330,100,"click.ogg")
leave_button=BUTTON("QUIT",buttonb,buttonb2,140,80,330,500,"click.ogg")
left_button=BUTTON("",menu_arrow1,menu_arrow1_m_one,100,100,50,(sh/2-50),"selection.mp3")
right_button=BUTTON("",menu_arrow2,menu_arrow2_m_one,100,100,sw-150,(sh/2-50),"selection.mp3")
back_button=BUTTON("BACK",buttonb,buttonb2,140,80,40,500,"click.ogg")
back2_button=BUTTON("BACK",buttonb,buttonb2,140,80,(sw/2)-250,450,"click.ogg")
play_again_button=BUTTON("PLAY AGAIN",buttonb,buttonb2,140,80,(sw/2)+100,450,"click.ogg")
gamemode1_button=BUTTON("","trlight.png","trlight2.png",150,150,330,250,"click.ogg")

class Car():
    def __init__(self,main_image,upper_view,t_left,t_right,w,h,x,y,w2,h2,g_x,g_y,price,max_speed):
        self.image=transform.scale(image.load(main_image),(w,h))
        self.w=w
        self.h=h
        self.w2=w2
        self.h2=h2
        self.main=main_image
        self.upper=upper_view
        self.left=t_left
        self.right=t_right
        self.x=x
        self.y=y
        self.g_x=g_x
        self.g_y=g_y
        self.rect=self.image.get_rect()
        self.rect.x=g_x
        self.rect.y=g_y
        self.speed=0
        self.price=price
        self.max=max_speed
    def show(self):
        self.image=transform.scale(image.load(self.main),(self.w,self.h))
        screen.blit(self.image,(self.x,self.y))

    def drive(self,speed):
        self.image=transform.scale(image.load(self.upper),(self.w2,self.h2))
        keys=key.get_pressed()
        if keys[K_DOWN] and self.speed>0:
            self.speed-=(self.speed/10)
        if keys[K_UP] and self.speed<self.max:
            self.speed+=1
        else:
            if self.speed>10:
                self.speed-=0.8
        if keys[K_LEFT] and self.rect.x>sw/2-175:
            self.image=transform.scale(image.load(self.left),(self.w,self.h))
            self.rect.x-=speed
        if keys[K_RIGHT] and self.rect.left<420:
            self.image=transform.scale(image.load(self.right),(self.w,self.h))
            self.rect.x+=speed
        screen.blit(self.image,self.rect)

car_Ford=Car("mustang.png","mustang upper view.png","mustang left.png","mustang right.png",200,150,standart_x*2,standart_y,160,210,standart_x-10,sh/2+50,3000,120)
car_Acura=Car("acura nsx.png","acura upper view.png","acura left.png","acura right.png",200,150,standart_x,standart_y,220,220,standart_x-10,sh/2+50,0,140)
car_Corvette=Car("corvette c8.png","corvette upper view.png","corvette left.png","corvette right.png",200,150,standart_x*3,standart_y,120,180,standart_x+40,sh/2+50,5000,200)
car_Koenigsegg=Car("one.png","one upper view.png","one left.png","one right.png",220,160,standart_x*4,standart_y-30,150,200,standart_x+10,sh/2+50,7000,250)

list_of_cars=[car_Acura,car_Ford,car_Corvette,car_Koenigsegg]
def for_main():
    play_button.rect.x,play_button.rect.y=330,400
    play_button.draw()
    leave_button.draw()

def for_menu():
    global unlock,price,money
    money_icon=BUTTON(str(money),"money icon.png","money icon.png",140,50,700,50)
    unlock=BUTTON(str(price)+" $","pnglock.png","unlock.png",100,100,standart_x+50,standart_y,"click.ogg")
    unlock.check_mouse(m_pose)
    if money>500:
        money_icon.rect.x=650
    for i in list_of_cars:
        i.show()
        if i.x==standart_x:
            price=i.price
            car=i
            if unlock.rect.collidepoint(x,y) and money>=price:
                car.price=0
                money-=price
    if price>0:
        play_button.rect.x=-sh
        unlock.draw()
    if price<=0:
        play_button.rect.x,play_button.rect.y=620,500
        play_button.draw()
    back_button.draw()
    money_icon.draw()
    left_button.draw()
    right_button.draw()

def for_lose():
    for npc_car in npc:
        npc_car.rect.y+=randint(600,700)
    main_car.speed=0
    main_car.rect.x,main_car.rect.y=main_car.g_x,main_car.g_y
    road.kmph=0
    road1.kmph=0
    road2.kmph=0
    if not again:
        distance_icon=BUTTON("Distance: "+str(round(distance,2)),"distance icon.png","distance icon.png",160,50,standart_x,standart_y)
        score_icon=BUTTON("Score: "+str(int(player_score)),"score icon.png","score icon.png",160,50,standart_x,standart_y+100)
    score_icon.draw()
    distance_icon.draw()
    back2_button.draw()
    play_again_button.draw()

def for_choose():
    back_button.draw()
    gamemode1_button.draw()

def for_game():
    global main_car, money, distance, start_time, player_score, again
    current_time=(time.get_ticks()-start_time)//1000
    for i in list_of_cars:
        if i.x==standart_x:
            main_car=i
    if again:
        distance=0.0
        player_score=0
        again=False
    for i in gras_sq:
        i.lets_go()
    speed_icon=BUTTON(str(int(main_car.speed)),"speed icon.png","speed icon.png",140,50,0,10)
    distance_icon=BUTTON("km "+str(round(distance,2)),"distance icon.png","distance icon.png",140,50,0,70)
    score_icon=BUTTON("score "+str(int(player_score)),"score icon.png","score icon.png",140,50,650,10)
    speed_icon.draw()
    distance_icon.draw()
    score_icon.draw()
    road1.lets_go()
    road.lets_go()
    road2.lets_go()
    main_car.drive(20)
    npc.update()
    npc.draw(screen)
    for npc_car in npc:
        npc_car.go_up(main_car)
    money+=distance*5
    if distance<0.5:
        money+=1
    distance+=(main_car.speed/current_time)*0.001
    if main_car.speed>10:
        player_score+=5*distance
    money=int(money)

start_time=time.get_ticks()

again=False
run=True
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
        if e.type == MOUSEMOTION:
            global m_pose
            m_pose=e.pos
            play_again_button.check_mouse(e.pos)
            play_button.check_mouse(e.pos)
            leave_button.check_mouse(e.pos)
            back_button.check_mouse(e.pos)
            back2_button.check_mouse(e.pos)
            left_button.check_mouse(e.pos)
            right_button.check_mouse(e.pos)
            gamemode1_button.check_mouse(e.pos)

        if e.type==MOUSEBUTTONDOWN:
            global x,y
            x,y=e.pos
            if leave_button.rect.collidepoint(x,y) and mode=="main":
                quit()
            if play_button.rect.collidepoint(x,y) and mode!="choose" and mode!="game" and mode!="lost":
                play_button.clicksound()
                mode="menu"
                if play_button.rect.x!=330:
                    mode="choose"
            if back2_button.rect.collidepoint(x,y) and mode!="main" and mode!="menu" and mode!="game" and mode!="choose":
                back2_button.clicksound()
                again=True
                mode="menu"
            if back_button.rect.collidepoint(x,y) and mode!="main" and mode!="game" and mode!="lost":
                back_button.clicksound()
                if mode!="choose":
                    mode="main"
                if mode=="choose":
                    mode="menu"
            if left_button.rect.collidepoint(x,y) and mode!="main" and mode!="game" and mode!="choose":
                left_button.clicksound()
                left_button.change2(list_of_cars)
            if right_button.rect.collidepoint(x,y) and mode!="main" and mode!="game" and mode!="choose":
                right_button.clicksound()
                right_button.change(list_of_cars)
            if gamemode1_button.rect.collidepoint(x,y) and mode!="main" and mode!="menu" and mode!="game" and mode!="lost":
                gamemode1_button.clicksound()
                mode="game"
            if play_again_button.rect.collidepoint(x,y) and mode=="lost":
                again=True
                play_again_button.clicksound()
                mode="game"

    screen_mode()

    screen.blit(background,(0,0))

    if mode=="main":
        for_main()
    if mode=="menu":
        for_menu()
    if mode=="choose":
        for_choose()
    if mode=="game":
        for_game()
    if mode=="lost":
        for_lose()

    display.update()
    
    clock.tick(60)