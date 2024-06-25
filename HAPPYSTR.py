t = int(input())

while t > 0:
    s = input()
    
    i=0
    count = 0
    breakk = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if(count >= 3 ):
            breakk = 1
            break
        else:
            if( s[i] in vowel ):
                count += 1
            else:
                count = 0
    
    if( breakk == 1 ):
        print("HAPPY")
    else:
        print("SAD")
    
    t -= 1
