def uniquePaths(m, n):
    # Memoization cache (store the results of subproblems)
    memo = {}

    # To store logs for decision steps
    decision_logs = []

    # Recursive function with memoization
    def dp(i, j):
        # Base cases: If we're at the top row or left column, there's only 1 way to reach the cell
        if i == 0 or j == 0:
            decision_logs.append(f"Cell ({i}, {j}): Base case, only 1 way to reach")
            return 1
        
        # Check if the result for dp(i, j) is already computed
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Calculate dp(i, j) recursively using the recurrence relation
        from_above = dp(i - 1, j)  # Coming from the cell above
        from_left = dp(i, j - 1)  # Coming from the cell to the left

        # Total unique paths to reach cell (i, j) is the sum of the paths from the above and left cells
        memo[(i, j)] = from_above + from_left

        # Log the decision at this step
        decision_logs.append(f"Cell ({i}, {j}): From above ({i-1}, {j}) + from left ({i}, {j-1}), total paths = {memo[(i, j)]}")

        return memo[(i, j)]

    # Start the recursion from the bottom-right cell (m-1, n-1)
    result = dp(m - 1, n - 1)

    # Output the logs for the decisions
    for log in decision_logs:
        print(log)

    return result

# Example usage
m, n = 3, 7
result = uniquePaths(m, n)
print(f"Number of unique paths: {result}")
