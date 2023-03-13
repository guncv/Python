class Card :
    def __init__(self,value,suit) :
        self.value = value
        self.suit = suit

    def __str__(self) : 
        return '(' + self.value + ' ' + self.suit + ')'

    def next1(self):
        sui = ['club','diamond','heart','spade']
        val = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','3']

        if self.suit != 'spade' :
            m = sui.index(self.suit)
            return Card(self.value,sui[m+1])

        else :
            n = val.index(self.value)
            return Card(val[n+1],'club')

    def next2(self):
        val = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','3']
        sui = ['club','diamond','heart','spade']

        if self.suit != 'spade' :
            m = sui.index(self.suit)
            self.suit = sui[m+1]
        
        else :
            n = val.index(self.value)
            self.suit = 'club'
            self.value = val[n+1]

n = int(input())
cards = []
for i in range(n):
    value,suit = input().split()
    cards.append(Card(value,suit))\

for i in range(n):
    print(cards[i].next1())
print('----------')

for i in range(n):
    print(cards[i])
print('----------')

for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])