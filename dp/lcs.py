def longestCommonSubsequence(A, B):
    # Get the lengths of the two sequences
    m = len(A)
    n = len(B)
    
    # Initialize a 2D DP table with all values set to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table using the recurrence relation with logging
    print("Filling the DP table:")
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:  # Characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
                print(f"dp[{i}][{j}] (match): A[{i-1}] = '{A[i-1]}', B[{j-1}] = '{B[j-1]}', dp[{i-1}][{j-1}] + 1 = {dp[i][j]}")
            else:  # Characters don't match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                print(f"dp[{i}][{j}] (no match): A[{i-1}] = '{A[i-1]}', B[{j-1}] = '{B[j-1]}', max(dp[{i-1}][{j}], dp[{i}][{j-1}]) = {dp[i][j]}")
    
    # The value in dp[m][n] is the length of the LCS
    lcs_length = dp[m][n]
    print("\nCompleted filling DP table:")
    print(f"dp[{m}][{n}] = {lcs_length} (Length of LCS)")
    
    # Backtrack to find the LCS string (optional)
    lcs = []
    i, j = m, n
    print("\nBacktracking to construct the LCS:")
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            lcs.append(A[i - 1])
            print(f"Match: A[{i-1}] = B[{j-1}] = '{A[i-1]}', add to LCS")
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            print(f"Move up: dp[{i-1}][{j}] >= dp[{i}][{j-1}], moving to dp[{i-1}][{j}]")
            i -= 1
        else:
            print(f"Move left: dp[{i}][{j-1}] > dp[{i-1}][{j}], moving to dp[{i}][{j-1}]")
            j -= 1
    
    # Reverse the LCS since we built it backwards
    lcs.reverse()

    # Return both the length and the actual LCS string
    return lcs_length, ''.join(lcs)

# Example usage
A = "ABCBDAB"
B = "BDCABB"

lcs_length, lcs_string = longestCommonSubsequence(A, B)
print(f"\nLength of LCS: {lcs_length}")
print(f"LCS: {lcs_string}")
