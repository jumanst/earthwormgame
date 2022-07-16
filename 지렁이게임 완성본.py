# 파이썬으로 게임을 만들고 깃허브에 올려보자

# pygame : 파이썬으로 간단한 고전 게임을 만들 수 있는 오픈 소스 입니다.

# pip install pygame: 설치해야지 모듈이 있습니다.
a =[1]
from lib2to3.pgen2.literals import evalString
import sys
import pygame
import random
from pygame.locals import QUIT , Rect , KEYDOWN ,\
    K_LEFT , K_RIGHT , K_UP , K_DOWN
 


pygame.init()
pygame.key.set_repeat(5,5)
배경 = pygame.display.set_mode((600,600))   # 화면 크기 
클릭 = pygame.time.Clock()
font = pygame.font.SysFont("arrial",30,True,True)
over_text = font.render("Game Over", True,  (255,255,255))
clear_text = font.render("Game Clear", True,  (255,255,255))


foods = []
def 먹이만들기(): 
    while True:
        pos = [random.randint(0,19) , random.randint(0,19)]    # 0부터 19까지의 수를 하나 랜덤으로 정해주는 것
        if pos in foods:
            continue     # 예로 [2,5]가 푸드안에 있다면? 만들지 않고 다시 새로운 숫자를 뽑으러 위로 올라간다.
        foods.append(pos)         # continue = 코드의 첫 부분으로 돌아가는 코드
        break
    

def 먹이그리기():
    for i in foods:
        pygame.draw.rect(배경 , (100,0,200), (i[0]*30,i[1]*30,30,30))  # 먹이의 색깔을 바꾸려면 배경 뒤에 (빨,초,파)를 변경
    


earthworms = [[10,10]]
def 지렁이그리기():
    for i in earthworms:
        pygame.draw.rect(배경 , (0,255,50), (i[0]*30,i[1]*30,30,30))
    



def 라인그리기():
    for x in range(0,20):
        pygame.draw.line(배경 , (255, 255 , 255) , (x*30,0) , (x*30,600) , 3)
    pygame.draw.line(배경 , (255, 255 , 255) , (0,30) , (600,30) , 3)
    for y in range(0,20):
        pygame.draw.line(배경 , (255, 255 , 255) , (0,y*30) , (600,y*30) , 3)



def main():
    for i in range(100): #먹이를 여러개 만들기 위해 반복문 사용
        먹이만들기()
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

        
        earthworms.insert(0,head)   # insert: (어디에 , 추가할 대상)
        if not head in foods:
            earthworms.pop()        # pop(): 리스트 맨 끝에 값을 제거 , pop(2) 두번째 리스트 제거
        else:
            del foods[foods.index(head)] # del : 리스트에서 삭제 # index(대상) : 값의 위치를 찾아줌            
            먹이만들기()  # 한 먹이를 먹어서 그 먹이가 삭제될 때마다 먹이를 다시 만들어주는 것
            #게임 클리어(먹이를 20개 먹었을 때)
        if len(earthworms) == 50:
            배경.blit(clear_text , (255,300))
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()
            

        #벽에 닿았을 때 게임 종료하게 하기
        if head[0] < 0 or head[0] > 20 or head[1] < 0 or head[1] > 20:
            배경.blit(over_text , (255,300))
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()
            

        라인그리기()    # 지렁이의 몸통(선) 내려가야 y좌표가 커진다.
        지렁이그리기()
        먹이그리기()
        

        pygame.display.update()
        클릭.tick(5)

main()

