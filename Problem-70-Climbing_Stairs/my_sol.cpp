class Solution {
public:
    int climbStairs(int n) {
        
        vector<int> dp(n+1, 0);
        
        //As 1 stair do have 1 way so we start fibo series with 1 1 2, instead of 0 1 1 2

        dp[0] = 1;
        dp[1] = 1;

        for(int i = 2; i <= n; i++)
        {
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n];
    }
};


//time complexity O(n)
//Space complexity O(n)