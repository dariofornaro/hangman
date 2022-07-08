import pygame


#setup of the main window
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The hangman game")

#draw buttons
RADIUS = 20 
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2) #I get the two extremes, hence I divide
starty = 400
for i in range(26):
  x = startx + ((RADIUS * 2 + GAP) * (i%13)) + RADIUS
  y = starty + (i // 13 ) * (RADIUS * 2 + GAP)
  letters.append([(x,y)])
  
#import images 
images = []
for i in range(0,7):
  image = pygame.image.load("hangman" + str(i) + ".png")
  images.append(image)

#hangman status 
image_status = 2

#setup game loop
run = True 
clock = pygame.time.Clock()
FPS = 60

#colours 
WHITE = (255,255,255)
BLACK = (0,0,0)

def draw():
  win.fill(WHITE)
  win.blit(images[image_status], (150,100))
  for letter in letters:
    x,y = letter[0]
    pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)

while run:
  clock.tick(FPS)

  draw()
  
  
  pygame.display.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    

pygame.quit()
  

