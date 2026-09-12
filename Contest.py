"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2260/A -----------------------------------------

Monocarp is preparing a team programming contest. The contest has n problems, each of which is either easy or hard. The problems are numbered from 1 to n.

Monocarp wants the first and the last problems of the contest to be easy. In one operation, he can choose any two problems and swap them.

Determine the minimum number of operations required to make the first and the last problems easy, or report that it is impossible.

Input
The first line contains an integer t (1≤t≤10^3) — the number of test cases.

Each test case consists of two lines

the first line contains one integer n (2≤n≤50) — the number of problems in the contest;
the second line contains n integers a1,a2,…,an (0≤ai≤1). If ai=0, then the problem with number i is easy; if ai=1, then it is hard.

Output
For each test case, print the minimum number of operations required to make the first and the last problems easy. If it is impossible to satisfy the requirement, print −1.

Input:
4
2
0 0
2
0 1
6
1 0 0 1 0 0
5
1 0 0 1 1

Output:
0
-1
1
2
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    if(arr[0] == arr[-1] and arr[0] == 0):
        print(0)
    else:
        temp_arr = arr[1:-1]
        needed = 0
        if(arr[0] == 1):
            needed += 1
        if(arr[-1] == 1):
            needed += 1
        if(temp_arr.count(0) >= needed):
            print(needed)
        else:
            print(-1)
    print("-------------------")