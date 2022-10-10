class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            ## for odd length
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resLen< (r-l+1):
                    res = s[l:r+1]
                    resLen=len(res)
                l-=1
                r+=1
            
            ## for even length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resLen< (r-l+1):
                    res = s[l:r+1]
                    resLen=len(res)
                l-=1
                r+=1
        return res
        
        
        
        
        
                
                
            
            
        
            
        