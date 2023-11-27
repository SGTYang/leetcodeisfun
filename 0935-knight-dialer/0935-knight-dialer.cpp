class Solution {
public:
    int dp[5001][4][3] = {0}; 
    int mod = 1000000007; 
    int memo(int n, int i, int j){
        if(i<0 || j <0 || i>3 || j > 2 || (i ==3 && j == 0) || (i == 3 && j ==2)) return 0;
        if(n == 0) return 1; 
        if(dp[n][i][j] > 0) return dp[n][i][j]; 
        return dp[n][i][j] = (((((((
            memo(n-1, i+2, j-1)+ memo(n-1, i+2, j+1))%mod +memo(n-1, i-2, j-1))%mod+ 
            memo(n-1, i-2, j+1))%mod + memo(n-1, i+1, j-2))%mod+ memo(n-1, i+1, j+2))%mod+ 
            memo(n-1, i-1, j-2))%mod+  memo(n-1, i-1, j+2))%mod; 
    }
    int knightDialer(int n) {
        int res = 0; 
        for(int i=0; i<4; i++){
            for(int j =0; j<3; j++){
                res = (res+memo(n-1, i,j))%mod; 
            }
        }
        return res ;
    }
};