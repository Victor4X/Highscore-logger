import pygame
from serverHandler import Handler


class Game:
    def __init__(self):
        self.state = 0
        self.Handler = Handler()
        self.t = 0
        self.dots = []
        self.tempdots = []
        # State 0: Menu
        # State 1: Game
        self.slidRed = pygame.Rect(4,4,255,30)
        self.slidGreen = pygame.Rect(4,38,255,30)
        self.slidBlue = pygame.Rect(4,72,255,30)

        self.color = [0,0,0]
        # State 2: Pause

    def tick(self, pg, pressed):
        self.x, self.y = pygame.mouse.get_pos()
        if self.state == 1:
            if (pressed[pg.K_e] or pressed[pg.K_w]):
                self.t = 0
                if pygame.Rect(self.x,self.y,1,1).collidelist([self.slidRed,self.slidGreen,self.slidBlue]) != -1:
                    self.color[pygame.Rect(self.x,self.y,1,1).collidelist([self.slidRed,self.slidGreen,self.slidBlue])] = abs(self.x-5)
                else:
                    self.tempdots.append([self.color,(self.x,self.y)])
                    
            self.t += 1

    def start_game(self):
        if self.state == 0:
            self.state = 1

    def end_game(self):
        if self.state > 0:
            self.state = 0

    def started(self):
        if self.state > 0:
            return True
        else:
            return False


def draw_game():
    if game.state == 0:
        pygame.draw.rect(screen, (30, 30, 30),
                         pygame.Rect(380, 280, 80, 50))
        screen.blit(myfont.render(
            "MENU", 1, (255, 255, 255)), (400, 300))
    elif game.state == 1:
        
        screen.fill((0, 10, 20))
        for d in game.dots:
            c = d[0]
            x,y = d[1]
            pygame.draw.circle(screen,c,(x,y),2,0)
        for d in game.tempdots:
            c = d[0]
            x,y = d[1]
            pygame.draw.circle(screen,c,(x,y),2,0)

        pygame.draw.rect(screen,(200,200,200),game.slidRed, 2)
        slidRedFill = game.slidRed.copy()
        slidRedFill.width = game.color[0]
        pygame.draw.rect(screen,(game.color),slidRedFill, 0)

        pygame.draw.rect(screen,(200,200,200),game.slidGreen, 2)
        slidGreenFill = game.slidGreen.copy()
        slidGreenFill.width = game.color[1]
        pygame.draw.rect(screen,(game.color),slidGreenFill, 0)

        pygame.draw.rect(screen,(200,200,200),game.slidBlue, 2)
        slidBlueFill = game.slidBlue.copy()
        slidBlueFill.width = game.color[2]
        pygame.draw.rect(screen,(game.color),slidBlueFill, 0)

        #Update stuffs
        if (game.t+120)%120 == 0:
            game.dots[:] = []
            for d in game.Handler.update(game.tempdots):
                c,x,y = d["color"],d["x"],d["y"]
                game.dots.append([c,(x,y)])
            game.tempdots[:] = []
                


pygame.init()
screen = pygame.display.set_mode((800, 600))
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

done = False

game = Game()

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            game.toggle_pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game.started():
                game.end_game()
            else:
                game.start_game()

    pressed = pygame.key.get_pressed()

    game.tick(pygame, pressed)
    draw_game()

    pygame.display.flip()
    clock.tick(60)
