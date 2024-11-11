def knapsack_dp(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
                
    return dp[n][capacity]

# Example usage
weights = [1, 2, 3, 8, 7, 4]
values = [20, 5, 10, 40, 15, 25]
capacity = 10
print("Maximum value (DP):", knapsack_dp(weights, values, capacity))
