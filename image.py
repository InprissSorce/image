import pygame
from pygame import surfarray
import numpy as np

def initialize():
    pygame.init()

def quit():
    pygame.quit()    

class Pixel():

    def __init__(self, r, g, b):
        '''
        A pixel is a triple of three integers each in the range 0 - 255.
        The first is the amount of red, the second the amount of blue
        and the third the amount of green.
        '''
        self.red = r
        self.green = g
        self.blue = b

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue

    def __repr__(self):
        red_str = str(self.red)
        green_str = str(self.green)
        blue_str = str(self.blue)
        str_rep = "red = " + red_str + "green = " + green_str + "blue = " + blue_str
        return str_rep

class Image():

    def __init__(self, name, load = False, width = None, height = None, color = (0, 0, 0)):
        '''
        If load is True, an image file will load.
        Otherise an empty imgage will be created.
        '''
        if load:
            img_surface = pygame.image.load(name)
            pix_array = surfarray.array3d(img_surface)
            width, height = pix_array.shape[0], pix_array.shape[1]
        else:
            pix_array = np.full((width, height, 3), color)
            # pix_array = np.zeros((width, height, 3))

        pygame.display.set_caption(name)   

        self.name = name
        self.pix_array = pix_array
        self.width = width
        self.height = height

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
        pygame.display.set_caption("name")

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def draw(self):
        w, h = self.get_width(), self.get_height()
        screen = pygame.display.set_mode((w, h))
        surfarray.blit_array(screen, self.pix_array)
        pygame.display.flip()

    def get_pixel(self, w, h):
        rgb = self.pix_array[w, h]
        red, green, blue = rgb[0], rgb[1], rgb[2]
        pix = Pixel(red, green, blue)
        return pix

    def set_pixel(self, pix, w, h):
        r, g, b = pix.red, pix.green, pix.blue
        self.pix_array[w, h] = (r, g, b)

    def change_name(self, new_name):
        self.name = new_name
        pygame.display.set_caption(name)

    def save(self):
        pygame.image.save(pygame.display.get_surface(), self.name)
    
    def save_as(self, new_name):
        self.name = new_name
        pygame.image.save(pygame.display.get_surface(), self.name)

    def __repr__(self):
        str_rep = self.name + ": " + str(self.width) + ", " + str(self.height)
        return str_rep
