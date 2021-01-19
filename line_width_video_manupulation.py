import pygame,sys
from pygame.locals import *
import math
import cv2
import numpy as np


cap=cv2.VideoCapture(0)
ret,img1=cap.read()
k=((len(img1)*len(img1[1]))/5000)**(.5)

rx=len(img1)/k
ry=len(img1[1])/k

r=int(len(img1)/rx)
c=int(len(img1[1])/ry)

screenlenth=800
dis=screenlenth/100

screenlenth=800
screen=pygame.display.set_mode((int(dis*ry),int(dis*rx)))
pygame.display.set_caption("Video MANUPULATION ")

pygame.init()

running=True
while running:
    
    ret,img1=cap.read()
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
    for i in range(int(c/2),len(img1)-2,c):
        for j in range(int(r/2),len(img1[i])-2,r):
            colour=(((img1[i][j][0])*0.3)+((img1[i][j][0])*0.59)+((img1[i][j][0])*0.11))
            #pygame.draw.circle(screen,(0,0,0),(int(dis*((j-int(c/2))/c)),int(dis*((i-int(r/2))/r))),int((dis)*((255-colour)/255)))
            pygame.draw.line(screen,(0,0,0),(int(dis*((j-int(c/2))/c)),int(dis*((i-int(r/2))/r))),(int(dis*(((j-int(c/2))/c)+1)),int(dis*(((i-int(r/2))/r)))),(int((dis)*((255-colour)/255)))) 
    pygame.display.update()                
cap.release()
cv2.destroyAllWindows()
