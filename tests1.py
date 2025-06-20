import pygame

pygame.init()

# Параметры экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Текстовое поле ввода")

# Параметры шрифта
font = pygame.font.SysFont('Arial', 30)

# Параметры текстового поля
input_box_rect = pygame.Rect(100, 100, 200, 50)
active_color = (0, 0, 255)
inactive_color = (0, 0, 0)
color = inactive_color
text = ""
active = False

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Обновление цвета текстового поля в зависимости от активности
    if active:
        color = active_color
    else:
        color = inactive_color

    # Отрисовка
    screen.fill((255, 255, 255))  # Белый фон
    pygame.draw.rect(screen, color, input_box_rect)  # Текстовое поле
    text_surface = font.render(text, True, (0, 0, 0))  # Текст
    screen.blit(text_surface, (input_box_rect.x + 5, input_box_rect.y + 5))  # Позиция текста

    pygame.display.flip()  # Обновление экрана

pygame.quit()