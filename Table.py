"""

----------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/577/A --------------------------------------

Let's consider a table consisting of n rows and n columns. The cell located at the intersection of i-th row and j-th column contains number i × j. The rows and columns are numbered starting from 1.

You are given a positive integer x. Your task is to count the number of cells in a table that contain number x.

Input
The single line contains numbers n and x (1 ≤ n ≤ 10^5, 1 ≤ x ≤ 10^9) — the size of the table and the number that we are looking for in the table.

Output
Print a single number: the number of times x occurs in the table.

Input:
10 5

Output:
2
"""
n, m = map(int, input().split())
count = 0
i = 1

# Loop from 1 up to the square root of m
while i * i <= m:
    if m % i == 0:
        j = m // i  # Complementary factor
        
        # Check if both factors fit within the n x n table boundaries
        if i <= n and j <= n:
            if i == j:
                count += 1  # Perfect square on the main diagonal (e.g., 6*6)
            else:
                count += 2  # Two distinct positions (e.g., 2*6 and 6*2)
    i += 1
    
print(count)