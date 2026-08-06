"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2254/A --------------------------------

Alice, Bob, and Charlie are playing a game with tokens. They start with a, b, and c tokens, respectively.

The game is played in rounds. Before the beginning of each round, they check the number of tokens everyone has:

If any two players have the exact same number of tokens, the game immediately ends.
Otherwise, the round begins, all three players have a strictly different number of tokens. 
The player with the strictly most tokens gives exactly 1 token to the player with the strictly fewest tokens.
Given the starting tokens a, b, and c, determine exactly how many rounds the game will last before it ends.

Input
The first line contains a single integer t (1≤t≤10^3) — the number of test cases.

Each test case consists of a single line containing three integers a, b, and c (1≤a,b,c≤10).

Output
For each test case, output a single integer — the number of rounds the game will last before it ends.

Input:
6
1 2 3
4 6 1
3 3 7
1 7 10
6 1 9
1 1 1

Output:
1
2
0
3
3
0
"""
cases = int(input())
for _ in range(cases):
    a, b, c = map(int, input().split())
    if(a == b or b == c or a == c):
        print("0")
    else:
        # sorting a, b, c to find the middle value
        sorted_values = sorted([a, b, c])
        print(min(sorted_values[-1] - sorted_values[1], sorted_values[1] - sorted_values[0]))
    print("-------------")