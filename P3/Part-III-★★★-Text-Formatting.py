l = []
# with open('C:/Users/User/OneDrive/เดสก์ท็อป/CODE/Python/P3/data1.txt','r') as f :
#     m = ''
#     for i in f.readline() :
#         m += i

x = input()
k = int(input())
ruler = ''
for i in range(k//10) :
    ruler += '-'*9 + str(i+1)
if k%10 != 0 :
    ruler += '-'*(k%10)
print(ruler)

ope = True
n = 0
# while ope :
    



