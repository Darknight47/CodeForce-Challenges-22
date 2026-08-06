"""

------------------------------------------------- Link for the challenge: https://codeforces.com/contest/2254/problem/B ----------------------------------------------

Let f(s) be the compressed version of a string s, formed by replacing every maximal contiguous block of identical characters with a single copy of that character. For example, f("aabbcc") = "abc".

Let |s| denote the length of a string s. Following this, |f(s)| denotes the length of the compressed string. For example:

|f("aabbcc")|= |"abc"| =3
If the string is empty, its length is 0.
Yousef has given you a string s consisting of n lowercase Latin letters. You must delete exactly one character si (2≤i≤n−1) to form a new string s′, and then find the minimum possible value of |f(s′)|.

Note that you cannot delete s1 or sn.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains an integer n (3 ≤ n ≤ 2 ⋅ 10^5) — the length of the string.

The second line of each test case contains a string s (|s|=n), consisting of lowercase Latin letters.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single integer — the minimum possible length of the resulting compressed string after deleting one character.

Input:
9
3
abb
3
aab
3
abc
4
abaa
4
abba
5
eeeee
6
yyssee
7
abacaba
18
goodluckandhavefun

Output:
2
2
2
1
3
1
3
5
16
"""
from itertools import groupby
cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()
    groups = [(k, len(list(g))) for k, g in groupby(s)]
    #groups = ["".join(group) for key, group in groupby(s)]
    ans = len(groups)
    found_min1 = False
    found_min2 = False
    for i in range(1, len(groups) - 1):
        char, length = groups[i]
        if(length == 1):
            prev_char = groups[i - 1][0]
            next_char = groups[i + 1][0]
            if(prev_char == next_char):
                ans -= 2
                found_min2 = True
                break
            found_min1 = True
    if(not found_min2 and found_min1):
        ans -= 1
    print(ans)