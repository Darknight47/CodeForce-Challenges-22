"""


-------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1941/B --------------------------------

Rudolf has an array a of n integers, the elements are numbered from 1 to n.

In one operation, he can choose an index i (2≤i≤n−1) and assign:

ai−1=ai−1−1
ai=ai−2
ai+1=ai+1−1

Rudolf can apply this operation any number of times. Any index i can be used zero or more times.

Can he make all the elements of the array equal to zero using this operation?

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases in the test.

The first line of each case contains a single integer n (3 ≤ n ≤ 2⋅10^5) — the number of elements in the array.

The second line of each case contains n integers a1,a2,…,an (0 ≤ aj ≤ 10^9) — the elements of the array.

It is guaranteed that the sum of the values of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output "YES" if it is possible to make all the elements of the array zero using the described operations. Otherwise, output "NO".

You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

Input:
7
5
1 3 5 5 2
5
2 4 4 5 1
5
0 1 3 3 1
6
5 6 0 2 3 0
4
1 2 7 2
3
7 1 0
4
1 1 1 1

Output:
YES
NO
YES
NO
NO
NO
NO
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    a = list(map(int, input().split()))
    ok = True
    for i in range(n - 2):
        need = a[i]  # number of operations needed

        if need < 0:
            ok =  False
            break

        if a[i+1] < 2 * need or a[i+2] < need:
            ok =  False
            break

        a[i] -= need
        a[i+1] -= 2 * need
        a[i+2] -= need

    if(not ok):
        print("NO")
    else:
        print("YES" if a[-1] == 0 and a[-2] == 0 else "NO")