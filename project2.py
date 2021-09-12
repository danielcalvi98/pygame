import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import cos, sin

import random
from random import *

#Gameobjects

class Pillar:
    def __init__(self,size, x_pos, height):
        self.size = size
        self.x_pos = x_pos
        self.y_pos = 0
        self.height = height

    def left_collision(self, x_pos, y_pos, size):
        if self.x_pos + self.size >= x_pos > self.x_pos and y_pos + size >= self.y_pos and y_pos < self.y_pos + self.height:
            return True

    def right_collision(self, x_pos, y_pos, size):
        if self.x_pos <= x_pos + size and x_pos + size <= self.x_pos + self.size and y_pos >= self.y_pos and y_pos < self.y_pos + self.height:
            return True

    def top_collision(self, x_pos, y_pos, size):
        if self.y_pos + self.height >= y_pos:
            if self.x_pos + self.size >= x_pos >= self.x_pos or self.x_pos <= x_pos + size <= self.x_pos + self.size:
                return True
        else:
            return False
    
    def bottom_collision(self, x_pos, y_pos, size):
        if self.y_pos >= y_pos + size:
            if self.x_pos + self.size >= x_pos > self.x_pos or self.x_pos <= x_pos + size < self.x_pos + self.size:
                return True
        else:
            return False

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3f(255, 255, 0)

        # Character
        glVertex2f(self.x_pos, self.y_pos)
        glVertex2f(self.x_pos, self.y_pos + self.height)
        glVertex2f(self.x_pos + self.size, self.y_pos)

        glVertex2f(self.x_pos + self.size, self.y_pos)
        glVertex2f(self.x_pos + self.size, self.y_pos + self.height)
        glVertex2f(self.x_pos, self.y_pos + self.height)
        glEnd()

class Tile:
    def __init__(self, size, x_pos, y_pos ):
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos

    def left_collision(self, x_pos, y_pos, size):
        if self.x_pos + self.size >= x_pos > self.x_pos and y_pos + size >= self.y_pos and y_pos < self.y_pos + self.size:
            return True

    def right_collision(self, x_pos, y_pos, size):
        if self.x_pos <= x_pos + size and x_pos + size <= self.x_pos + self.size and y_pos >= self.y_pos and y_pos < self.y_pos + self.size:
            return True

    def top_collision(self, x_pos, y_pos, size):
        if self.y_pos + self.size >= y_pos:
            if self.x_pos + self.size >= x_pos >= self.x_pos or self.x_pos <= x_pos + size <= self.x_pos + self.size:
                return True
        else:
            return False
    def bottom_collision(self, x_pos, y_pos, size):
        if self.y_pos >= y_pos + size:
            if self.x_pos + self.size >= x_pos > self.x_pos or self.x_pos <= x_pos + size < self.x_pos + self.size:
                return True
        else:
            return False

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3f(255, 255, 0)

        glVertex2f(self.x_pos, self.y_pos)
        glVertex2f(self.x_pos, self.y_pos + self.size)
        glVertex2f(self.x_pos + self.size, self.y_pos)

        glVertex2f(self.x_pos + self.size, self.y_pos)
        glVertex2f(self.x_pos + self.size, self.y_pos + self.size)
        glVertex2f(self.x_pos, self.y_pos + self.size)
        glEnd()


class Victory_tile(Tile):
    def __init__(self, size, x_pos, y_pos):
        super().__init__(size, x_pos, y_pos)

    def left_collision(self, x_pos, y_pos, size):
        if self.x_pos + self.size >= x_pos > self.x_pos and y_pos + size >= self.y_pos and y_pos < self.y_pos + self.size:
            return True

    def right_collision(self, x_pos, y_pos, size):
        if self.x_pos <= x_pos + size and x_pos + size <= self.x_pos + self.size and y_pos >= self.y_pos and y_pos < self.y_pos + self.size:
            return True

    def top_collision(self, x_pos, y_pos, size):
        if self.y_pos + self.size >= y_pos:
            if self.x_pos + self.size >= x_pos >= self.x_pos or self.x_pos <= x_pos + size <= self.x_pos + self.size:
                return True
        else:
            return False
            
    def bottom_collision(self, x_pos, y_pos, size):
        if self.y_pos >= y_pos + size:
            if self.x_pos + self.size >= x_pos > self.x_pos or self.x_pos <= x_pos + size < self.x_pos + self.size:
                return True
        else:
            return False

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3f(0, 0, 255)

        glVertex2f(self.x_pos, self.y_pos)
        glVertex2f(self.x_pos, self.y_pos + self.size)
        glVertex2f(self.x_pos + self.size, self.y_pos)

        glVertex2f(self.x_pos + self.size, self.y_pos)
        glVertex2f(self.x_pos + self.size, self.y_pos + self.size)
        glVertex2f(self.x_pos, self.y_pos + self.size)
        glEnd()

class Moving_tile(Tile):
    def __init__(self, size, x_pos, y_pos, speed):
        super().__init__(size, x_pos, y_pos)
        self.speed = speed
        self.is_right = True

    def left_collision(self, x_pos, y_pos, size):
        if self.x_pos + self.size >= x_pos > self.x_pos and y_pos >= self.y_pos and y_pos < self.y_pos + self.size:
            return True

    def right_collision(self, x_pos, y_pos, size):
        if self.x_pos < x_pos + size <= self.x_pos + self.size and y_pos >= self.y_pos and y_pos < self.y_pos + self.size:
            return True

    def top_collision(self, x_pos, y_pos, size):
        if self.y_pos + self.size >= y_pos:
            if self.x_pos + self.size >= x_pos > self.x_pos or self.x_pos <= x_pos + size < self.x_pos + self.size:
                return True
        else:
            return False

    def update(self):
        if self.is_right:
            self.x_pos += self.speed
            if self.x_pos + self.size >= 800:
                self.is_right = False
                return
        else:
            self.x_pos -= self.speed
            if self.x_pos <= 0:
                self.is_right = True
                return

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3f(255, 0, 0)

        # Character
        glVertex2f(self.x_pos, self.y_pos)
        glVertex2f(self.x_pos, self.y_pos + self.size)
        glVertex2f(self.x_pos + self.size, self.y_pos)

        glVertex2f(self.x_pos + self.size, self.y_pos)
        glVertex2f(self.x_pos + self.size, self.y_pos + self.size)
        glVertex2f(self.x_pos, self.y_pos + self.size)
        glEnd()


# Main Game
class TwoDgame:
    def __init__(self):
        self.x_pos = 390
        self.y_pos = 700
        self.width = 800
        self.height = 600
        self.size = 19
        self.char_color = [0.5, 0.2, 1.0]
        self.vel_x = 4
        self.vel_y = 10
        self.gravity = 2
        self.game_won = False
        self.draw_moving_tile = True

        # Game rules
        self.game_on = True

        # Movement
        self.going_left = False
        self.going_right = False
        self.jump = False
        self.jump_multiplier = 2
        self.powerjump = False
        self.falling = False

        # Game Objects
        self.box1 = Pillar(50, 20, 50)
        self.box2 = Pillar(50, 300, 500)
        self.box3 = Pillar(60, 390, 100)
        self.box4 = Pillar(50, 450, 500)
        self.box5 = Pillar(50, 700, 200)
        self.victorytile = Victory_tile(35, 705, 200)
        self.moving_box1 = Moving_tile(20, 0, 50, 1)
        

        self.game_objects = [
            self.box1,
            self.box2,
            self.box3,
            self.box4,
            self.box5
        ]

        # Init pygame
        pygame.display.init()
        pygame.display.set_mode((self.width, self.height), DOUBLEBUF|OPENGL)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def game_over(self):
        if self.y_pos <= 0:
            glClearColor(255, 0, 0, 1.0)
            self.game_on = False
        
        if self.game_won:
            glClearColor(0, 0, 255, 1.0)
            self.game_on = False 
            print("GAME WON")
        

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glViewport(0, 0, 800, 600)
        gluOrtho2D(0, 800, 0, 600)

        glBegin(GL_TRIANGLES)
        glColor3f(self.char_color[0], self.char_color[1], self.char_color[2])

        # Character
        glVertex2f(self.x_pos, self.y_pos)
        glVertex2f(self.x_pos, self.y_pos + self.size)
        glVertex2f(self.x_pos + self.size, self.y_pos)

        glVertex2f(self.x_pos + self.size, self.y_pos)
        glVertex2f(self.x_pos + self.size, self.y_pos + self.size)
        glVertex2f(self.x_pos, self.y_pos + self.size)
        glEnd()
        

        # Game Objects
        for game_object in self.game_objects:
            game_object.draw()
            
        if self.draw_moving_tile:
            self.moving_box1.draw()
        else:
            self.victorytile.draw()

        pygame.display.flip()

    def update(self):
        if self.powerjump:
            self.char_color = [255, 0, 0]
            self.vel_x = 10

        if self.y_pos == 0:
            self.falling = False


        if self.falling and self.y_pos > 0:
            self.y_pos -= self.gravity
            
        if self.going_left:
            col = False
            for game_object in self.game_objects:
                if game_object.left_collision(self.x_pos, self.y_pos, self.size):
                    col = True
            if self.x_pos > 0 and col == False:
                self.x_pos -= self.vel_x
    
        if self.going_left:
            if self.moving_box1.left_collision(self.x_pos, self.y_pos, self.size):
                self.powerjump = True 
                self.draw_moving_tile = False

        if self.going_left:
            if self.victorytile.left_collision(self.x_pos, self.y_pos, self.size):
                self.game_won = True


        if self.going_right:
            col = False
            for game_object in self.game_objects:
                if game_object.right_collision(self.x_pos, self.y_pos, self.size):
                    col = True
            if self.x_pos < self.width - self.size and col == False:
                self.x_pos += self.vel_x
        
        if self.going_right:
            if self.moving_box1.right_collision(self.x_pos, self.y_pos, self.size):
                self.powerjump = True
                self.draw_moving_tile = False

        if self.going_right:
            if self.victorytile.right_collision(self.x_pos, self.y_pos, self.size):
                self.game_won = True

        if self.jump:
            if self.powerjump:
                self.jump_multiplier = 4
            self.y_pos += self.vel_y * self.jump_multiplier
            self.vel_y -= 1
            if self.vel_y < 0:
                self.jump = False
                self.vel_y = 10

        # collision check
    def check_collision(self):
        for game_object in self.game_objects:
            if game_object.top_collision(self.x_pos, self.y_pos, self.size) and self.y_pos > 0:
                self.falling = False
                return
            else:
                self.falling = True
        
        if self.moving_box1.top_collision(self.x_pos, self.y_pos, self.size):
            self.powerjump = True
            self.draw_moving_tile = False

        if self.victorytile.top_collision(self.x_pos, self.y_pos, self.size):
            self.game_won = True
            

    def game_loop(self):
        # Physics
        self.check_collision()
        
        # In game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Keydown events
            elif event.type == pygame.KEYDOWN:
                if self.game_on:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == K_q:
                        glClearColor(random(), random(), random(), 1.0)
                
                    elif event.key == K_LEFT:
                        self.going_left = True

                    elif event.key == K_RIGHT:
                        self.going_right = True

                    elif event.key == K_SPACE and self.jump == False and self.falling == False:
                        self.jump = True

                    elif event.key == K_UP and self.jump == False and self.falling == False:
                        self.jump = True
                else:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == K_RETURN:
                        self.__init__()


            # Keyup events
            elif event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    self.going_left = False

                elif event.key == K_RIGHT:
                    self.going_right = False

        pygame.time.delay(10)
        if self.game_on:
            self.game_over()
            self.moving_box1.update()
            self.update()
            self.display()
            
            

if __name__ == "__main__":
    game = TwoDgame()
    while True:
        game.game_loop()