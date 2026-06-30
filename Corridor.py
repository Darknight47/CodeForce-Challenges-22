"""

---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1872/B -------------------------------------

You are in a corridor that extends infinitely to the right, divided into square rooms. You start in room 1, proceed to room k, and then return to room 1. 
You can choose the value of k. Moving to an adjacent room takes 1 second.

Additionally, there are n traps in the corridor: the i-th trap is located in room di and will be activated si seconds after you enter the room di. 
Once a trap is activated, you cannot enter or exit a room with that trap.

Determine the maximum value of k that allows you to travel from room 1 to room k and then return to room 1 safely.

For instance, if n=1 and d1=2,s1=2, you can proceed to room k=2 and return safely (the trap will activate at the moment 1+s1=1+2=3, 
it can't prevent you to return back). But if you attempt to reach room k=3 , the trap will activate at the moment 1+s1=1+2=3, 
preventing your return (you would attempt to enter room 2 on your way back at second 3, but the activated trap would block you). 
Any larger value for k is also not feasible. Thus, the answer is k=2.

Input
The first line of the input contains an integer t (1 ≤ t ≤ 1000) — the number of test cases.

The descriptions of the test cases follow.

The first line of each test case description contains an integer n (1 ≤ n ≤ 100) — the number of traps.

The following n lines of each test case description present two integers di and si (1 ≤ di, si ≤ 200) — 
the parameters of a trap (you must leave room di strictly before si seconds have passed since entering this room). 
It's possible for multiple traps to occupy a single room (the values of di can be repeated).

Output
For each test case, print the maximum value of k that allows you to travel to room k and return to room 1 without encountering an active trap.

Input:
7
1
2 2
3
2 8
4 3
5 2
1
200 200
4
1 20
5 9
3 179
100 1
2
10 1
1 18
2
1 1
1 2
3
1 3
1 1
1 3

Output:
2
5
299
9
9
1
1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    ans = 10**18
    for _ in range(n):
        d, s = map(int, input().split())
        ans = min(ans, d + ((s - 1) // 2))
    print(ans)