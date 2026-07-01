"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2241/A ---------------------------------

You are given two positive integers x and y.

You are allowed to perform the following operation any number of times (possibly zero):

Choose any positive integer z such that z divides x;
Set x:=xz.
Determine whether you can make x exactly equal to y using this operation.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of each test case follows.

The only line of each test case contains two space-separated integers x and y (1 ≤ x, y ≤ 100).

Output
For each test case, print "YES" if you can make x exactly equal to y and "NO" otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes" and "Yes" will be recognized as a positive response).

Input:
3
12 2
6 7
99 79

Output:
YES
NO
NO
"""
cases = int(input())
for _ in range(cases):
    x, y = map(int, input().split())
    if(x >= y and x % y == 0):
        print("YES")
    else:
        print("NO")        