# 파이썬으로 게임을 만들고 깃허브에 올려보자

# pygame : 파이썬으로 간단한 고전 게임을 만들 수 있는 오픈 소스 입니다.

# pip install pygame: 설치해야지 모듈이 있습니다.

from lib2to3.pgen2.literals import evalString
import sys
import pygame
from pygame.locals import QUIT , Rect , KEYDOWN ,\
    K_LEFT , K_RIGHT , K_UP , K_DOWN
 


pygame.init()
pygame.key.set_repeat(5,5)
배경 = pygame.display.set_mode((600,600))   # 화면 크기 
클릭 = pygame.time.Clock()


earthworms = [[10,10]]
def 지렁이그리기():
    x = 10
    y = 10
    earthworms.append([x,y])
    for i in earthworms:
        pygame.draw.rect(배경 , (0,200,200), (i[0]*30,i[1]*30,30,30))


def 라인그리기():
    for x in range(0,20):
        pygame.draw.line(배경 , (255, 255 , 255) , (x*30,0) , (x*30,600) , 3)
    pygame.draw.line(배경 , (255, 255 , 255) , (0,30) , (600,30) , 3)
    for y in range(0,20):
        pygame.draw.line(배경 , (255, 255 , 255) , (0,y*30) , (600,y*30) , 3)



def main():
    key = K_DOWN
    while True:
        배경.fill((0,0,0))      # 배경색에 대한 변경(빨강,초록,파랑 순)
        for event in pygame.event.get():      #여러가지 이벤트들
            if event.type == QUIT:            # 이벤트의 종류가 종료라면 파이게임을 그만두고 sys(시스템) 종료
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key           # KEYDOWN 이벤트 == 아래


        if key == K_DOWN:
            head = [earthworms[0][0] ,earthworms[0][1]+1]  # 만약  a = [23,21] 23을 부르고 싶다면 0번째 칸 안에 있는 첫번째 [0][1]이 된다.
        elif key == K_UP:
            head = [earthworms[0][0],earthworms[0][1]-1]
        elif key == K_LEFT:
            head = [earthworms[0][0]-1,earthworms[0][1] ]
        elif key == K_RIGHT:
            head = [earthworms[0][0]+1,earthworms[0][1] ]

        
        earthworms.insert(0,head)
        earthworms.pop()


        라인그리기()    # 지렁이의 몸통(선) 내려가야 y좌표가 커진다.
        지렁이그리기()

        pygame.display.update()
        클릭.tick(5)

main()