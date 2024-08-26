#longest common subsequence

# Function to find the length of the Longest Common Subsequence (LCS)
def lcs(S1, S2, m, n, memo):
    # Base case: if either string is empty, the LCS is 0
    if m == 0 or n == 0:
        return 0
        
    # If the value is already computed, return it to avoid recomputation
    if memo[m][n] != -1:
        return memo[m][n]
        
    # If the last characters of both strings match
    if S1[m - 1] == S2[n - 1]:
        # Store the result in the memoization table and return
        memo[m][n] = 1 + lcs(S1, S2, m-1, n-1, memo)
        return memo[m][n]
        
    # If the last characters do not match, consider both possibilities:
    # 1. Exclude the last character of S1 and find LCS
    # 2. Exclude the last character of S2 and find LCS
    # Take the maximum of these two possibilities
    memo[m][n] = max(lcs(S1, S2, m, n-1, memo),
                     lcs(S1, S2, m-1, n, memo))
    return memo[m][n]

# Driver code to test the function
if __name__ == "__main__":
    # Strings for which LCS is to be calculated
    S1 = "ABCBDAB"
    S2 = "BDCABA"
    
    # Length of the strings
    m = len(S1)
    n = len(S2)
    
    # Initialize memoization table with -1 (indicating uncomputed values)
    memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    
    # Print the length of the LCS
    print("Length of LCS is", lcs(S1, S2, m, n, memo))

    
    
    
'''
The memo in the code refers to a "memoization table" used to store results
of subproblems that have already been computed. 
This helps avoid redundant calculations, making the algorithm more efficient.

Memoization Table (memo)
What is it? The memo is a 2D list (or matrix) where each element memo[i][j] stores the
result of the LCS for the substrings S1[0...i-1] and S2[0...j-1].

If memo[i][j] is -1, it means that the result for this subproblem hasn't been computed yet.
If memo[i][j] contains a number, that number represents the length of the LCS for the corresponding substrings.

Why use it? Without memoization, the same subproblems would be solved multiple times,
leading to a high computational cost, especially as the input size grows.
Memoization ensures that each subproblem is solved only once,
and the result is reused whenever needed.'''