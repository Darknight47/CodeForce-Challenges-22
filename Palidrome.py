"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/798/A ------------------------------------

Mike has a string s consisting of only lowercase English letters. He wants to change exactly one character from the string so that the resulting one is a palindrome.

A palindrome is a string that reads the same backward as forward, for example strings "z", "aaa", "aba", "abccba" are palindromes, but strings "codeforces", "reality", "ab" are not.

Input
The first and single line contains string s (1 ≤ |s| ≤ 15).

Output
Print "YES" (without quotes) if Mike can change exactly one character so that the resulting string is palindrome or "NO" (without quotes) otherwise.

Input:
abccaa

Output:
YES
"""
s = input()
n = len(s)
ok = True
unequal_pairs = sum(1 for i in range(n // 2) if s[i] != s[n - 1 - i])
if(unequal_pairs >= 2):
    ok = False
elif(unequal_pairs == 0 and n % 2 == 0):
    ok = False
print("YES" if ok else "NO")