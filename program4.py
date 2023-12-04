def findpairs(pairs):
    s=set()
    for (x,y) in pairs:
        s.add((x,y))
        if(y,x)in s:
            print((x,y)," ",(y,x))
pairs = [(3,4),(1,2),(5,99),(100,7),(7,100),(4,3),(99,5)]
findpairs(pairs)







