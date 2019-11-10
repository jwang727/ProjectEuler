import time
from functools import lru_cache

p=10**9+7
def modpinverse(x,p):
    y = pow(x, p - 2, p) #Fermat's little theorem
    return y

def pascalnthrowmodp(n,p):
    nthrow = [0] * (int((n+1)/2)+1)
    nchooser = 1
    nthrow[0]=nchooser
    for r in range(1,int((n+1)/2)+1):
        nchooser=((nchooser*(n-r+1) %p)*modpinverse(r,p) % p)
        nthrow[r]=nchooser
    return nthrow

def dicecount(n,d,m,s):
  #shifts the dice to roll between 0 and d-1 rather than 1 to d
  return dicecount3(n,d-1,m,s-m) %p

@lru_cache(maxsize=None)
def dicecount3(n,d,m,s):
    pascaln=pascalnthrowmodp(n,p)
    if s-d*m == 0:
        ans = 0
        for i in range(m,n+1): #n-i>=m dice fixed at d, the rest i dice can be anything from 1 to d-1, nCi ways to arrange the dice that rolled d
            ans += pascaln[min(i,n-i)] * pow(d, n-i, p) %p
        return ans
    elif s-d*m > 0:
        return 0
    else:
        ans = 0
    #print(d)
        for i in range(0,min(s//d+1,m)): #i dice rolled at d, cannot exceed s/d or m, whichever is smaller
            ans += pascaln[min(i,n-i)]*dicecount3(n-i,d-1,m-i,s-d*i)%p
        return ans %p

@lru_cache(maxsize=None)
def dicecount4(n,d,m,s):
    pascaln=pascalnthrowmodp(n,p)
    if (d == 0) or (m == 0) or (s == 0):
        return 0
    elif m == 1:
        if d >= s:
            return (pow(s, n, p) - pow(s - 1, n, p)) % p
        else:
            return 0
    elif d == 1:
        if m >= s:
            return 1
        else:
            return 0
    elif s == 1:
        if m == 1:
            return 1
        else:
            return 0
    else:
        ans = 0
        #print(d)
        for i in range(0,min(s//d+1,m+1)): #i dice rolled at d, cannot exceed s/d or m, whichever is smaller
            ans += pascaln[min(i,n-i)]*dicecount4(n-i,d-1,m-i,s-d*i)%p
        return ans %p

print(dicecount(5,6,3,15))
print(dicecount4(5,6,3,15))