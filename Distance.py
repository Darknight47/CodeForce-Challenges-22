"""

------------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2060/B --------------------------------

Farmer John's n cows are playing a card game! Farmer John has a deck of n⋅m cards numbered from 0 to n⋅m−1. He distributes m cards to each of his n cows.

Farmer John wants the game to be fair, so each cow should only be able to play 1 card per round. 
He decides to determine a turn order, determined by a permutation∗ p of length n, such that the pi'th cow will be the i'th cow to place a card on top of the center pile in a round.

In other words, the following events happen in order in each round:

The p1 'th cow places any card from their deck on top of the center pile.
The p2 'th cow places any card from their deck on top of the center pile.
...
The pn
'th cow places any card from their deck on top of the center pile.
There is a catch. Initially, the center pile contains a card numbered −1. 
In order to place a card, the number of the card must be greater than the number of the card on top of the center pile. 
Then, the newly placed card becomes the top card of the center pile. If a cow cannot place any card in their deck, the game is considered to be lost.

Farmer John wonders: does there exist p such that it is possible for all of his cows to empty their deck after playing all m rounds of the game? If so, output any valid p. Otherwise, output −1.

∗ A permutation of length n contains each integer from 1 to n exactly once

Input
The first line contains an integer t (1≤t≤400) — the number of test cases.

The first line of each test case contains two integers n and m (1≤n⋅m≤2000) — the number of cows and the number of cards each cow receives.

The following n lines contain m integers each – the cards received by each cow. It is guaranteed all given numbers (across all n lines) are distinct and in the range from 0 to n⋅m−1, inclusive.

It is guaranteed the sum of n⋅m over all test cases does not exceed 2000.

Output
For each test case, output the following on a new line:

If p exists, output n space-separated integers p1,p2,…,pn.
Otherwise, output −1.

Input:
4
2 3
0 4 2
1 5 3
1 1
0
2 2
1 2
0 3
4 1
1
2
0
3

Output:
1 2
1
-1
3 1 2 4
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    arrs = []
    for _ in range(n):
        temp = sorted(set(map(int, input().split())))
        temp_possibility = all(y - x == n for x, y in zip(temp, temp[1:]))
        if(temp_possibility):
            arrs.append(temp)
        #arrs.append(sorted(list(map(int, input().split()))))

    if(len(arrs) != n):
        print("-1")
        continue

    ans = []
    for i in range(n*m):
        for j in range(n):
            if(i in arrs[j]):
                ans.append(j+1)
                break
        if(len(ans) == n):
            break
    print(" ".join(map(str, ans)))