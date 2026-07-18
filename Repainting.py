"""

----------------------------------------------- Link for the challenge: https://codeforces.com/contest/1415/problem/B ------------------------------------------

There is a street with n houses in a line, numbered from 1 to n. The house i is initially painted in color ci. 

The street is considered beautiful if all houses are painted in the same color. 
Tom, the painter, is in charge of making the street beautiful. Tom's painting capacity is defined by an integer, let's call it k.

On one day, Tom can do the following repainting process that consists of two steps:

He chooses two integers l and r such that 1≤l≤r≤n and r−l+1=k.
For each house i such that l ≤ i ≤ r, he can either repaint it with any color he wants, or ignore it and let it keep its current color.
Note that in the same day Tom can use different colors to repaint different houses.

Tom wants to know the minimum number of days needed to repaint the street so that it becomes beautiful.

Input
The first line of input contains a single integer t (1 ≤ t ≤ 10^4), the number of test cases. Description of test cases follows.

In the first line of a test case description there are two integers n and k (1 ≤ k ≤ n ≤ 10^5).

The second line contains n space-separated integers. The i-th of these integers represents ci (1 ≤ ci ≤ 100), the color which house i is initially painted in.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
Print t lines, each with one integer: the minimum number of days Tom needs to make the street beautiful for each test case.

Input:
3
10 2
1 1 2 2 1 1 2 2 2 1
7 1
1 2 3 4 5 6 7
10 3
1 3 3 3 3 1 2 1 3 3

Output:
3
6
2
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    values = set(arr)

    best_windows = float('inf')
    for v in values:
        windows = 0
        i = 0
        while i < n:
            if arr[i] == v:
                i += 1
            else:
                windows += 1
                i += k  # this window fixes up to K positions
        if windows < best_windows:
            best_windows = windows
    print(best_windows)