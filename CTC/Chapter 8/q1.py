def no_ways(n):
    res = [0]*(n+1)
    res[1] = 1
    res[0] = 1
    for i in range(2,n+1):
        res[i]+=res[i-1]
        if (i-2) >=0 :
            res[i]+=res[i-2]
        if (i-3) >=0:
            res[i] += res[i-3]
    return res[n]