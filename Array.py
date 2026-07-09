"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2209/B ----------------------------------


You are given an integer array a of length n.

For each index i, find the maximum number of indices j such that j>i and |ai−k|>|aj−k|, over all possible integer values of k.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 5000).

The second line contains n integers a1,a2,…,an (−10^9 ≤ ai ≤ 10^9).

It is guaranteed that the sum of n over all test cases does not exceed 5000.

Output
For each test case, output n integers denoting the answer.

Input:
6
1
1092
2
105 -105
5
1 2 93 84 2
7
2 9 38 4 7 1 6
10
1 9 20 9 829 3 87 1 283 7
11
9 18 29817 283 3 3928 5726 1942 1000000000 -1000000000 19

Output:
0
1 0
4 2 2 1 0
5 4 4 2 2 1 0
8 4 4 3 5 3 2 2 1 0
8 7 7 4 5 3 3 2 2 1 0
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    # Coordinate compression
    vals = sorted(set(arr))
    comp = {v: i+1 for i, v in enumerate(vals)}  # 1-indexed

    # Fenwick tree
    fenw = [0] * (n + 5)

    def update(i):
        while i <= n:
            fenw[i] += 1
            i += i & -i

    def query(i):
        s = 0
        while i > 0:
            s += fenw[i]
            i -= i & -i
        return s

    ans = [0] * n
    seen = 0

    # Process from right to left
    for i in range(n - 1, -1, -1):
        x = comp[arr[i]]
        # smaller = count of values < x
        smaller = query(x - 1)
        # greater = seen - count of values <= x
        greater = seen - query(x)
        ans[i] = max(smaller, greater)

        update(x)
        seen += 1

    print(*ans)
