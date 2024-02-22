import turtle as t
from PIL import Image
class Render:
    def __init__(self):
        self.wn = t.Screen()
        
    def save(self):
        self.wn.getcanvas().postscript(file='render.eps')
        Image.open("render.eps").save('render.png', 'PNG')