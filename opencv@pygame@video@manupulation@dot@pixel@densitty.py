import time,math,random
import pygame,sys
from pygame.locals import *
import math
import cv2


cap=cv2.VideoCapture(0)
ret,img1=cap.read()
pixels=5000
k=((len(img1)*len(img1[1]))/pixels)**(.5)

rx=len(img1)/k
ry=len(img1[1])/k

screenlenth=800
dis=int(screenlenth/pixels**(.5))

screen=pygame.display.set_mode((int(dis*ry),int(dis*rx)))
pygame.display.set_caption("Video MANUPULATION 2")
darkness=10
pygame.init()

running=True

while running:
     
    ret,img1=cap.read()
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    
    img1 = cv2.flip(img1, 1)
    screen.fill((255,255,255))       
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                cap.release()
    mice=pygame.mouse.get_pos()
    posx=mice[0]
    if(posx!=0):
        fr=posx/int(dis*rx)
    else:fr=1
    rd=rx*fr
    cd=ry*fr
    
    r=int(len(img1)/rd)
    c=int(len(img1[1])/cd)
    radius=(math.sqrt(int(dis*ry)*int(dis*rx)/rd/cd))
    # cd=int(c*((posx/100)+1))
    # rd=int(r*((posx/int(dis*rx)*7)+1))
    for i in range(int(c/2),len(img1),c):
        for j in range(int(r/2),len(img1[i]),r):
            pygame.draw.circle(screen,(0,0,0),(int(radius*((j-int(c/2))/c)),int(radius*((i-int(r/2))/r))),int(((radius/2)+3)*(255-img1[i][j])/255))
            
    pygame.display.update()  
cap.release()
cv2.destroyAllWindows()



              
