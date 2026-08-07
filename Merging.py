"""


---------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1831/B -------------------------------------

You are given two arrays a and b both of length n.

You will merge† these arrays forming another array c of length 2⋅n. 
You have to find the maximum length of a subarray consisting of equal values across all arrays c that could be obtained.

† A merge of two arrays results in an array c composed by successively taking the first element of either array (as long as that array is nonempty) and removing it. 
After this step, the element is appended to the back of c. 
We repeat this operation as long as we can (i.e. at least one array is nonempty).

Input
Each test contains multiple test cases. The first line of input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer n (1≤n≤2⋅10^5) — the length of the array a and b.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤2⋅n) — the elements of array a.

The third line of each test case contains n integers b1,b2,…,bn (1≤bi≤2⋅n) — the elements of array b.

It is guaranteed that the sum of n across all test cases does not exceed 2⋅10^5.

Output
For each test case, output the maximum length of a subarray consisting of equal values across all merges.

Input:
4
1
2
2
3
1 2 3
4 5 6
2
1 2
2 1
5
1 2 2 2 2
2 1 1 1 1

Output:
2
1
2
5
"""
from collections import defaultdict
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    best_a = defaultdict(int)
    best_b = defaultdict(int)

    # longest runs in a
    i = 0
    while i < n:
        v = arr[i]
        j = i
        while j < n and arr[j] == v:
            j += 1
        best_a[v] = max(best_a[v], j - i)
        i = j

    # longest runs in b
    i = 0
    while i < n:
        v = brr[i]
        j = i
        while j < n and brr[j] == v:
            j += 1
        best_b[v] = max(best_b[v], j - i)
        i = j

    ans = 0
    for v in set(arr) | set(brr):
        ans = max(ans, best_a[v] + best_b[v])

    print(ans)