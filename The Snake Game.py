# Importing Modules.....
import pygame
import random
import os 

# Intitalising the module from pygame....
pygame.init()

# snake window variables...
window_width = 700
window_height = 400

# Setting rgb color code for snakes....
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 216, 1)

# Creating window for snakes.....
game_window = pygame.display.set_mode((window_width, window_height))
window_title = pygame.display.set_caption("The Snake Game - Created by Mohd.Tahil")
img = pygame.image.load("1.png.png")
window_img = pygame.display.set_icon(img)
pygame.display.update()

# Making a function forl ploting a snake....
def plot_snake(window_path, color, snk_list, snake_size):

    for x, y in snk_list:
        pygame.draw.rect(window_path, color, [x, y, snake_size, snake_size])

# Creating a function for font....
font = pygame.font.SysFont(None, 55)
def screen_text(text, color, x, y):
    text_screen = font.render(text, True, color)
    game_window.blit(text_screen, [x, y])

# Creating the welcome screen.....
def welcome():
    # Setting music.....
    pygame.mixer.init()
    pygame.mixer.music.load("CjW.mp3.mp3")
    pygame.mixer.music.play()

    exit_game = False

    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game = True
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()

                if event.key==pygame.K_q:
                    exit_game = True 

        #Setting Image.....
        wimg = pygame.image.load("jpj3.image.jpg")
        wimg = pygame.transform.scale(wimg, (window_width, window_height)).convert_alpha()
        game_window.blit(wimg, (0, 0))
        screen_text("Press Space to Play", yellow, 120, 100)
        screen_text("Press q to exit", yellow, 200, 180)
        pygame.display.update()
    
# Creating Game Main loop....
def gameloop():
    # Creating game end variables....
    game_over = False
    exit_game = False

    # Setting Game Specific functiong for snakes game.....
    snake_x = 100
    snake_y = 100
    snake_size = 20
    food_x = 60
    food_y = 60
    food_size = 16
    velocity_x = 0
    velocity_y = 0
    score = 0
    snk_list = []
    snk_lenght = 1
    fps = 30
    clock = pygame.time.Clock()

    while not exit_game:
        if game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        gameloop()
                    
                    if event.key==pygame.K_q:
                        exit_game = True
            
            # Pasting image......
            img_over = pygame.image.load("jopj1.image.jpg")
            img_over = pygame.transform.scale(img_over, (window_width, window_height)).convert_alpha()
            game_window.blit(img_over, (0, 0))

            screen_text("Game Over !!!!", red, 200, 120)
            screen_text("Press Space to Continue", red, 120, 180)
            screen_text("Press q to exit", red, 200, 250)
            pygame.display.update()
        
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    
                    if event.key==pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    
                    if event.key==pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0
        
            snake_x = snake_x + velocity_x 
            snake_y = snake_y + velocity_y 
            
            if snake_x<0 or snake_x>window_width or snake_y<0 or snake_y>window_height:
                game_over = True
                # Setting music for game_over.....
                pygame.mixer.init()
                pygame.mixer.music.load("pubg.mp3.mp3")
                pygame.mixer.music.play()

            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8 or abs(snake_x-food_y)<1 and abs(snake_y-food_y)<1:
                score+=5
                food_x = random.randint(200, window_width/2)
                food_y = random.randint(200, window_height/2)
                snk_lenght+=4
                pygame.mixer.init()
                pygame.mixer.music.load("Beep Mp3.mp3")
                pygame.mixer.music.play()
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenght:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True
                # Setting music for game_over.....
                pygame.mixer.init()
                pygame.mixer.music.load("pubg.mp3.mp3")
                pygame.mixer.music.play()
            
            if (not os.path.exists("highscore.txt.py")):
                with open("highscore.txt.py", "w") as f:
                    f.write("0")
            
            with open("highscore.txt.py") as f:
                highscore = f.read()
            
            if score>int(highscore):
                highscore=str(score)

            game_window.fill(black)
            screen_text("Score_:"+ str(score)+"    "+"HighScore_:"+ str(highscore), red, 5, 5)
            pygame.draw.rect(game_window, yellow, [snake_x, snake_y, snake_size, snake_size])
            pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
            plot_snake(game_window, yellow, snk_list, snake_size)
            pygame.display.update()
            clock.tick(fps)

welcome()
# Setting game out functions...
pygame.quit()
quit()