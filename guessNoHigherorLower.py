class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        
        while l <= r:
            mid=l+(r-l)//2
            if guess(mid) == -1:
                r=mid-1
            elif guess(mid) == 1:
                l=mid+1
            else:
                return mid
