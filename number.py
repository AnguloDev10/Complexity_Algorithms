
ara={}
#def cast():
    #for x in range()
def pivot(n):
    ara[2]=['a','b','c']
    ara[3]=['d','e','f']
    ara[4]=['g','h','i']
    ara[5]=['d','e','f']
    ara[6]=['d','e','f']
    ara[7]=['d','e','f']
    ara[8]=['d','e','f']
    ara[9]=['d','e','f']
    comb=[]
    if(n==0):
        return []
    if(n==1):
        c= int(digits[0])
        for x in range(len(ara[c])):
            comb.append(ara[c][x])
    if(n==2):
       c= int(digits[0])
       b= int(digits[1])
       for x in range(len(ara[c])):
         for y in range(len(ara[c])):
            if c != b or c==b :
                comb.append((ara[c][x],ara[b][y]))
    if(n==3):
       c= int(digits[0])
       b= int(digits[1])
       d= int(digits[2])
       for x in range(len(ara[c])):
         for y in range(len(ara[c])):
            for z in range(len(ara[c])):
                comb.append((ara[c][x],ara[b][y],ara[d][z]))
    return comb
            

#def valid():
    
#    #if len(digits) < 0:
    #    return []
#    for c in range(len(a)):
#        for b in range(len(a)):
#            if c != b or c==b :
#                comnbs.append((a[c],x[b]))
    
#    return comnbs
digits=input()
n= len(digits)
#print(len(digits))
print(pivot(n))