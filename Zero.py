"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2247/A -------------------------------------

You are given an array a of length n, consisting only of −1 and 1.

You may perform the following operation on a any number of times:

Choose an index i satisfying 1≤i≤n−1.
Assign ai=−ai and ai+1=−ai+1.
Determine whether it is possible to make the sum of elements of a equal to 0.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 200). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of array a.

The second line of each test case contains n integers a1,a2,…,an (ai∈{−1,1}) — the array a.

Output
For each test case, print "YES" if it is possible to make the sum of elements of a equal to 0, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
5
1
-1
2
1 -1
2
1 1
5
1 -1 1 -1 1
6
-1 1 -1 -1 -1 -1

Output:
NO
YES
NO
NO
YES
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    if(n % 2 == 1):
        print("NO")
    else:
        temp_sum = abs(sum(arr))
        if(temp_sum % 4 == 0):
            print("YES")
        else:
            print("NO")