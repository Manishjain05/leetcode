class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s)==0:
            return 0
        else:
            max = 1
        p1=p2=0
        cnt = 1
        while(p2<len(s)-1):
            p2=p2+1
            if s[p2] not in s[p1:p2]:
                
                print(s[p1:p2+1])
                print(len(s[p1:p2+1]))
                
            elif s[p2]  in s[p1:p2]:
                print("elif")
                if max<len(s[p1:p2]):
                    max = len(s[p1:p2])
                    # print("max: "+str(max))
                # print(p1)
                # print(p2)
                p1 = p1+ s[p1:p2].find(s[p2])+1
                # print(p1)
                # print(p2)
                # print(s[p1:p2+1])
        if max<len(s[p1:p2])+1:
                    max = len(s[p1:p2])+1
        return max
        

        
                
        
                
        
        