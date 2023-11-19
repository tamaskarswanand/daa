def knapsack_dp(W, wt, val, n):
  
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    print_k(K,n)
    # Build table K[][] in bottom up manner
    
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    print_k(K,n)
    return K[n][W]

def print_k(K,n):
    for i in range(n+1):
        print(K[i])

val = [100, 60, 120]
wt = [10, 20, 30]
W = 10
n = len(val)
print("Maximum possible profit =", knapsack_dp(W, wt, val, n))