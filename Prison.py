"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1415/A ------------------------------------------------

There is a prison that can be represented as a rectangular matrix with n rows and m columns. 
Therefore, there are n⋅m prison cells. There are also n⋅m prisoners, one in each prison cell. Let's denote the cell in the i-th row and the j-th column as (i,j).

There's a secret tunnel in the cell (r,c), that the prisoners will use to escape! However, to avoid the risk of getting caught, they will escape at night.

Before the night, every prisoner is in his own cell. When night comes, they can start moving to adjacent cells. 
Formally, in one second, a prisoner located in cell (i,j) can move to cells (i−1,j) , (i+1,j) , (i,j−1) , or (i,j+1), as long as the target cell is inside the prison. 
They can also choose to stay in cell (i,j).

The prisoners want to know the minimum number of seconds needed so that every prisoner can arrive to cell (r,c) if they move optimally. 
Note that there can be any number of prisoners in the same cell at the same time.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4), the number of test cases.

Each of the next t lines contains four space-separated integers n, m, r, c (1 ≤ r ≤ n ≤ 10^9, 1 ≤ c ≤ m ≤ 10^9).

Output
Print t lines, the answers for each test case.

Input:
3
10 10 1 1
3 5 2 4
10 2 5 1

Output:
18
4
6
"""
cases = int(input())
for _ in range(cases):
    n, m, r, c = map(int, input().split())
    d1 = abs(1 - r) + abs(1 - c)
    d2 = abs(1 - r) + abs(m - c)
    d3 = abs(n - r) + abs(1 - c)
    d4 = abs(n - r) + abs(m - c)
    print(max(d1, d2, d3, d4))