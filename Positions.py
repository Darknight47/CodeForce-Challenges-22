"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/124/A ------------------------------------

Petr stands in line of n people, but he doesn't know exactly which position he occupies. 
He can say that there are no less than a people standing in front of him and no more than b people standing behind him. Find the number of different positions Petr can occupy.

Input
The only line contains three integers n, a and b (0 ≤ a, b < n ≤ 100).

Output
Print the single number — the number of the sought positions.

Input:
3 1 1

Output:
2
"""
n, a, b = map(int, input().split())
# left to right
left_limit = min(b + 1, n - a)
count_lr = max(0, left_limit)
print(count_lr)