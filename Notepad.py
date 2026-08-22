"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1766/B --------------------------------------

You want to type the string s, consisting of n lowercase Latin letters, using your favorite text editor Notepad#.

Notepad# supports two kinds of operations:

append any letter to the end of the string;
copy a continuous substring of an already typed string and paste this substring to the end of the string.
Can you type string s in strictly less than n operations?

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The first line of each testcase contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the length of the string s.

The second line contains a string s, consisting of n lowercase Latin letters.

The sum of n doesn't exceed 2⋅10^5 over all testcases.

Output
For each testcase, print "YES" if you can type string s in strictly less than n operations. Otherwise, print "NO".

Input:
6
10
codeforces
8
labacaba
5
uohhh
16
isthissuffixtree
1
x
4
momo

Output:
NO
YES
NO
YES
NO
YES
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()
    seen = {}
    ok = False
    for i in range(len(s) - 1):
        substring = s[i:i+2]
        # Check if we have seen it before and it doesn't overlap
        if substring in seen and seen[substring] <= i:
            ok = True
            break
        if substring not in seen:
            seen[substring] = i + 2 # Store where this substring ends
    print("YES" if ok else "NO")
    print("------------------")