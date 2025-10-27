import pygame

# инициализируем игру

pygame.init()

# создаём экран
screen = pygame.display.set_mode((320,240))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# создаём обьект шрифта
font = pygame.font.Font(None, 42)

while True:
  screen.fill(WHITE) # заполнить фон

  # проверить событие выхода
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()

  # создать текстовую поверхность
  text = font.render("Кот Тимофей", True, BLACK)

  # переместить текстовую поверхность в центр экрана
  screen.blit(text, ((screen.get_width() - text.get_width())/2, (screen.get_height() - text.get_height())/2))

  # обновить экран
  pygame.display.flip()
