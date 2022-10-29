import pygame
import math
import pygame.time as time

#setup of the main window
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The hangman game")

#draw buttons
visible = True
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) /
               2)  #I get the two extremes, hence I divide
starty = 400
A = 65
for i in range(26):
    x = startx + ((RADIUS * 2 + GAP) * (i % 13)) + RADIUS
    y = starty + (i // 13) * (RADIUS * 2 + GAP)
    letters.append([x, y, chr(A + i), visible])

#import images
images = []
for i in range(0, 7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#hangman status
image_status = 0
word = "CIAO"
guessed = []

#setup game loop
run = True
clock = pygame.time.Clock()
FPS = 60

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#font
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 60)
RESULT_FONT = pygame.font.SysFont('comicsans', 100)


def draw():
    win.fill(WHITE)
    win.blit(images[image_status], (150, 100))
    
    #draw title
    text = ()
    
    #display word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = LETTER_FONT.render(display_word, 1, BLACK)
    win.blit (text, (400,250))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text,
                     (x - text.get_width() / 2, y - text.get_height() / 2))

#print the message
def result (message):
    time.delay(1000)
    win.fill(WHITE)
    text = RESULT_FONT.render(message, 1, BLACK)
    win.blit (text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2) )
    pygame.display.update()
    time.delay(3000)
    
while run:
    clock.tick(FPS)

    draw()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()

            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((m_x - x)**2 + (m_y - y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            image_status += 1  
        if event.type == pygame.QUIT:
            run = False

    #check if I won
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
    if won:
        print ("I won")
        result("YOU WON!")
        break 

    if image_status == 6:
        print ("loose")
        result("YOU LOST :(")
        break
    

pygame.quit()
