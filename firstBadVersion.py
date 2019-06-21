class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        
        while l <= r:
            mid=l+(r-l)//2
            if isBadVersion(mid) is False:
                l=mid+1
            elif isBadVersion(mid) is True:
                r=mid-1
            else:
                return l
        return l
