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
BLUE = (0, 0, 255)

# 캐릭터 속성 설정
character_width, character_height = 50, 50
character_x, character_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - character_height * 2
character_speed = 10
jump_height = 10
is_jump = False
gravity = 0.5  # 중력 가속도

# 발판 속성 설정
platform_width, platform_height = 100, 20
platform_color = BLUE

# 블록 좌표 설정 (수동으로 지정)
blocks_positions = [
    (100, 400),
    (300, 300),
    (500, 200),
    (700, 100)
]

# 블록 클래스 정의
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 블록 리스트 초기화
blocks = []

# 초기 블록 생성
for pos in blocks_positions:
    block = Block(*pos)
    blocks.append(block)

clock = pygame.time.Clock()

# 키 입력 상태 저장
left_pressed = False
right_pressed = False

# 충돌 감지 함수
def check_collision(character_x, character_y, character_width, character_height, blocks):
    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)
    for block in blocks:
        platform_rect = pygame.Rect(block.x, block.y, platform_width, platform_height)
        if character_rect.colliderect(platform_rect):
            return block  # 충돌한 블록 반환
    return None  # 충돌하지 않음

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

    # 중력 적용
    if not is_jump:
        character_y += gravity

    # 발판 그리기
    for block in blocks:
        pygame.draw.rect(screen, platform_color, (block.x, block.y, platform_width, platform_height))

    # 캐릭터 그리기
    pygame.draw.rect(screen, RED, (character_x, character_y, character_width, character_height))

    # 충돌 검사 및 바닥에 떨어짐 처리
    block_collided = check_collision(character_x, character_y, character_width, character_height, blocks)
    if block_collided:
        # 캐릭터가 블록 위에 있는 경우
        character_y = block_collided.y - character_height  # 캐릭터 위치를 블록 위로 이동
        is_jump = False  # 점프 중인지 여부 초기화
    else:
        # 캐릭터가 바닥에 닿으면 초기화
        if character_y >= SCREEN_HEIGHT - character_height:
            character_y = SCREEN_HEIGHT - character_height
            is_jump = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
