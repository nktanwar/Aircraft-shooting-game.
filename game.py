# TO PLAY THE GAME THE PERSON ON THE LEFT HAVE CONTROL AS 
# W FOR UP , S FOR DOWN , D FOR RIGHT , A FOR LEFT
# AND LEFT CONTROL OF THE KEYBOARD IS USED TO FIRE BULLETS

#INTIAL HEALTH IS 13 AND DECREASE 1 PER HIT

#TO PLAY THE GAME THE PERSON ON THE RIGHT SIDE HAVE THE CONTROL AS FOLLOWING 
# THE GAME KEYS UP KEY FOR UP , DOWN KEY FOR DOWN, RIGHT KEY TO MOVE RIGHT , LEFT KEY TO MOVE LEFT
# THE RIGHT CONTROL IS USED TO FIRE BULLET



import pygame
import os
pygame.font.init()# is use to intialise fonts
pygame.mixer.init() # IS USED FOR UPLOAD SOUNDS

#SETING WIDTH AND HEIGHT OF THE GAME SCREEN
(WIDTH, HIEGHT)=(900, 500)
WIN=pygame.display.set_mode((WIDTH, HIEGHT))
pygame.display.set_caption('game')
BORDER = pygame.Rect(450-5,0,10,500)


#defining font
HEALTH_FONT= pygame.font.SysFont('comicsans',40)
WINNER_FONT= pygame.font.SysFont('comicsans',101)


#constants
MAX_BULLETS=3
VEL=5
BULLET_VELOCITY=7
RED_HIT= pygame.USEREVENT + 1 # unservernt create a no for a manual created event we add 1 to make it unique 
BLACK_HIT= pygame.USEREVENT + 2


#DEFINING COLORS
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
VOILET=(100,83,148)
GREEN=(0,255,0)


# Sound effects
BULLET_HIT_SOUND=pygame.mixer.Sound(os.path.join('assets','bullet_hit.mp3'))
BULLET_FIRE=pygame.mixer.Sound(os.path.join('assets','bullet_sounds.mp3'))


#FRAME PER SECOND
FPS=60 


#IMAGE LOADING
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets','red_spaceship.png'))
RED_SPACESHIP_IMAGE=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(50,50)),(-90))
#RED_SPACESHIP_IMAGE=pygame.transform.rotate(RED_SPACESHIP_IMAGE,(-90.0)) can also be used in seprate line 

BLACK_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets','black_spaceship.png'))
BLACK_SPACESHIP_IMAGE=pygame.transform.rotate(pygame.transform.scale(BLACK_SPACESHIP_IMAGE,(50,50)),(90.0))

BACKGROUND_IMAGE= pygame.image.load(
    os.path.join('assets', 'space.png')
)


# CREATING A RECTANGLE FOR RED AND BLACK SPACESHIP AND ALONG WITH BACKGROUND
red=pygame.Rect(100,200,50,50)
black=pygame.Rect(800,200,50,50)
background=pygame.Rect(0,0,900,500)


#DRAW WINDOW TO DRAW ALL STUFF
def draw_window(red,black,red_bullets,black_bullets,RED_HEALTH,BLACK_HEALTH):
    #WIN.fill(WHITE)
    WIN.blit(BACKGROUND_IMAGE,(background.x,background.y))
    red_health_text = HEALTH_FONT.render("HEALTH: " + str(RED_HEALTH),1,WHITE) #antialias ==1
    black_health_text = HEALTH_FONT.render('HEALTH: ' + str(BLACK_HEALTH),1,WHITE)
    WIN.blit(red_health_text,(10,20 ))
    WIN.blit(black_health_text,(650,20))
    WIN.blit(RED_SPACESHIP_IMAGE,(red.x,red.y))#blit is used to draw surface on the screen
    WIN.blit(BLACK_SPACESHIP_IMAGE,(black.x,black.y))
    pygame.draw.rect(WIN,VOILET,BORDER)

    
    #DRAWING BULLET AS BEING FIRED
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)

    for bullet in black_bullets:
        pygame.draw.rect(WIN,GREEN,bullet)  


    #UPDATING DISPLAY SHOW THE DRAW STUFF CAN BE SEEN ON SCREEN
    pygame.display.update()


# THIS FUNCITON HANDLE THE MOVEMENT OF RED SPACESHIP
def red_movement():
    # key control for red_spaceship
        key_pressed = pygame.key.get_pressed() 
        if key_pressed[pygame.K_a] and red.x-VEL>0:
            red.x-=VEL
        if key_pressed[pygame.K_d] and red.x+VEL<400:
            red.x+=VEL   
        if key_pressed[pygame.K_w] and red.y-VEL>0:
            red.y-=VEL  
        if key_pressed[pygame.K_s] and red.y+VEL<450:
            red.y+=VEL                        
 
# THIS FUNCTION HANDLE MOVEMENT OF BLACK SPACESHIP
def black_movement():
    # key control for black_spaceship
        key_pressed = pygame.key.get_pressed() 
        if key_pressed[pygame.K_LEFT] and black.x-VEL>450:
            black.x-=VEL
        if key_pressed[pygame.K_RIGHT] and black.x+VEL<850:
            black.x+=VEL   
        if key_pressed[pygame.K_UP] and black.y-VEL>0:
            black.y-=VEL  
        if key_pressed[pygame.K_DOWN] and black.y+VEL<450:
            black.y+=VEL                        
         
def handle_movement(red_bullets,black_bullets,red,black):
    for bullet in red_bullets:
        bullet.x += VEL
        if black.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLACK_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > 900:
            red_bullets.remove(bullet)    

    for bullet in black_bullets :
        bullet.x -= VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            black_bullets.remove(bullet)
        elif bullet.x < 0 :
            black_bullets.remove(bullet)

#FUNCTION OT DRAW WINNER TEXT ON SCREEN
def draw_winner(text): 
    draw_text=WINNER_FONT.render(text,1,BLACK)  
    WIN.blit(draw_text,(300,200))
    pygame.display.update()
    pygame.time.delay(3000)
     

             
# MAIN FUCNITON
def main():
    RED_HEALTH= 7
    BLACK_HEALTH= 7
    red_bullets=[]   
    black_bullets=[]
    clock = pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  # looping through the events list get by using(pygame.event.get()) in pygame
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if  event.key ==  pygame.K_LCTRL and len(red_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(red.x + 50.0, red.y + 25.0,10.0,5.0)
                    red_bullets.append(bullet)
                    BULLET_FIRE.play()
                     
            
                if event.key == pygame.K_RCTRL and len(black_bullets)< MAX_BULLETS:
                    bullet = pygame.Rect(black.x , black.y + 25,10,5)
                    black_bullets.append(bullet)
                    BULLET_FIRE.play()

            if event.type == RED_HIT:
                RED_HEALTH = RED_HEALTH -1 
                BULLET_HIT_SOUND.play()
            if event.type == BLACK_HIT:
                BLACK_HEALTH = BLACK_HEALTH -1 
                BULLET_HIT_SOUND.play() 
                
        winner_text=''             
        if RED_HEALTH<=0:
            winner_text = "Black Wins"
        if BLACK_HEALTH<=0:
            winner_text = 'Red Wins'
        if winner_text!='':
            draw_winner(winner_text)
            break               
        
         
        # CALLING ALL THE REQUIRED FUNCTION CREATED ABOVE 
        red_movement() 
        black_movement() 
        handle_movement(red_bullets,black_bullets,red,black)      
        draw_window(red,black,red_bullets,black_bullets,RED_HEALTH,BLACK_HEALTH)        
 
    main() # ONCE THE WINNER IS DRAW TO RESTART THE GAME MAIN() FUNCTION IS CALLED   

main()                
    

          



