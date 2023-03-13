class Complex :
    def __init__(self,a,b) :
        self.R = a
        self.Im = b

    def __str__(self) :
        m = ''
        if self.R > 0 or self.R < 0 :
            m += str(self.R)
        else : pass

        if self.Im == 1 :
            if self.R != 0 :
                m += '+i'
            else : m += 'i'
            
        elif self.Im == -1 :
            m += '-i'
        elif self.Im == 0 :
            pass
        elif self.Im > 0 :
            if self.R != 0 :
                m += '+' + str(self.Im) + 'i'
            else : m += str(self.Im) + 'i'
        else :
            m += str(self.Im) + 'i'

        if m == '' :
            return '0'
        else : 
            return m
        

    def __add__(self,rhs) :
        add_R = self.R + rhs.R
        add_Im = self.Im + rhs.Im
        return Complex(add_R,add_Im)

    def __mul__(self,rhs) :
        mul_R = (self.R*rhs.R - self.Im*rhs.Im)
        mul_Im = (self.R*rhs.Im + self.Im*rhs.R)
        return Complex(mul_R,mul_Im)

    def __truediv__(self,rhs) :
        div_R = (self.R*rhs.R + self.Im*rhs.Im)/(rhs.R**2 + rhs.Im**2)
        div_Im = (self.Im*rhs.R - self.R*rhs.Im)/(rhs.R**2 + rhs.Im**2)
        return Complex(div_R,div_Im)

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)
