import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout with Coins and Animation")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)  # Для анимации

# Параметры шара
BALL_RADIUS = 10
ball_x = WIDTH // 2
ball_y = HEIGHT - 50
ball_dy = 0
ball_dx = 0
balls_left = 10

# Параметры платформы
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - 30
paddle_speed = 8

# Параметры блоков
BLOCK_WIDTH = WIDTH // 10  # 10 колонн
BLOCK_HEIGHT = 30
blocks = []
score = 0

# Параметры монетки
COIN_RADIUS = 10
coin_x = random.randint(COIN_RADIUS, WIDTH - COIN_RADIUS)
coin_y = random.randint(HEIGHT // 2, HEIGHT - COIN_RADIUS)
coin_active = True
coins_collected = 0

# Анимация разрушения блока
explosions = []  # Список для хранения анимаций (x, y, frame)

# Создание блоков (10 рядов, 10 колонн)
for row in range(10):
    for col in range(10):
        block = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT + 50,
                            BLOCK_WIDTH - 2, BLOCK_HEIGHT - 2)
        blocks.append(block)

# Игровой цикл
clock = pygame.time.Clock()
running = True
active_ball = False

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active_ball:
            if event.key == pygame.K_SPACE and balls_left > 0:
                ball_x = paddle_x + PADDLE_WIDTH // 2
                ball_y = paddle_y - BALL_RADIUS
                ball_dy = -5
                ball_dx = random.uniform(-2, 2)
                active_ball = True
                balls_left -= 1

    # Управление платформой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += paddle_speed

    # Логика движения шара
    if active_ball:
        ball_y += ball_dy
        ball_x += ball_dx

        # Отскок от стен
        if ball_x <= BALL_RADIUS or ball_x >= WIDTH - BALL_RADIUS:
            ball_dx = -ball_dx
        if ball_y <= BALL_RADIUS:
            ball_dy = -ball_dy

        # Отскок от платформы
        paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        if paddle.collidepoint(ball_x, ball_y + BALL_RADIUS) and ball_dy > 0:
            ball_dy = -ball_dy
            hit_pos = (ball_x - paddle_x) / PADDLE_WIDTH
            ball_dx = 6 * (hit_pos - 0.5)

        # Проверка столкновения с блоками
        for block in blocks[:]:
            if block.collidepoint(ball_x, ball_y):
                blocks.remove(block)
                ball_dy = -ball_dy
                ball_dx += random.uniform(-1, 1)
                score += 10
                # Добавляем анимацию разрушения
                explosions.append(
                    [block.x + BLOCK_WIDTH // 2, block.y + BLOCK_HEIGHT // 2, 0])
                break

        # Проверка столкновения с монеткой
        if coin_active:
            coin_rect = pygame.Rect(coin_x - COIN_RADIUS, coin_y - COIN_RADIUS,
                                    COIN_RADIUS * 2, COIN_RADIUS * 2)
            ball_rect = pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS,
                                    BALL_RADIUS * 2, BALL_RADIUS * 2)
            if ball_rect.colliderect(coin_rect):
                coins_collected += 1
                coin_active = False
                coin_x = random.randint(COIN_RADIUS, WIDTH - COIN_RADIUS)
                coin_y = random.randint(HEIGHT // 2, HEIGHT - COIN_RADIUS)
                coin_active = True

        # Шар упал вниз
        if ball_y > HEIGHT:
            active_ball = False

    # Обновление анимации разрушения
    for explosion in explosions[:]:
        explosion[2] += 1  # Увеличиваем кадр анимации
        if explosion[2] > 10:  # Анимация длится 10 кадров
            explosions.remove(explosion)

    # Отрисовка
    screen.fill((0, 0, 0))

    # Рисуем блоки
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block)

    # Рисуем платформу
    pygame.draw.rect(screen, GREEN, (paddle_x, paddle_y,
                     PADDLE_WIDTH, PADDLE_HEIGHT))

    # Рисуем шар
    if active_ball:
        pygame.draw.circle(
            screen, RED, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Рисуем монетку
    if coin_active:
        pygame.draw.circle(
            screen, YELLOW, (int(coin_x), int(coin_y)), COIN_RADIUS)

    # Рисуем анимацию разрушения
    for explosion in explosions:
        radius = explosion[2] * 5  # Радиус увеличивается с каждым кадром
        pygame.draw.circle(screen, ORANGE, (int(
            explosion[0]), int(explosion[1])), int(radius), 2)

    # Отображение статистики
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    balls_text = font.render(f"Balls left: {balls_left}", True, WHITE)
    coins_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(balls_text, (10, 40))
    screen.blit(coins_text, (10, 70))

    # Проверка конца игры
    if balls_left <= 0 and not active_ball:
        text = font.render("Game Over! Press Q to quit", True, WHITE)
        screen.blit(text, (WIDTH//2 - 100, HEIGHT//2))
        if pygame.key.get_pressed()[pygame.K_q]:
            running = False

    # Проверка победы
    if not blocks and active_ball:
        text = font.render("You Win! Press Q to quit", True, WHITE)
        screen.blit(text, (WIDTH//2 - 100, HEIGHT//2))
        if pygame.key.get_pressed()[pygame.K_q]:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
