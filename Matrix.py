"""

-------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1699/B -----------------------------------

You are given two even integers n and m. Your task is to find any binary matrix a with n rows and m columns where every cell (i,j) has exactly two neighbours with a different value than ai,j.

Two cells in the matrix are considered neighbours if and only if they share a side. More formally, the neighbours of cell (x,y) are: (x−1,y), (x,y+1), (x+1,y) and (x,y−1).

It can be proven that under the given constraints, an answer always exists.

Input
Each test contains multiple test cases. The first line of input contains a single integer t (1≤t≤100) — the number of test cases. The following lines contain the descriptions of the test cases.

The only line of each test case contains two even integers n and m (2≤n,m≤50) — the height and width of the binary matrix, respectively.

Output
For each test case, print n lines, each of which contains m numbers, equal to 0 or 1 — any binary matrix which satisfies the constraints described in the statement.

It can be proven that under the given constraints, an answer always exists.

Input:
3
2 4
2 2
4 4

Output:
1 0 0 1
0 1 1 0
1 0
0 1
1 0 1 0
0 0 1 1
1 1 0 0
0 1 0 1
"""
def generate_grid(n, m):
    if n % 2 != 0 or m % 2 != 0:
        raise ValueError("Both n and m must be even numbers.")

    grid = []
    for r in range(n):
        row = []
        for c in range(m):
            # Check if row block and column block have the same parity
            if (r // 2) % 2 == (c // 2) % 2:
                # Top-left and bottom-right of the 2x2 block are 1
                val = 1 if (r % 2 == c % 2) else 0
            else:
                # Top-right and bottom-left of the 2x2 block are 1
                val = 0 if (r % 2 == c % 2) else 1
            row.append(val)
        grid.append(row)

    return grid

cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    grid = generate_grid(n, m)
    for row in grid:
            print(" ".join(map(str, row)))
    print("----------------------")