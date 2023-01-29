#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp = [[0  for _ in range(W+1) ] for _ in range(len(val)+1)]
        
        for index in range(len(val)-1,-1,-1):
            for weight in range(0,W+1):
                y = val[index] + dp[index+1][weight+wt[index]] if wt[index] + weight <= W else 0
                dp[index][weight] = max(dp[index+1][weight], y)
        return dp[0][0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends