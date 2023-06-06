#Search a 2D Matrix II - Leetcode 240 problem
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l,r=0,len(row)-1
            while l <= r:
                m=int(l+(r-l)/2)
                if row[m] == target:
                    return True
                elif row[m] > target:
                    r=m-1  
                else:
                    l=m+1
        return False
        