def distance1(x1,y1,x2,y2) :
    d = ((x2-x1)**2+(y2-y1)**2)**0.5
    return d

def distance2(p1,p2) :
    [x1,y1] = p1 
    [x2,y2] = p2
    d = ((x2-x1)**2+(y2-y1)**2)**0.5
    return d

def distance3(c1,c2) :
    [h1,k1,r1] = c1
    [h2,k2,r2] = c2

def perimeter(points) :
    d =0
    for i in range(len(points)-1) :
        d += distance2(points[i],points[i+1])
    d += distance2(points[0],points[-1]) 
    return d

def distance3(c1,c2) :
    [x1,y1,r1] = c1
    [x2,y2,r2] = c2
    d3 = distance1(x1,y1,x2,y2)
    return d3,d3 <= r1+r2
    

exec(input().strip())