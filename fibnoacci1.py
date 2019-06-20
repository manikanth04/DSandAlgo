#!/usr/bin/python
import os
def fibonacciser(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacciser(n-1)+fibonacciser(n-2)
def fibonacciser1(n):
    
    if n in fibonacciser_cache:
        return fibonacciser_cache[n]
    #if n==0:
    #    value=1
    if n==1:
        value=1
    if n==2:
        value=1
    if n >2:
        value=fibonacciser1(n-1)+fibonacciser1(n-2)

    fibonacciser_cache[n]=value
    return Value

        
def fibonacciser2(n):
    fibonacciser_cache[0]=1
    fibonacciser_cache[1]=1
    fibonacciser_cache[2]=1
    for i in range(3,n+1):
        fibonacciser_cache[i]=fibonacciser_cache[i-1]+fibonacciser_cache[i-2]
    return fibonacciser_cache[n]
def fibonacciser3(n):
    prev1=1
    prev2=1
    current=0
    for i in range (3,n+1):
        current=prev1+prev2
        prev2=prev1
        prev1=current
    return current
if __name__=='__main__':
    print("ManiKanth")
    n=100
    fibonacciser_cache={}
    for n in range (1,101):
        print(n,fibonacciser3(n))
