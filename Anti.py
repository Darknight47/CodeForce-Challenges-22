"""

-------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1610/A ---------------------------------------

You are playing a game on a n×m grid, in which the computer has selected some cell (x,y) of the grid, and you have to determine which one.

To do so, you will choose some k and some k cells (x1,y1),(x2,y2),…,(xk,yk), and give them to the computer. 
In response, you will get k numbers b1,b2,…bk, where bi is the manhattan distance from (xi,yi) to the hidden cell (x,y) (so you know which distance corresponds to which of k input cells).

After receiving these b1,b2,…,bk, you have to be able to determine the hidden cell. 
What is the smallest k for which is it possible to always guess the hidden cell correctly, no matter what cell computer chooses?

As a reminder, the manhattan distance between cells (a1,b1) and (a2,b2) is equal to |a1−a2|+|b1−b2|.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of test cases follows.

The single line of each test case contains two integers n and m (1 ≤ n, m ≤ 10^9) — the number of rows and the number of columns in the grid.

Output
For each test case print a single integer — the minimum k for that test case.

Input:
2
2 3
3 1

Output:
2
1
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    if(n == 1 and m == 1):
        print(0)
    elif(n == 1 or m == 1):
        print(1)
    else:
        print(2)