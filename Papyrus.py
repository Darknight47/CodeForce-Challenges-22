"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2238/A ------------------------------

Papyrus came up with another puzzle for Frisk to solve. 
Papyrus brought two arrays a and b of length n and allowed the following two operations to be performed:

choose any index i (1 ≤ i ≤ n) and change ai to ai−1. 
The execution time of such an operation is 1 second.
reorder all elements of array a in any way. The execution time of such an operation is c seconds.
You need to convert array a into array b.

Frisk wants to solve the puzzle as soon as possible. Help Frisk determine the minimum time needed to solve the puzzle. 
If there is no solution, output −1.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains two integers n and c (1 ≤ n, c ≤ 100) — the length of arrays a and b and the cost of the second operation.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 100) — the elements of the first array.

The third line of each test case contains n integers b1,b2,…,bn (1 ≤ bi ≤ 100) — the elements of the second array.

Output
For each test case, output a single integer representing the minimum number of seconds required to solve the puzzle, or −1 if it is impossible to solve the puzzle.

Input:
6
3 5
5 2 3
2 3 4
3 3
1 2 3
4 5 6
4 4
4 5 2 3
3 5 1 2
6 4
2 4 5 3 6 8
5 8 3 1 2 5
5 11
5 8 11 14 17
16 12 10 10 6
3 5
20 14 20
12 18 17

Output:
6
-1
3
8
-1
12
"""
cases = int(input())
for _ in range(cases):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    arr_sorted = sorted(arr)
    brr_sorted = sorted(brr)
    ans1 = c
    ans2 = 0
    ok = True
    for i in range(n - 1, -1, -1):
        first = arr_sorted[i]
        second = brr_sorted[i]
        if(first < second):
            ok = False
            break
        ans1 += (first - second)
    if(ok):
        re = False
        for i in range(n):
            if(arr[i] < brr[i]):
                # re-order needed.
                re = True
                break
            ans2 += arr[i] - brr[i]
        if(re):
            print(ans1)
        else:
            print(min(ans1, ans2))
    else:
        print(-1)