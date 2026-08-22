"""

------------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1800/B -----------------------------------------------

Kristina has a string s of length n, consisting only of lowercase and uppercase Latin letters. For each pair of lowercase letter and its matching uppercase letter, Kristina can get 1 burl. 
However, pairs of characters cannot overlap, so each character can only be in one pair.

For example, if she has the string s = "aAaaBACacbE", she can get a burl for the following character pairs:

s1 = "a" and s2 = "A"
s4 = "a" and s6 = "A"
s5 = "B" and s10 = "b"
s7 = "C" and s9 = "c"
Kristina wants to get more burles for her string, so she is going to perform no more than k operations on it. In one operation, she can:

either select the lowercase character si (1≤i≤n) and make it uppercase.
or select uppercase character si (1≤i≤n) and make it lowercase.
For example, when k = 2 and s = "aAaaBACacbE" it can perform one operation: choose s3 = "a" and make it uppercase. Then she will get another pair of s3 = "A" and s8 = "a"

Find maximum number of burles Kristina can get for her string.

Input
The first line of input data contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The description of the test cases follows.

The first line of each test case contains two integers n (1≤n≤2⋅10^5) and k (0≤k≤n) — the number of characters in the string and the maximum number of operations that can be performed on it.

The second line of each test case contains a string s of length n, consisting only of lowercase and uppercase Latin letters.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, print exactly one integer on a separate line: the maximum number of burles that Kristina can get for her string s.

Input:
5
11 2
aAaaBACacbE
2 2
ab
4 1
aaBB
6 0
abBAcC
5 3
cbccb

Output:
5
0
1
3
2
"""
from collections import Counter

cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    s = input()
    counts = Counter(s)
    seen = set()
    ans = 0
    for char in counts:
        lower_char = char.lower()

        if(lower_char in seen):
            continue
        seen.add(lower_char)
        upper_char = char.upper()

        lower_char_count = counts[lower_char]
        upper_char_count = counts[upper_char]
        existed_pairs = min(lower_char_count, upper_char_count)
        ans += existed_pairs
        diff = max(lower_char_count, upper_char_count) - existed_pairs
        potential_extra = diff // 2

        if(k <= 0 or potential_extra <= 0):
            continue

        temp = min(k, potential_extra)
        ans += temp
        k -= temp
    print(ans)
    print("----------------")