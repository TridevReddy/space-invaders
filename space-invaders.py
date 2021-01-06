import pygame
import math
import random

# Initialize pygame
pygame.init()

# Screen and background
screen = pygame.display.set_mode((800, 600))
background = pygame.transform.scale(pygame.image.load("background-black.png"),
                                    (800, 600))
#Sound
bullet_sound = pygame.mixer.Sound("Bullet sound.mp3")
# Title
pygame.display.set_caption("Space Invaders")
# Player spaceship
playerimg = pygame.image.load("pixel_ship_yellow.png")
playerx = 400
playery = 510
playerx_change = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


# Enemy
enemyimg = pygame.image.load("pixel_ship_green_small.png")
enemy2img = pygame.image.load("pixel_ship_red_small.png")
enemy2x = random.randint(0, 800)
enemy2y = random.randint(0, 80)
enemyx = random.randint(0, 800)
enemyy = random.randint(0, 80)
enemyx_change = 3
enemyy_change = 40
enemy2x_change = 3
enemy2y_change = 40


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def enemy2(x, y):
    screen.blit(enemy2img, (x, y))


# Bullet
bulletimg = pygame.image.load("pixel_laser_yellow.png")
bulletx = 450
bullety = 500
bulletx_change = 0
bullety_change = 20
bullet_state = "ready"

#Dotted Line
end_line = pygame.image.load("Dotted Line.png")
end_line2 = pygame.image.load("Dotted Line.png")
end_line3 = pygame.image.load("Dotted Line.png")
end_line4 = pygame.image.load("Dotted Line.png")

def line(x,y):
    screen.blit(end_line, (x,y))
def line2(x,y):
    screen.blit(end_line2, (x,y))
def line3(x,y):
    screen.blit(end_line3, (x,y))
def line4(x,y):
    screen.blit(end_line4, (x,y))


#Lives
lives_value = 0
lives_textx = 10
lives_texty = 50


def firing(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x, y + 10))


def collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(math.pow(enemyx - bulletx, 2) + math.pow(enemyy - bullety, 2))
    if distance < 30:
        return True
    else:
        return False


def collision2(enemy2x, enemy2y, bulletx, bullety):
    distance = math.sqrt(math.pow(enemy2x - bulletx, 2) + math.pow(enemy2y - bullety, 2))
    if distance < 30:
        return True
    else:
        return False


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 20


def score_(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def lives_(x, y):
    lives = font.render("Lives :" + str(lives_value+1) + "/3", True, (255, 255, 255))
    screen.blit(lives, (x, y))


gameover = pygame.font.Font('freesansbold.ttf', 32)



def game_over():
    gameover_text = gameover.render("Game Over. Your final score is: " + str(score_value), True, (255, 255, 255))
    screen.blit(gameover_text, (150, 200))


running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and lives_value<3:
                playerx_change = -2.0
            if event.key == pygame.K_RIGHT and lives_value<3:
                playerx_change = 2.0
            if event.key == pygame.K_SPACE and lives_value<3:
                bulletx = playerx
                firing(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    line_x = 5
    line_y = 370
    line2_x = 200
    line2_y = 370
    line3_x = 400
    line3_y = 370
    line4_x = 570
    line4_y = 370

    # Player movements
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    if playerx >= 705:
        playerx = 705

    if enemyy >450 and lives_value<3:
        lives_value+=1
        enemyy = random.randint(0, 80)
        enemyx = random.randint(0, 800)
    if enemy2y > 450 and lives_value<3:
        lives_value+=1
        enemy2y = random.randint(0, 80)
        enemy2x = random.randint(0, 800)



    # Enemy1 movements
    enemyx += enemyx_change
    if enemyx <= 0:
        enemyx_change = 3
        enemyy += enemyy_change
        enemyx = 0
    if enemyx > 730:
        enemyx_change = -3
        enemyy += enemyy_change
        enemyx = 730

    # Enemy2 movements
    enemy2x += enemy2x_change
    if enemy2x <= 0:
        enemy2x_change = 3
        enemy2y += enemy2y_change
        enemy2x = 0
    if enemy2x > 730:
        enemy2x_change = -3
        enemy2y += enemy2y_change
        enemy2x = 730
    #Game Over Condition
    if lives_value>=3:
        enemyx_change=0
        enemy2x_change=0
        enemyy_change=0
        enemy2y_change=0
        game_over()

    # Bullet movements
    if bullety < 0:
        bullety = 500
        bullet_state = "ready"
    if bullet_state == "fire":
        firing(bulletx, bullety)
        bullety -= bullety_change

    # Collision with Enemy1
    if collision(enemyx, enemyy, bulletx, bullety):
        bullet_state = "ready"
        bullety = 500
        enemyx = random.randint(0, 800)
        enemyy = random.randint(0, 80)
        score_value += 1
        print(score_value)

    # Collision with Enemy2
    if collision2(enemy2x, enemy2y, bulletx, bullety):
        bullet_state = "ready"
        bullety = 500
        enemy2x = random.randint(0, 800)
        enemy2y = random.randint(0, 80)
        score_value += 1
        print(score_value)


    player(playerx, playery)
    enemy(enemyx, enemyy)
    enemy2(enemy2x, enemy2y)
    score_(textx, texty)
    line(line_x, line_y)
    line(line2_x, line2_y)
    line(line3_x, line3_y)
    line(line4_x, line4_y)
    if lives_value<3:
        lives_(lives_textx, lives_texty)
    pygame.display.update()
