"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1837/C -----------------------------------------------

You are given a string s consisting of the characters 0, 1 and/or ?. Let's call it a pattern.

Let's say that the binary string (a string where each character is either 0 or 1) matches the pattern if you can replace each character ? with 0 or 1 
(for each character, the choice is independent) so that the strings become equal. For example, 0010 matches ?01?, but 010 doesn't match 1??, ??, or ????.

Let's define the cost of the binary string as the minimum number of operations of the form "reverse an arbitrary contiguous substring of the string" required to sort the string in non-descending order.

You have to find a binary string with the minimum possible cost among those that match the given pattern. If there are multiple answers, print any of them.

Input
The first line contains a single integer t (1≤t≤3⋅10^4) — the number of test cases.

The first and only line of each test case contains the string s (1≤|s|≤3⋅10^5) consisting of characters 0, 1, and/or ?.

The sum of the string lengths over all test cases does not exceed 3⋅10^5.

Output
For each test case, print a binary string with the minimum possible cost among those that match the given pattern. If there are multiple answers, print any of them.

Input:
4
??01?
10100
1??10?
0?1?10?10

Output:
00011
10100
111101
011110010
"""
cases = int(input())
for _ in range(cases):
    s = input()
    s = list(s) 
    n = len(s)

    i = 0
    while i < n:
        if s[i] != '?':
            i += 1
            continue

        # start of ? block
        start = i
        while i < n and s[i] == '?':
            i += 1
        end = i - 1  # last ? in block

        left = s[start - 1] if start > 0 else None
        right = s[end + 1] if end + 1 < n else None

        if left is None and right is None:
            fill = '0'
        elif left is None:
            fill = right
        elif right is None:
            fill = left
        else:
            fill = left  

        # fill block
        for k in range(start, end + 1):
            s[k] = fill
        i = end + 1

    print("".join(s))