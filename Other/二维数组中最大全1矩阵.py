# *-* coding=utf8 *-*
def MaxMatrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    M = len(matrix)
    N = len(matrix[0])
    dp = [[0]*100 for i in range(100)]
   # print(dp)
    for i in range(0, M, 1):
        if matrix[i][0] == 1:
            dp[i][0] = 1
            res = 1
    for j in range(0, N, 1):
        if matrix[0][j] == 1:
            dp[0][j] = 1
            res = 1
    for i in range(1, M):
        for j in range(1, N):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1
            res = max(res, dp[i][j])
    return res

print(MaxMatrix([[1,0,1,0,0], [1,0,1,1,1], [1,1,1,1,1], [1,0,0,1,0]]))


