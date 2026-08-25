"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2124/B ------------------------------------

This problem differs from problem G. In this problem, you must output the minimum sum of prefix minimums after at most one operation.

You are given an array a of length n, with elements satisfying 0≤ai≤n. You can perform the following operation at most once:

Choose two indices i and j such that i<j. Set ai:=ai+aj. Then, set aj=0.
Output the minimum possible value of min(a1)+min(a1,a2)+…+min(a1,a2,…,an) that you can get.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains an integer n (2 ≤ n ≤ 2⋅10^5) — the length of a.

The following line contains n space-separated integers a1,a2,…,an (0≤ai≤n) — denoting the array a.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output an integer on a new line, the minimum possible value of min(a1)+min(a1,a2)+…+min(a1,a2,…,an).

Input:
3
2
1 2
3
1 2 3
4
3 0 2 3

Output:
2
2
3
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = min(arr[0], arr[1]) + arr[0]
    print(ans)