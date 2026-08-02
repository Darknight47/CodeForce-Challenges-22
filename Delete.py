"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/contest/2248/problem/A ------------------------------------

Alice and Bob are given a binary string∗ s of length n. It contains at least one 0 and at least one 1.

They each perform exactly one operation in the following order:

First, Alice chooses an occurrence of 0 in s and deletes it.
Then, Bob chooses an occurrence of 1 in the resulting string and deletes it.
Alice wants the final string to be lexicographically† as large as possible, while Bob wants it to be lexicographically as small as possible. Determine the final string if both players act optimally.

∗ A binary string is a string consisting only of the characters 0 and 1.

† For two distinct binary strings a and b of the same length, a is lexicographically smaller than b if, at the first position where they differ, a has the smaller digit.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤100). The description of the test cases follows.

The only line of each test case contains a binary string s of length n (3≤n≤100).

It is guaranteed that s contains at least one 0 and at least one 1.

Output
For each test case, output the final string if both players act optimally.

Input:
4
101
11001
0010
0101010000010100100101

Output:
1
101
00
01010000010100100101
"""
cases = int(input())
for _ in range(cases):
    s = list(input())
    # removing the first occurrence of 0 and 1 from the string or list
    if '0' in s:
        s.remove('0')
    if '1' in s:
        s.remove('1')
    # printing the remaining characters in the list
    print(''.join(s))