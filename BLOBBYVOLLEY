t = int(input())

while t > 0:
    n = int(input())
    s = input()
    
    server = 0
    A = 0
    B = 0
    i=0
    for i in range(len(s)):
        if server == 0 and s[i] == "A":
            #print("i=",i,"server=",server, ",s[i]",s[i], ",A",A, "B",B)
            A += 1
        if server == 1 and s[i] == "A":
            #print("i=",i,"server=",server, ",s[i]",s[i], ",A",A, ",B",B)
            server = 0    
        if server == 1 and s[i] == "B":
            #print("i=",i,"server=",server, ",s[i]",s[i], ",A",A, ",B",B)
            B += 1
        if server == 0 and s[i] == "B":
            #print("i=",i,"server=",server, ",s[i]",s[i], ",A",A, ",B",B)
            server = 1
    print(A,B)
            
    t -= 1
