"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2035/B  ----------------------------------------

Given a positive integer n. Find the smallest integer whose decimal representation has length n and consists only of 3
s and 6
s such that it is divisible by both 33 and 66. If no such integer exists, print −1.

Input
The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases.

The only line of each test case contains a single integer n (1 ≤ n ≤ 500) — the length of the decimal representation.

Output
For each test case, output the smallest required integer if such an integer exists and −1 otherwise.

Input:
6
1
2
3
4
5
7

Output:
-1
66
-1
3366
36366
3336366
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n == 1 or n == 3):
        print(-1)
        continue
    if(n % 2 == 0):
        ans = '3'*(n - 2) + '66'
    else:
        ans = '3'*(n - 5) + '36366'
    print(ans)