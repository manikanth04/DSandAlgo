#!/usr/bin/env python
import os
import sys

if __name__=='__main__':
    arry=[[2,5,7,8],[9,10,15,16],[17,18,19,20]]
    x=19
    for i in range(len(arry)):
        y=len(arry[i])/2
        if x > arry[i][y]:
            for j in range(y,len(arry[i])):
                if arry[i][j] == x:
                    print(i,j)
                    print(arry[i][j])
        elif  x == arry[i][y]:
            print(i,y)
            print arry[i][y]
            
            
                      
