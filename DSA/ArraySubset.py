def isSubset( a1, a2, n, m):
    freq = {}
    
    for i in range(n):
        if a1[i] in freq:
            freq[a1[i]] += 1
        else:
            freq[a1[i]] = 1
    
    # Check if all elements of the second array are present in the dictionary
    for i in range(m):
        if a2[i] in freq and freq[a2[i]] > 0:
            freq[a2[i]] -= 1
        else:
            return "No"
    
    return "Yes"
