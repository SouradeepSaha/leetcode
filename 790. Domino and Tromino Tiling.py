class Solution:
    def numTilings(self, n: int) -> int:
        
        # row = 0 -> only top row occupied
        # row = 1 -> only bottom row occupied
        # row = 2 -> both top and bottom rows occupied
        dp = {(0,2): 1, (1,1): 1, (1, 0): 1, (1,2): 2}
        
        def tile(col, row) -> int:
            if col < 0:
                dp[(col, row)] = 0
            
            elif (col, row) not in dp:
                dp[(col, row)] = 0
                if row == 0:
                    dp[(col,row)] += tile(col-2, 2) + tile(col-1,0)
                elif row == 1:
                    dp[(col,row)] += dp[(col-2,2)] + tile(col-1,1)
                else:
                    dp[(col,row)] += tile(col-1,2) + tile(col-2,2) + tile(col-1,0) + tile(col-1,1)
                
            #print(col, row)
            dp[(col,row)] %= (10**9 + 7)
            return dp[(col,row)]

        tile(n-1, 2)
        return dp[(n-1,2)]
