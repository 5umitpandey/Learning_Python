t = int(input())

while t > 0:
    x = input()
    y = input()
    
    flag = 1
    for i in range(len(x)):
        if x[i]!='?' and y[i]!='?' and x[i]!=y[i]:
            flag = 0
            break
    if flag:
        print("Yes")
    else:
        print("No")
    # Your code goes here
    t -= 1
