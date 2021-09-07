import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import cos, sin

import random
from random import *


class Click:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.width = 800
        self.height = 600
        self.size = 10
        self.vel_x = 4
        self.vel_y = 10


        self.going_left = False
        self.going_right = False
        self.jump = False

        pygame.display.init()
        pygame.display.set_mode((self.width, self.height), DOUBLEBUF|OPENGL)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glViewport(0, 0, 800, 600)
        gluOrtho2D(0, 800, 0, 600)

        glBegin(GL_TRIANGLES)
        glColor3f(0.5, 0.2, 1.0)

        glVertex2f(self.x_pos, self.y_pos)
        glVertex2f(self.x_pos, self.y_pos + 10)
        glVertex2f(self.x_pos + 10, self.y_pos)

        glVertex2f(self.x_pos + 10, self.y_pos)
        glVertex2f(self.x_pos + 10, self.y_pos + 10)
        glVertex2f(self.x_pos, self.y_pos + 10)

        glEnd()

        pygame.display.flip()
    def update(self):
        if self.going_left:
            if self.x_pos > 0:
                self.x_pos -= self.vel_x
    
        if self.going_right:
            if self.x_pos < self.width - self.size:
                self.x_pos += self.vel_x

        if self.jump:
            self.y_pos += self.vel_y
            self.vel_y -= 1
            if self.vel_y < -10:
                self.jump = False
                self.vel_y = 10
                

    def game_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Keydown events
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_q:
                    glClearColor(random(), random(), random(), 1.0)
            
                elif event.key == K_LEFT:
                    self.going_left = True

                elif event.key == K_RIGHT:
                    self.going_right = True

                elif event.key == K_SPACE and self.jump == False:
                    self.jump = True

                elif event.key == K_UP and self.jump == False:
                    self.jump = True

            # Keyup events
            elif event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    self.going_left = False

                elif event.key == K_RIGHT:
                    self.going_right = False


        pygame.time.delay(10)
        self.update()
        self.display()

if __name__ == "__main__":
    click = Click()
    while True:
        click.game_loop()