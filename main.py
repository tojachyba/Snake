import pygame
import random
pygame.init()
blocks=[[1,1],[1,2]]
food=[random.randint(3,119),random.randint(3,78)]
czcionka=pygame.font.SysFont(None,25)
di="d"
fps=pygame.time.Clock()
screen=pygame.display.set_mode([1200,800])
pygame.display.set_caption("Gra w Snake'a")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type== pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit(0)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                if di=="d":
                    di="l"
                elif di=="l":
                    di="u"
                elif di=="u":
                    di="r"
                elif di=="r":
                    di="d"
            if event.key==pygame.K_a:
                if di=="d":
                    di="r"
                elif di=="r":
                    di="u"
                elif di=="u":
                    di="l"
                elif di=="l":
                    di="d"
    fps.tick(20)
    screen.fill((50, 50, 50)) 
    i=0
    pygame.draw.circle(screen,(255,0,0),(food[0]*10+5,food[1]*10+5),5)
    if blocks[len(blocks)-1][0]==food[0] and blocks[len(blocks)-1][1]==food[1]:
        blocks.insert(0, blocks[0])
        food = [random.randint(3,119), random.randint(3,78)]
    while i < len(blocks):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(blocks[i][0]*10,blocks[i][1]*10, 10, 10))
        if blocks[len(blocks)-1][0]==blocks[i][0] and blocks[len(blocks)-1][1]==blocks[i][1] and i<len(blocks)-1:
            blocks=[[1,1],[1,2]]
            food=[random.randint(3,129),random.randint(3,78)]
            di="d"
        i+=1
    screen.blit(czcionka.render("Dlugosc: "+str(len(blocks)),1,(200, 200, 200)),(1080, 8))
    if di=="d":
        blocks.append([blocks[len(blocks)-1][0],blocks[len(blocks)-1][1]+1])
    if di=="u":
        blocks.append([blocks[len(blocks)-1][0],blocks[len(blocks)-1][1]-1])
    if di=="r":
        blocks.append([blocks[len(blocks)-1][0]+1, blocks[len(blocks)-1][1]])
    if di=="l":
        blocks.append([blocks[len(blocks)-1][0]-1, blocks[len(blocks)-1][1]])
    del blocks[0]
    if blocks[len(blocks)-1][0]<0:
        blocks[len(blocks)-1][0]=119
    elif blocks[len(blocks)-1][0]>120:
        blocks[len(blocks)-1][0]=1
    if blocks[len(blocks)-1][1]<0:
        blocks[len(blocks)-1][1]=79
    elif blocks[len(blocks)-1][1]>80:
        blocks[len(blocks)-1][1]=1
    pygame.display.flip()