"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2246/B ---------------------------------

You are given a single integer n. Construct an array of n distinct positive integers a1,…,an such that for all i(1≤i≤n), a1+a2+a3+…+an is divisible by ai, or determine that no such array exists.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 50). The description of the test cases follows.

The first and only line of each test case contains a single integer n(1≤n≤50).

Output
For each test case, if there is no solution, output a single integer −1.

Otherwise, output n integers a1,…,an(1 ≤ ai ≤ 10^17) — an array satisfying the conditions.

If there are multiple solutions, print any of them.

Input:
3
1
4
5

Output:
1
1 9 2 6
12 3 10 20 15
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n == 1):
        print(1)
    elif(n == 2):
        print(-1)
    elif(n == 3):
        print(1, 2, 3)
    else:
        arr = [1, 9, 2, 6]
        temp_sum = sum(arr)
        while len(arr) < n:
            arr.append(temp_sum)
            temp_sum += temp_sum
        print(*arr)