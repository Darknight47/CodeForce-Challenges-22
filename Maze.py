"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1797/A -----------------------------------------

There is a rectangular maze of size n×m. Denote (r,c) as the cell on the r-th row from the top and the c-th column from the left. 
Two cells are adjacent if they share an edge. A path is a sequence of adjacent empty cells.

Each cell is initially empty. Li Hua can choose some cells (except (x1,y1) and (x2,y2)) and place an obstacle in each of them. 
He wants to know the minimum number of obstacles needed to be placed so that there isn't a path from (x1,y1) to (x2,y2).

Suppose you were Li Hua, please solve this problem.

Input
The first line contains the single integer t (1 ≤ t ≤ 500) — the number of test cases.

The first line of each test case contains two integers n,m (4 ≤ n, m ≤ 10^9) — the size of the maze.

The second line of each test case contains four integers x1,y1,x2,y2 (1≤x1,x2≤n,1≤y1,y2≤m) — the coordinates of the start and the end.

It is guaranteed that |x1−x2|+|y1−y2|≥2.

Output
For each test case print the minimum number of obstacles you need to put on the field so that there is no path from (x1,y1) to (x2,y2).

Input:
3
4 4
2 2 3 3
6 7
1 1 2 3
9 9
5 1 3 6

Output:
4
2
3
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    ans1 = 0
    if(x1 > 1): # we can move up
        ans1 += 1 
    if(x1 < n): # we can move down
        ans1 += 1
    if(y1 > 1): # we can move left
        ans1 += 1
    if(y1 < m): # we can move right
        ans1 += 1
    ans2 = 0
    if(x2 > 1): # we can move up
        ans2 += 1
    if(x2 < n): # we can move down
        ans2 += 1
    if(y2 > 1): # we can move left
        ans2 += 1
    if(y2 < m): # we can move right
        ans2 += 1
    print(min(ans1, ans2))