class piggybank :
    def __init__(self) :
        self.coins = {}

    def add(self,v,n) :
        if v not in self.coins :
            self.coins[float(v)] = int(n)
        else :
            if self.coins[float(v)] + int(n) > 100 :
                return False
            self.coins[float(v)] += int(n)
        return True
    
    def __float__(self) :
        total = 0
        for i in self.coins :
            total += i*self.coins[i]
        return float(total)
    
    def __str__(self) :
        s = '{'
        l = []
        for i in self.coins :
            l.append(i)
        for i in sorted(l) :
            s += str(i) + ':' + str(self.coins[i])
            if sorted(l).index(i) != len(l)-1 :
             s += ',  '
        s += '}'
        return s
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
