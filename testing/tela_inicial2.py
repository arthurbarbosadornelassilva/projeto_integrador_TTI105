import pygame

class TelaInicial:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 960, 680
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tela inicial")

        self.bg_image = pygame.image.load("fundo1.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (self.WIDTH, self.HEIGHT))

        self.font1 = pygame.font.Font('PixelifySans-Bold.ttf', 85)

        button_radius = 20  # Define o raio para os cantos arredondados do botão
        self.cadastro_button = self.create_rounded_button(395, 430, 200, 60, (106, 13, 173), button_radius, text="Cadastro", text_color=(255, 255, 255), font_size=40)
        self.login_button = self.create_rounded_button(395, 500, 200, 60, (106, 13, 173), button_radius, text="Login", text_color=(255, 255, 255), font_size=40)

    def create_rounded_button(self, x, y, width, height, color, radius, text=" ", text_color=(0, 0, 0), font_size=30):
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

    def draw_rounded_button(self, surface, button):
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

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.bg_image, (0, 0))  # Preencher a tela com a cor de fundo
            self.draw_text("VACMAN", self.font1, (255, 255, 255), self.screen, self.WIDTH // 1.91, 330)

            # Desenhar o botão com bordas arredondadas
            if self.draw_rounded_button(self.screen, self.cadastro_button):
                print("Botão Cadastro!")
            if self.draw_rounded_button(self.screen, self.login_button):
                print("Botão Login!")

            pygame.display.flip()
            pygame.display.update()

        pygame.quit()


# Inicializar e executar a tela inicial
if __name__ == "__inicio__":
    tela_inicial = TelaInicial()
    tela_inicial.run()
