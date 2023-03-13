win = set()
loss = set()
for i in range(int(input())) :
    x = input().split()
    win.add(x[0])
    loss.add(x[1])
print(sorted(win-loss))