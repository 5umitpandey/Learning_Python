# cook your dish here
t = int(input())

while t:
    s = str(input())
    
    c = 0, i = 0

    while(i < (len(s) - 1)):
        if(s[i] != s[i+1]):
            c += 1
            i += 2
        else:
            i += 1
    
    print(c)
    
    t -= 1
