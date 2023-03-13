class Point :
    def __init__(self,x,y) :
        self.x = x
        self.y = y

    def __str__(self) :
        return '(' + str(self.x) + ',' + str(self.y) + ')'

class Rect:
    def __init__(self,p1,p2):
        self.lowerleft = p1
        self.upperright = p2

    def area(self) :
        W = self.upperright.x - self.lowerleft.x
        H = self.upperright.y - self.lowerleft.y
        return W*H

    def contains(self,p): 
        if p.x <= self.upperright.x and p.x >= self.lowerleft.x :
            if p.y <= self.upperright.y and p.y >= self.lowerleft.y :
                return True
            return False
        return False

x1,y1,x2,y2 = [int(e) for e in input().split()]
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
 x,y = [int(e) for e in input().split()]
 p = Point(x,y)
 print(rect.contains(p)) 