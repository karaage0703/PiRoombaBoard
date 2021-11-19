#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math
from pyroombaadapter import PyRoombaAdapter
import pygame
from pygame.locals import *
import sys

PORT = "/dev/ttyUSB0"
adapter = PyRoombaAdapter(PORT)

pygame.init()
screen = pygame.display.set_mode((400, 330))    # 画面を作成
pygame.display.set_caption("keyboard event")    # タイトルを作成

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if pygame.key.name(event.key) == 'a':
                print('turn left')
                adapter.move(0, math.radians(20))

            if pygame.key.name(event.key) == 'd':
                print('turn right')
                adapter.move(0, math.radians(-20))

            if pygame.key.name(event.key) == 'w':
                print('go straight')
                adapter.move(0.2, math.radians(0.0))

            if pygame.key.name(event.key) == 's':
                print('turn right')
                adapter.move(0, math.radians(0))

            if pygame.key.name(event.key) == 'x':
                print('go back')
                adapter.move(-0.2, math.radians(0.0))
            else:
                print("key= " + pygame.key.name(event.key))
        pygame.display.update()
