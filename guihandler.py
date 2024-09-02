import pygame as pg

pg.init()
pg.font.init()

def normalize(array, ratio):
    return [i * ratio for i in array]

class disp:
    def __init__(self, dims=[800, 800]):
        self.disp = pg.display.set_mode(dims[:])
        self.conv_rat = (dims[0] * dims[1] / 640000)
        self.dims = dims[:]
    
class textLable:
    def __init__(self, target_disp, args):
        # args = {"msg" : text, "size" : size, "pos" : pos, "font" : font, "col" : color}
        self.target_disp = target_disp
        self.args = args[:]
    
    def add(self):
        font = pg.font.SysFont(self.args["font"], self.args["size"]*self.target_disp.conv_rat)
        text_surface = font.render(self.args["msg"], False, self.args["col"])
        self.target_disp.disp.blit(text_surface, normalize(self.args["pos"], self.target_disp.conv_rat))
        pg.display.update()

class textInp:
    def __init__(self, target_disp, args):
        self.target_disp = target_disp
        self.args = args[:]
    
    
        