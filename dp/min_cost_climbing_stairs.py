def minCostClimbingStairs(cost):
    # Memoization cache (store the results of subproblems)
    memo = {}
    
    # To store logs for decision steps
    decision_logs = []

    # Recursive function with memoization
    def dp(i):
        # Base cases
        if i == 0: 
            return cost[0]
        if i == 1:
            return cost[1]
        
        # Check if the result for dp[i] is already computed
        if i in memo:
            return memo[i]
        
        # Calculate dp[i] recursively using the recurrence relation
        option1 = dp(i - 1)  # Coming from the previous step
        option2 = dp(i - 2)  # Coming from two steps below

        # Choose the minimum of the two options
        if option1 < option2:
            decision_logs.append(f"Step {i}: Took the previous step (from {i-1}), cost = {cost[i]} + {option1}")
            memo[i] = cost[i] + option1
        else:
            decision_logs.append(f"Step {i}: Took two steps back (from {i-2}), cost = {cost[i]} + {option2}")
            memo[i] = cost[i] + option2
        
        return memo[i]

    # Final result: minimum cost to reach the top is the minimum of dp[n-1] and dp[n-2]
    n = len(cost)
    min_cost = min(dp(n - 1), dp(n - 2))

    # Output the logs for the decisions
    for log in decision_logs:
        print(log)

    return min_cost

# Example usage
cost = [7,9,30,15,42,72]
result = minCostClimbingStairs(cost)
print(f"Minimum cost to reach the top: {result}")
