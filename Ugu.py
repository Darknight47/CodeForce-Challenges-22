"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1732/B ------------------------------------------

A binary string is a string consisting only of the characters 0 and 1. You are given a binary string s1s2…sn. 
It is necessary to make this string non-decreasing in the least number of operations. In other words, each character should be not less than the previous. In one operation, you can do the following:

Select an arbitrary index 1≤i≤n in the string;
For all j≥i, change the value in the j-th position to the opposite, that is, if sj=1, then make sj=0, and vice versa.
What is the minimum number of operations needed to make the string non-decreasing?

Input
Each test consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of test cases follows.

The first line of each test cases a single integer n (1 ≤ n ≤ 10^5) — the length of the string.

The second line of each test case contains a binary string s of length n.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single integer — the minimum number of operations that are needed to make the string non-decreasing.

Input:
8
1
1
2
10
3
101
4
1100
5
11001
6
100010
10
0000110000
7
0101010

Output:
0
1
2
1
2
3
1
5
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()

    flipped = False
    ops = 0

    for i in range(n - 1):
        cur = s[i]
        nxt = s[i + 1]

        # Apply virtual flip
        if flipped:
            cur = '1' if cur == '0' else '0'
            nxt = '1' if nxt == '0' else '0'

        # If we see a decreasing pair, we must flip
        if cur == '1' and nxt == '0':
            ops += 1
            flipped = not flipped

    print(ops)