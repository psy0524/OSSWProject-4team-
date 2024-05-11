import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("키보드 움직임과 점프")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 캐릭터 속성 설정
character_width, character_height = 50, 50
character_x, character_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - character_height * 2
character_speed = 10
jump_height = 10
is_jump = False

clock = pygame.time.Clock()

# 키 입력 상태 저장
left_pressed = False
right_pressed = False

# 게임 루프
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 키를 누르는 이벤트 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_SPACE and not is_jump:
                is_jump = True

        # 키를 뗄 때의 이벤트 처리
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_RIGHT:
                right_pressed = False

    # 캐릭터의 이동 처리
    if left_pressed:
        character_x -= character_speed
    if right_pressed:
        character_x += character_speed

    # 캐릭터가 화면 밖으로 나가지 않도록 처리
    character_x = max(0, min(character_x, SCREEN_WIDTH - character_width))

    # 캐릭터의 점프 처리
    if is_jump:
        if jump_height >= -10:
            neg = 1
            if jump_height < 0:
                neg = -1
            character_y -= (jump_height ** 2) * 0.5 * neg
            jump_height -= 1
        else:
            is_jump = False
            jump_height = 10

    # 캐릭터 그리기
    pygame.draw.rect(screen, RED, (character_x, character_y, character_width, character_height))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
