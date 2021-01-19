import time,math,random
import pygame,sys
from pygame.locals import *
import math
import cv2


cap=cv2.VideoCapture(0)
ret,img1=cap.read()
k=((len(img1)*len(img1[1]))/5000)**(.5)

rx=len(img1)/k
ry=len(img1[1])/k

r=int(len(img1)/rx)
c=int(len(img1[1])/ry)

screenlenth=800
dis=screenlenth/100


screen=pygame.display.set_mode((int(dis*ry),int(dis*rx)))
pygame.display.set_caption("Video MANUPULATION 2")

pygame.init()
threshold=10
running=True

while running:
     
    ret,img1=cap.read()
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    
    img1 = cv2.flip(img1, 1)
    screen.fill((0,0,0))       
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                cap.release()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    for i in range(int(c/2),len(img1),c):
        for j in range(int(r/2),len(img1[i]),r):
            cl=int((img1[i][j])/(255/threshold))*int(255/threshold)
            pygame.draw.circle(screen,(cl,cl,cl),(int(dis*((j-int(c/2))/c)),int(dis*((i-int(r/2))/r))),int(dis/2))
            
    pygame.display.update()  
cap.release()
cv2.destroyAllWindows()



              
