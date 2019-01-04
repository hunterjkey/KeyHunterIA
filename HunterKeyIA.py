import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (249, 141, 0)
BLUE = (0, 73, 209)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 550)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("The Ideal Gas Law")
 
# Loop until the user clicks the close button.
done = False

#initial variables
MoleAmount = 5
TempAmount = 5
VolumeAmount = 50
PressureAmount = 0
MolesX = [413, 326, 363, 445, 288, 230, 368, 342, 250, 423]
MolesY = [247, 244, 347, 267, 324, 344, 277, 183, 206, 188]
MolesXMovement = [1,1,-1,1,-1,1,1,-1,-1,-1]
MolesYMovement = [1,-1,-1,1,1,1,-1,-1,-1,1]
bump = False
bumpwidth = 400
Cycle = 0
Counts = 0
slidersY = 215
notchesY = 0
notchesX = 0

MolesLetters = ["M","O","L","E","S"]
MolesLettersX = [15,15,16,16,16]
PressureLetters = ["P","R","E","S","S","U","R","E"]
PressureLettersX = [16,15,16,16,16,15,15,16]
TemperatureLetters = ["T","E","M","P","E","R","A","T","U","R","E"]
TemperatureLettersX = [16,16,15,16,16,15,15,16,15,15,16]
VolumeLetters = ["V","O","L","U","M","E"]
VolumeLettersX = [15,15,16,15,15,16]
letterY = 185 #Y position for the column letters
letterX = 15 #Y position for the column letters
LettersList = [MolesLetters, PressureLetters, TemperatureLetters, VolumeLetters]
LettersListX = [MolesLettersX, PressureLettersX, TemperatureLettersX, VolumeLettersX]
LettersChoice = 0 #current column being printed
LettersChoiceX = 0 #current column's positions being printed



# Used to manage how fast the screen updates
clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if TempAmount<10:
                    TempAmount+=1
            if event.key == pygame.K_DOWN:
                if TempAmount>0:
                    TempAmount-=1
            if event.key == pygame.K_LEFT:
                if MoleAmount>0:
                    MoleAmount-=1
            if event.key == pygame.K_RIGHT:
                if MoleAmount<10:
                    MoleAmount+=1
            if event.key == pygame.K_w:
                if VolumeAmount<100:
                    VolumeAmount+=10
            if event.key == pygame.K_s:
                if VolumeAmount>0:
                    VolumeAmount-=10
                    for i in range(len(MolesX)):
                        if (MolesX[i]-175>15):
                            MolesX[i]-=10
                        if (MolesY[i]-180>15):
                            MolesY[i]-=10

    #screen fill
    screen.fill(BLACK)

    #Code that detects the mouse
    pos = pygame.mouse.get_pos()
    mouseX = pos[0]
    mouseY = pos[1]
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    
    #logical Code
    if ((MoleAmount*2)<len(MolesX)):
        for i in range(len(MolesX)-(MoleAmount*2)):
            if len(MolesX)>0:
                MolesX.pop(0)
                MolesY.pop(0)
                MolesXMovement.pop(0)
                MolesYMovement.pop(0)
    if ((MoleAmount*2)>len(MolesX)):
        for i in range((MoleAmount*2)-len(MolesX)):
            MolesX.append(random.randint(176,450+VolumeAmount))
            MolesY.append(random.randint(182,350+VolumeAmount))
            MolesXMovement.append(1)
            MolesYMovement.append(1)
            
    for i in range(len(MolesX)):
        if ((450+VolumeAmount)-MolesX[i]<5):
            MolesXMovement[i] *= -1
            bump = True
            Counts+=1
        elif (MolesX[i]-175<=5):
            MolesXMovement[i] *= -1
            bump = True
            Counts+=1
            
        if ((355+VolumeAmount)-MolesY[i]<5):
            MolesYMovement[i] *= -1
            bump = True
            Counts+=1
        elif (MolesY[i]-180<=5):
            MolesYMovement[i] *= -1
            bump = True
            Counts+=1

    if bump == True:
        bumpwidth = 5
        bump = False
    else:
        bumpwidth = 0
            
    for i in range(len(MolesX)):
        MolesX[i] += (MolesXMovement[i]*TempAmount)
        MolesY[i] += (MolesYMovement[i]*TempAmount)

    if Cycle==10:
        PressureAmount = Counts
        print (PressureAmount)
        Cycle = 0
        Counts = 0
    Cycle+=1
    #---- Other Drawing Code ----

    #--Title Code--
    font = pygame.font.SysFont('timesnewroman', 120, True, False)
    text = font.render("PV=nRT",True,WHITE)
    screen.blit(text, [170, 0])

    font = pygame.font.SysFont('timesnewroman', 20, True, False)
    text = font.render("Pressure, Volume, Moles, the univeRsal constant, and Temperature",True,WHITE)
    screen.blit(text, [125, 120])

    pygame.draw.line(screen, WHITE, [15, 150], [785, 150], 3)

    #--Body Code--
    pygame.draw.rect(screen, WHITE, [(10, 180), (30, 300)])
    pygame.draw.rect(screen, WHITE, [(50, 180), (30, 300)])
    pygame.draw.rect(screen, WHITE, [(90, 180), (30, 300)])
    pygame.draw.rect(screen, WHITE, [(130, 180), (30, 300)])
    pygame.draw.rect(screen, WHITE, [(175-bumpwidth, 180-bumpwidth), (300+(2*bumpwidth)+VolumeAmount, 200+(2*bumpwidth)+VolumeAmount)], 3)
    pygame.draw.rect(screen, WHITE, [(600, 180), (185, 300)], 3)
    for i in range(4):
        pygame.draw.line(screen, WHITE, [615, slidersY], [765, slidersY], 3)
        slidersY += 70
    slidersY = 225

    for i in range(4):
        for i in range(11):
            pygame.draw.line(screen, WHITE, [notchesX, notchesY], [notchesX, notchesY+10], 3)
            notchesX += 15
        notchesX = 615
        notchesY += 70
    notchesY = 220

    notchesY = 215
    for i in range(4):
        pygame.draw.line(screen, RED, [690, notchesY], [690, notchesY+20], 5)
        notchesY += 70
    notchesY = 220

    pygame.draw.rect(screen, BLUE, [(15, 480-(MoleAmount*30)), (20, (MoleAmount*30))])
    pygame.draw.rect(screen, ORANGE, [(55, 480-(PressureAmount*5)), (20, (PressureAmount*5))])
    pygame.draw.rect(screen, RED, [(95, 480-(TempAmount*30)), (20, (TempAmount*30))])
    pygame.draw.rect(screen, GREEN, [(135, 480-(VolumeAmount*3)), (20, (VolumeAmount*3))])

    #-Column Code-
    font = pygame.font.SysFont('timesnewroman', 24, False, False)
    for a in range(len(LettersList)):
        LettersChoice = LettersList[a]
        LettersChoiceX = LettersListX[a]
        for i in range(len(LettersChoice)):
            text = font.render(LettersChoice[i],True,BLACK)
            screen.blit(text, [letterX+LettersChoiceX[i], letterY])
            letterY += 20
        letterY = 185
        letterX += 40
    letterX = 0

    for i in range(len(MolesX)):
        pygame.draw.ellipse(screen, WHITE, [MolesX[i],MolesY[i],25,25], 3)
    #mouse placement code (remove)
    font = pygame.font.SysFont('timesnewroman', 20, False, False)
    text = font.render("("+str(mouseX)+","+str(mouseY)+")",True,WHITE)
    screen.blit(text, [10, 520])
    
    #update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
