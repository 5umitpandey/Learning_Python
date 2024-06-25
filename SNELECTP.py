# cook your dish here
t = int(input())

while t:
    s = str(input())
    
    n = len(s)
    killed = [False] * n
    
    #print(killed)
    for i in range(n):
        if s[i] == 'm':
            if i - 1 >= 0 and s[i - 1] == 's' and not killed[i - 1]:
                killed[i - 1] = True
                continue
            if i + 1 < n and s[i + 1] == 's':
                killed[i + 1] = True
       
    snakes = 0
    mongooses = 0

    for i in range(n):
        if s[i] == 's' and not killed[i]:
            snakes += 1
        if s[i] == 'm':
            mongooses += 1
     
    print(killed)
    # if(mongooses > snakes):
    #     print("mongooses")
    # elif(mongooses < snakes):
    #     print("snakes")
    # else:
    #     print("tie")
    
    t -= 1
