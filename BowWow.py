"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2258/B1 -----------------------------------------

This is the easy version of the problem. The difference between the versions is that in this version, you only need to solve the problem for k=1. 
You can hack only if you solved all versions of this problem.

Alp loves carrots. Since he hasn't eaten lunch yet, he wants to buy a carrot salad to eat outside. 
However, he has a weird obsession: all the carrots must be the exact same length; otherwise, the salad doesn't look aesthetically pleasing to him. 
Since he is in the middle of the street and doesn't have a knife, he can't cut the carrots himself. You need to divide all the carrots using your machine and sell them to Alp.

You are given n delicious carrots with sizes a1,a2,…,an. You are also given a cutting machine, which works as follows.

For each operation, you choose a set of carrots (you can choose chopped carrots again) and a positive integer x (not necessarily the same for each operation).
After that, consider every chosen carrot, let its length be l. 
If l≤x, this carrot is unaffected; otherwise, it is divided into two carrots of sizes x and l−x.
We'll sell some of the final carrots to an interesting guy who wants them all to be the same length.

We are asking you to determine the maximum number of carrots we can sell after using this machine exactly k times. Solve the problem for only k=1.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤10^4). The description of the test cases follows.

The first line of each test case contains n and m (1≤n,m≤2⋅10^5), denoting the number of carrots and the maximum possible length of a carrot.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤m), denoting the initial carrot sizes.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5 and the sum of m over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single integer — the answer for k=1.

Input:
6
5 4
1 2 3 4 4
5 8
1 1 8 8 8
1 8
6
7 9
1 7 5 1 7 5 3
4 1
1 1 1 1
3 5
3 1 5

Output:
6
6
2
7
4
3
"""
from collections import Counter, defaultdict
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    frequency_dict = Counter(arr)
    sorted_keys = sorted(frequency_dict.keys())
    total_elements_ahead = sum(frequency_dict.values())
    bonus_counts = defaultdict(int)

    for n, f in frequency_dict.items():
        if n % 2 == 0:
            bonus_counts[n // 2] += f
    
    max_count = 0
    key_idx = 0
    num_unique_keys = len(sorted_keys)

    all_candidates = sorted(
        list(set([1] + sorted_keys + list(bonus_counts.keys())))
    )

    for x in all_candidates:
        # Advance our sorted keys pointer to drop elements smaller than X
        while key_idx < num_unique_keys and sorted_keys[key_idx] < x:
            total_elements_ahead -= frequency_dict[sorted_keys[key_idx]]
            key_idx += 1

        # Total copies = (Count of all valid elements >= X) + (Bonus elements where 2X == N)
        current_count = total_elements_ahead + bonus_counts[x]

        if current_count > max_count:
            max_count = current_count

    print(max_count)
    print("---------------------")