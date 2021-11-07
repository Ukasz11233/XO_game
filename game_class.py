from settings import *
from Functions import *
from sprite_class import *
import pygame


class Game:
    def __init__(self):  # Intializing game
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Kolko i krzyzyk")
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        self.running = True
        self.clicked = False
        self.board = [[0]*3 for _ in range(3)]            # 1 for X, -1 for O


    def run(self):  # Main game loop
        self.sprites.add(Sprite((10, 10)), Sprite((176, 0)), Sprite((342, 0)),
                        Sprite((0, 176)), Sprite((176, 176)), Sprite((342, 176)),
                        Sprite((0, 342)), Sprite((176, 342)), Sprite((342, 342)))
        while self.running:
            self.clock.tick(FPS)
            self.get_events()
            self.update()
            self.draw()
        pygame.quit()


    def draw(self):
        blank = SCREEN_HEIGHT / 3
        x, y = 0, 0
        self.screen.fill(BLACK)
        self.sprites.draw(self.screen)
        for i in range(3):
            x += blank
            y += blank
            pygame.draw.line(self.screen, (WHITE), (x, 0), (x, SCREEN_HEIGHT), width = 5)
            pygame.draw.line(self.screen, (WHITE), (0, y), (SCREEN_HEIGHT, y), width = 5)


        # *after* drawing everything flip the display
        pygame.display.flip()


    def update(self):
        self.sprites.update()
        if check(self.board) == 1:
            self.draw()
            message_box("Message", "X wygral!\nZagraj jeszcze raz")
            run_again(self.sprites, self.board)
            self.clicked = False
        elif check(self.board) == -1:
            self.draw()
            message_box("Message", "O wygral\nZagraj jeszcze raz")
            run_again(self.sprites, self.board)
            self.clicked = False
        elif check(self.board) == 2:
            self.draw()
            message_box("Message", "Nikt nie wygral\nZagraj jeszcze raz")
            run_again(self.sprites, self.board)
            self.clicked = False


    def get_events(self):
        ev_list = pygame.event.get()
        for event in ev_list:
            #check for closing the window
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ev in self.sprites:
                    if ev.click(event, self.clicked, self.board):
                        self.clicked = not self.clicked


