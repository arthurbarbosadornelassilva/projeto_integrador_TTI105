import pygame
import sys

class EscolhePersonagem:

    def __init__(self):
        # Inicializa o Pygame
        pygame.init()

        # Configurações da tela
        self.screen_width = 960
        self.screen_height = 680
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Escolha seu Personagem')

        # Cores
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Carregar imagens dos personagens e fundo
        self.char1_image = pygame.image.load('img/linf_b.png')
        self.char2_image = pygame.image.load('img/linf_t.png')
        self.bg_image = pygame.image.load('img/Fundo veia.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))

        # Dimensões dos personagens
        self.char_width = self.char1_image.get_width()
        self.char_height = self.char1_image.get_height()

        # Constante para deslocar a posição y
        self.y_offset = 70

        # Posições dos personagens
        self.char1_pos = (self.screen_width // 3 - self.char_width // 2, self.screen_height // 2 - self.char_height // 4 + self.y_offset)
        self.char2_pos = (2 * self.screen_width // 3 - self.char_width // 2, self.screen_height // 2 - self.char_height // 4 + self.y_offset)
        self.char3_pos = (self.screen_width // 2 - self.char_width // 2, self.screen_height // 4 - self.char_height // 4 + self.y_offset)

        # Fonte
        self.font1 = pygame.font.Font('font/PixelifySans-Regular.ttf', 32)

        # Botão Voltar
        self.voltar_button = self.create_rounded_button(430, 500, 100, 50, (106, 13, 173), 10, text="Voltar")

    def create_rounded_button(self, x, y, width, height, color, radius, text=" ", text_color=(255, 255, 255), font_size=30):
        button = {}
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
        pos = pygame.mouse.get_pos()

        if button['rect'].collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not button['clicked']:
                button['clicked'] = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            button['clicked'] = False

        pygame.draw.rect(surface, button['color'], button['rect'], border_radius=button['radius'])
        text_rect = button['text_surface'].get_rect(center=button['rect'].center)
        surface.blit(button['text_surface'], text_rect)

        return action

    def display_message(self, text):
        message = self.font1.render(text, True, self.WHITE)
        self.screen.blit(message, (self.screen_width // 2 - message.get_width() // 2, self.screen_height // 2.3))

    def display_message2(self, text):
        message = self.font1.render(text, True, self.WHITE)
        self.screen.blit(message, (self.screen_width // 2 - message.get_width() // 2, self.screen_height // 7))

    def main_screen(self):
        running = True
        selected_character = None

        while running:
            self.screen.blit(self.bg_image, (0, 0))

            self.screen.blit(self.char1_image, self.char1_pos)
            self.screen.blit(self.char2_image, self.char2_pos)

            self.display_message("Pressione 1 ou 2 para escolher o personagem")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_character = 'Personagem 1'
                    elif event.key == pygame.K_2:
                        selected_character = 'Personagem 2'

            if selected_character:
                self.screen.fill(self.BLACK)
                self.display_message2(f'Você escolheu o {selected_character}!')
                if selected_character == 'Personagem 1':
                    self.screen.blit(self.char1_image, self.char3_pos)
                elif selected_character == "Personagem 2":
                    self.screen.blit(self.char2_image, self.char3_pos)
                if self.draw_rounded_button(self.screen, self.voltar_button):
                    selected_character = None

            pygame.display.flip()

if __name__ == "__main__":
    jogo = EscolhePersonagem()
    jogo.main_screen()
    pygame.quit()
