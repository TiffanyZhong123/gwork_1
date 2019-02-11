from display import *
from draw import *
from math import *

screen = new_screen()
color = [ 0, 200, 0 ]
y = 100
#for x in range(0,500,5):
def drawtri(startx,starty,screen,color,base,height):
    draw_line(startx,starty,startx+base,starty,screen,color)
    draw_line(startx,starty,(startx+base)/2,starty+height,screen,color)
    draw_line((startx+base)/2,starty+height,startx+base,starty,screen,color)
def drawdowntri(startx,starty,screen,color,base,height):
    draw_line(startx,starty,startx+base,starty,screen,color)
    draw_line(startx,starty,(startx+base)/2,starty-height,screen,color)
    draw_line((startx+base)/2,starty-height,startx+base,starty,screen,color)
def drawleftsidetri(startx,starty,screen,color,base,height):
    draw_line(startx,starty,startx,starty+base,screen,color)
    draw_line(startx,starty,startx+height,(starty+base)/2,screen,color)
    draw_line(startx,starty+base,startx+height,(starty+base)/2,screen,color)
def drawrightsidetri(startx,starty,screen,color,base,height):
    draw_line(startx,starty,startx,starty+base,screen,color)
    draw_line(startx-height,(starty+base)/2,startx,starty,screen,color)
    draw_line(startx-height,(starty+base)/2,startx,starty+base,screen,color)
for x in range(0,62):
    y += 2
    color = [0,y,0]
    drawtri(0,0,screen,color,499,x*8)
y= 100
for x in range(0,62):
    y+=2
    color=[0,0,y]
    drawdowntri(0,499,screen,[0,0,200],499,x*8)
y = 100
for x in range(0,62):
    y+=2
    color=[y,0,0]
    drawleftsidetri(0,0,screen,[200,0,0],499,x*8)
color= [110,103,12]
for x in range(0,62):
    color[0] += 2
    color[1] += 2
    color[2] += 2
    drawrightsidetri(499,0,screen,color,499,x*8)

display(screen)
save_extension(screen, 'img.png')
