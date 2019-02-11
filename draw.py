from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #undefined
    if((x1-x0) == 0):
        while(y0 <= y1):
            plot(screen,color,x0,y0)
            y0+=1
        pass
    x,y = x0,y0
    a = y1 - y0
    b = -(x1 - x0)
    #octant I and V
    if(y0<=y1):
        if(abs(a)<=abs(b)):
            d = 2*a + b
            while(x<=x1):
                plot(screen,color,x,y)
                if (d>0):
                    y+=1
                    d+= (2*b)
                x+=1
                d+=(2*a)
        #octant II and VI
        else:
            d = a + 2*b
            while(y<=y1):
                plot(screen,color,x,y)
                if (d<0):
                    x+=1
                    d += (2*a)
                y+=1
                d+=(2*b)
    #octant III and VII
    else:
        if(abs(a)>abs(b)):
            d = 2*a + b
            while(y>=y1):
                plot(screen,color,x,y)
                if (d>0):
                    x +=1
                    d += (2*a)
                y -= 1
                d -=(2*b)
    #octant IV and VIII
        else:
            d = a + 2*b
            while(x<=x1):
                plot(screen,color,x,y)
                if (d<0):
                    y -= 1
                    d -= (2*b)
                x += 1
                d +=(2*a)
    pass
