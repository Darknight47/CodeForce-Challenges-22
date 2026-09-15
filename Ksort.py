"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1987/B ---------------------------------

You are given an array of integers a of length n.

You can apply the following operation any number of times (maybe, zero):

First, choose an integer k such that 1≤k≤n and pay k+1 coins.
Then, choose exactly k indices such that 1≤i1<i2<…<ik≤n.
Then, for each x from 1 to k, increase aix by 1.
Find the minimum number of coins needed to make a non-decreasing. That is, a1≤a2≤…≤an.

Input
Each test contains multiple test cases. The first line of input contains a single integer t (1≤t≤10^4) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1≤n≤10^5) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤10^9) — the elements of the array a.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output a single integer — the minimum number of coins needed to make a non-decreasing.

Input:
5
3
1 7 9
5
2 1 4 7 6
4
1 3 2 4
1
179
9
344 12 37 60 311 613 365 328 675

Output:
0
3
2
0
1821
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    running_max = 0
    sum_increments = 0
    max_increment = 0
    
    for num in arr:
        running_max = max(running_max, num)
        increment = running_max - num
        
        sum_increments += increment
        max_increment = max(max_increment, increment)
        
    total_cost = sum_increments + max_increment
    print(total_cost)
    print("--------------------")