"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2263/A -----------------------------------------

Bessie and Elsie are playing a game on a binary array a of length n.

The players alternate turns, with Bessie moving first. 
On Bessie's turn, she chooses two adjacent elements x and y and replaces them with the single value max(x,y).

On Elsie's turn, she chooses two adjacent elements x and y and replaces them with the single value min(x,y).

After each move, the length of the array decreases by 1. 
The game ends when only one element remains. Bessie wins if the final element is 1, and Elsie wins if the final element is 0.

Assuming both players play optimally, determine who wins.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤500). The description of the test cases follows.

The first line of each test case contains a single integer n (2≤n≤100).

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤1).

Output
For each test case, you should output the name of who wins on a new line.

Input:
3
5
1 0 1 0 1
3
0 0 1
4
1 1 0 0

Output:
Bessie
Elsie
Bessie
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ones = arr.count(1)
    zeros = n - ones
    if(ones >= zeros):
        print("Bessie")
    else:
        print("Elsie")