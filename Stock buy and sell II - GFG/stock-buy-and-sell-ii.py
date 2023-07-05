
from typing import List


class Solution:
    
    def buy(self, n : int, prices : List[int], p : int):
        if p+1 < n and prices[p] < prices[p+1]:
            return True
        else:
            return False
        
        
    def sell(self, n : int, prices : List[int], p : int):
        # curr_price = prices[p]
        # p += 1
        # sell = False
        # while(p<n):
        #     if curr_price < prices[p]:
        #         buy = True
        #         break
        # return buy
        if p+1 < n and prices[p] > prices[p+1]:
            return True
        elif p+1 == n:
            return True
        else:
            return False
        
    
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        # code here
        buy = True
        sell = False
        buy_price = None
        sell_price = None
        profit = 0
        i = 0
        p = 0
        while(i<n):
            p = i
            if buy and self.buy(n, prices, p):
                # print("buying at: ",prices[p])
                buy = False
                sell = True
                buy_price = prices[p]
                i += 1
                continue
            if sell and self.sell(n, prices, p):
                # print("selling at: ",prices[p])
                sell = False
                buy = True
                sell_price = prices[p]
                profit += sell_price - buy_price
                # print("profit: ",profit )
                i += 1
                continue
            i += 1
        return profit
                
                
                
            



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        prices=IntArray().Input(n)
        
        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)
        
        print(res)
        

# } Driver Code Ends