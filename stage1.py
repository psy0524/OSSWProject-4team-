import pygame
import sys

def run_stage():
    pygame.init()

    # 화면 크기 설정
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("스테이지 1")

    # 색깔 정의
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    FLOOR_COLOR = (144, 228, 144)

    # 캐릭터 속성 설정
    character_width, character_height = 50, 50
    character_x, character_y = 50, 50
    character_speed = 10

    # 바닥 속성 설정
    floor_height = 22
    floor_y = SCREEN_HEIGHT - floor_height

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)
        character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_x -= character_speed
        if keys[pygame.K_RIGHT]:
            character_x += character_speed

        # 화면 범위 제한 및 바닥 충돌 처리
        character_x = max(0, min(SCREEN_WIDTH - character_width, character_x))
        character_y = min(character_y, floor_y - character_height)

        # 바닥 그리기
        pygame.draw.rect(screen, FLOOR_COLOR, (0, floor_y, SCREEN_WIDTH, floor_height))

        # 캐릭터 그리기
        pygame.draw.rect(screen, RED, character_rect)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()
