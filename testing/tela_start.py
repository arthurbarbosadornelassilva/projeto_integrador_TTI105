import pygame
import sys

class TelaExplicacao:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 960, 680
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Explicação do Jogo de Labirinto")
        self.font = pygame.font.Font('font/PixelifySans-Bold.ttf', 18)
        self.running = True

        # Carregar imagens
        self.up_arrow = pygame.image.load("img/w.png")
        self.down_arrow = pygame.image.load("img/s.png")
        self.left_arrow = pygame.image.load("img/a.png")
        self.right_arrow = pygame.image.load("img/d.png")
        self.space = pygame.image.load("img/space.png")

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.running = False

            self.screen.fill((0,0,0))# Desenha o fundo personalizado
            self.draw_text("Como jogar o Vacman:", self.font, (255, 255, 255), self.screen, 120, 20)
            self.draw_text("São 4 fases + 1 com o final boss. Cada fase tem 4 virus que precisam ser derrotados para avançar de fase, ", self.font, (255, 255, 255), self.screen, 480, 50)  
            self.draw_text("você derrota eles acertando corretamente as perguntas, que são geradas ao encostar neles.", self.font, (255,255,255), self.screen, 395, 80)       
            
    
            self.draw_text("Use as setas do teclado para mover o personagem:", self.font, (255, 255, 255), self.screen, 230, 140)

            # Desenhar setas e textos explicativos
            self.screen.blit(self.up_arrow, (50, 180))
            self.draw_text("Mover para cima", self.font, (255, 255, 255), self.screen, 200, 205)

            self.screen.blit(self.down_arrow, (50, 260))
            self.draw_text("Mover para baixo", self.font, (255, 255, 255), self.screen, 203, 285)

            self.screen.blit(self.left_arrow, (50, 340))
            self.draw_text("Mover para a esquerda", self.font, (255, 255, 255), self.screen, 225, 365)

            self.screen.blit(self.right_arrow, (50, 420))
            self.draw_text("Mover para a direita", self.font, (255, 255, 255), self.screen, 210, 445)

            self.screen.blit(self.space, (50, 500))
            self.draw_text("Pausar o jogo", self.font, (255, 255, 255), self.screen, 240, 525)

            self.draw_text("Pressione Enter para começar o jogo", self.font, (255, 255, 255), self.screen, 170, 600)

            pygame.display.flip()

        # Quando o usuário pressiona Enter, saímos do loop e podemos iniciar o jogo
        self.start_game()

    def start_game(self):
        print("Iniciando o jogo de labirinto...")

if __name__ == "__main__":
    tela_explicacao = TelaExplicacao()
    tela_explicacao.run()
