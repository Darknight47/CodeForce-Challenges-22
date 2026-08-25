"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2145/B -----------------------------------------------

Monocarp has a deck of cards numbered from 1 to n. Initially, the cards are arranged from smallest to largest, with 1 on top and n at the bottom.

Monocarp performed k actions on the deck. Each action was one of three types:

remove the top card;
remove the bottom card;
remove either the top or bottom card.
Your task is to determine the fate of each card: whether it remains in the deck, has been removed, or might be both.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains two integers n and k (1 ≤ k ≤ n ≤ 2⋅10^5).

The second line contains a string s of length k, consisting of characters 0, 1, and/or {2}. This string describes Monocarp's actions. 
If the i-th character is 0, Monocarp removes the top card on the i-th action. If it's 1, he removes the bottom card. If it's 2, either the top or bottom card can be removed.

Additional constraint on the input: the sum of n over all test cases doesn't exceed 2⋅10^5.

Output
For each test case, print a string consisting of n characters. The i-th character should be + (plus sign) if the i-th card is still in the deck, 
- (minus sign) if it has been removed, or ? (question mark) if its state is unknown.

Input:
4
4 2
01
3 2
22
1 1
2
7 5
01201


Output:
-++-
???
-
--?+?--
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    s = input()

    cnt0 = cnt1 = cnt2 = 0
    for temp in s:
        if(temp == '0'):
            cnt0 += 1
        elif(temp == '1'):
            cnt1 += 1
        else:
            cnt2 += 1
    
    min_top = cnt0
    max_top = cnt0 + cnt2
    
    min_bot = cnt1
    max_bot = cnt1 + cnt2
    
    result = []
    if(n == k):
        print('-'*n)
        continue

    for i in range(1, n + 1):
        if i <= min_top or i > (n - min_bot):
            result.append('-')
        elif i > max_top and i <= (n - max_bot):
            result.append('+')
        else:
            result.append('?')
            
    print("".join(result))