"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1998/B -----------------------------------

You are given a permutation∗ p of length n.

Find a permutation q of length n that minimizes the number of pairs (i,j) (1≤i≤j≤n) such that pi+pi+1+…+pj=qi+qi+1+…+qj.

∗ A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
The first line contains t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains n (1 ≤ n ≤ 2⋅10^5).

The following line contains n space-separated integers p1,p2,…,pn (1 ≤ pi ≤ n) — denoting the permutation p of length n.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output one line containing any permutation of length n (the permutation q) such that q minimizes the number of pairs.

Input:
3
2
1 2
5
1 2 3 4 5
7
4 7 5 1 2 6 3

Output:
2 1
3 5 4 2 1
6 2 1 4 7 3 5
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    # shifting 1 to left
    last = arr[0]
    #print(last, end=' ')
    for i in range(1, n):
        #arr[i] = arr[i - 1]
        print(arr[i], end=' ')
    #arr[0] = last
    print(last)