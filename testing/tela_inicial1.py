import pygame

class TelaInicial:
    

    # Função para criar um botão com bordas arredondadas
    def create_rounded_button(x, y, width, height, color, radius, text=" ", text_color=(0, 0, 0), font_size=30):
        button = {}  # Dicionário para armazenar os atributos do botão
        button['width'] = width
        button['height'] = height
        button['color'] = color
        button['radius'] = radius
        button['rect'] = pygame.Rect(x, y, width, height)
        button['clicked'] = False
        button['text'] = text
        button['text_color'] = text_color
        button['font'] = pygame.font.SysFont(None, font_size)
        button['text_surface'] = button['font'].render(button['text'], True, button['text_color'])
        return button

    # Função para desenhar um botão com bordas arredondadas
    def draw_rounded_button(surface, button):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if button['rect'].collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and button['clicked'] == False:
                button['clicked'] = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            button['clicked'] = False

        # Draw rounded button on screen
        pygame.draw.rect(surface, button['color'], button['rect'], border_radius=button['radius'])

        # Draw text on button
        text_rect = button['text_surface'].get_rect(center=button['rect'].center)
        surface.blit(button['text_surface'], text_rect)

        return action

    #desenha texto
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)


    # Inicializar o Pygame
    pygame.init()

    #fontees
    font1 = pygame.font.Font('PixelifySans-Bold.ttf', 85)

    # Criar a tela
    WIDTH, HEIGHT = 960, 680
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tela inicial")


    # Cor de fundo
    bg_image = pygame.image.load("fundo1.png")
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))


    # Criar o botão
    button_radius = 20  # Define o raio para os cantos arredondados do botão
    cadastro_button = create_rounded_button(395, 430, 200, 60, (106, 13, 173), button_radius, text="Cadastro", text_color=(255, 255, 255), font_size=40)
    login_button = create_rounded_button(395, 500, 200, 60, (106, 13, 173), button_radius, text="Login", text_color=(255, 255, 255), font_size=40)



    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg_image, (0,0))  # Preencher a tela com a cor de fundo
        draw_text("VACMAN", font1, (255,255,255), screen, WIDTH // 1.91,330)


        # Desenhar o botão com bordas arredondadas
        if draw_rounded_button(screen, cadastro_button):
            print("Botão Cadastro!")
        if draw_rounded_button(screen, login_button):
            print("Botão Login!")

        pygame.display.flip()
        pygame.display.update()

    pygame.quit()

