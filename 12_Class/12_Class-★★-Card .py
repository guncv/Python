class Card :
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def getScore(self):
        l = ['Q','J','K']
        if self.value == 'A':
            return 1
        elif self.value in l :
            return 10
        else : 
            return int(self.value)
        
    def sum(self,other):
        return (self.getScore() + other.getScore())%10
    
    def __lt__(self, rhs):
        val = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        sui = ['club','diamond','heart','spade']
        if self.value != rhs.value :
            return val.index(self.value) < val.index(rhs.value)
        return sui.index(self.suit) < sui.index(rhs.suit)

        
n = int(input())
cards = []
for i in range(n) :
    value,suit = input().split()
    cards.append(Card(value,suit))
for i in range(n) :
    print(cards[i].getScore())
print('----------')
for i in range(n-1) :
    print(cards[i].sum(cards[i+1]))
print('----------')
cards.sort()
for i in range(n):
    print(cards[i])