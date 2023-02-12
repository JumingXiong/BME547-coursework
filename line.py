def line(point1,point2,x):
    x1,y1 = point1
    x2,y2 = point2
    k = (y2-y1) / (x2-x1)
    b = y1 - k*x1
    y = k*x + b
    return y