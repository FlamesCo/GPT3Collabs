## use gpt-2 tokeninzer to write pong using ataris engine from github code
import os
import time
import random
import sys
## make a atari game engine for pygame and addd pong to import
import pygame as pg
from pygame.locals import *
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.models import load_model
from keras.models import model_from_json
from keras.models import model_from_yaml
from keras.models import load_model
## make the game engine for pong and its code from a random github repo with its code from ataris database
atariengine=pg.init()
## make the game window for pong
screen=pg.display.set_mode((600,500))
## make the game window title for pong
pg.display.set_caption("Pong")
## make the game window background color for pong
bgcolor=(0,0,0)
