"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1849/B --------------------------------------------------

Monocarp is playing yet another computer game. And yet again, his character is killing some monsters. There are n monsters, numbered from 1 to n, and the i-th of them has ai health points initially.

Monocarp's character has an ability that deals k damage to the monster with the highest current health. 
If there are several of them, the one with the smaller index is chosen. If a monster's health becomes less than or equal to 0 after Monocarp uses his ability, then it dies.

Monocarp uses his ability until all monsters die. Your task is to determine the order in which monsters will die.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains two integers n and k (1 ≤ n ≤ 3⋅10^5; 1 ≤ k ≤ 10^9) — the number of monsters and the damage which Monocarp's ability deals.

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the initial health points of monsters.

The sum of n over all test cases doesn't exceed 3⋅10^5.

Output
For each test case, print n integers — the indices of monsters in the order they die.

Input:
3
3 2
1 2 3
2 3
1 1
4 3
2 8 3 5

Output:
2 1 3 
1 2 
3 1 2 4 
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    diction = {}
    for i in range(n):
        num = arr[i]
        if(num % k == 0):
            diction[i + 1] = k
        else:
            diction[i + 1] = num % k    
    sorted_dict = dict(sorted(diction.items(), key=lambda item: item[1], reverse=True))
    print(*sorted_dict.keys())