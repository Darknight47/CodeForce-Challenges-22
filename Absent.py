"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1613/B ---------------------------------

You are given a sequence a1,a2,…,an consisting of n pairwise distinct positive integers.

Find ⌊n2⌋ different pairs of integers x and y such that:

x≠y;
x and y appear in a;
x mod y doesn't appear in a.
Note that some x or y can belong to multiple pairs.

⌊x⌋ denotes the floor function — the largest integer less than or equal to x. x mod y denotes the remainder from dividing x by y.

If there are multiple solutions, print any of them. It can be shown that at least one solution always exists.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The first line of each testcase contains a single integer n (2 ≤ n ≤ 2⋅10^5) — the length of the sequence.

The second line of each testcase contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^6).

All numbers in the sequence are pairwise distinct. The sum of n over all testcases doesn't exceed 2⋅10^5.

Output
The answer for each testcase should contain ⌊n2⌋ different pairs of integers x and y such that x≠y, x and y appear in a and x mod y doesn't appear in a. 
Print the pairs one after another.

You can print the pairs in any order. However, the order of numbers in the pair should be exactly such that the first number is x and the second number is y. 
All pairs should be pairwise distinct.

If there are multiple solutions, print any of them.

Input:
4
2
1 4
4
2 8 3 4
5
3 8 5 9 7
6
2 7 5 3 4 8

Output:
4 1
8 2
8 4
9 5
7 5
8 7
4 3
5 2
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    temp_min = min(arr)
    pairs = n // 2
    for i in range(n):
        if(pairs <= 0):
            break
        if(arr[i] != temp_min):
            print(arr[i], temp_min)
            pairs -= 1
    print("-------------------")