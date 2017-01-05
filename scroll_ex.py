# Eric Lu

import pygame
import sys


class ScrollApp:

    def __init__(self):

        self.x1 = 0
        self.y1 = 0
        self.x2 = 800
        self.y2 = 0

        # Creates a window and title
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption('Scroll - Eric Lu')

        # Loads background image
        self.bg = pygame.image.load('background.jpg')
        self.screen.blit(self.bg, (0,0))

    def mainloop(self):

        while True:

            for event in pygame.event.get():

                pressed = pygame.key.get_pressed()

                if (event.type == pygame.QUIT):        
                    pygame.quit()
                    sys.exit()

                if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
                    self.x2 -= 50
                    self.x1 -= 50

                if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]):
                    self.x2 += 50
                    self.x1 += 50

                if (self.x1 < -800):
                    self.x1 = -50
                    self.x2 = 750

                if (self.x2 > 800):
                    self.x1 = -750
                    self.x2 = 50

            self.screen.blit(self.bg, (self.x1, self.y1))
            self.screen.blit(self.bg, (self.x2, self.y2))

            pygame.display.update()

if __name__ == '__main__':
    ScrollApp().mainloop()
