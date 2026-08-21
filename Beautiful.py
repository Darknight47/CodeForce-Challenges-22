"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1861/B -----------------------------------------

You are given two strings a and b of equal length, consisting of only characters 0 and/or 1; both strings start with character 0 and end with character 1.

You can perform the following operation any number of times (possibly zero):

choose one of the strings and two equal characters in it; then turn all characters between them into those characters.
Formally, you choose one of these two strings (let the chosen string be s), then pick two integers l and r such that 1≤l<r≤|s| and sl=sr, then replace every character si such that l<i<r with sl.

For example, if the chosen string is 010101, you can transform it into one of the following strings by applying one operation:

000101 if you choose l=1 and r=3;
000001 if you choose l=1 and r=5;
010001 if you choose l=3 and r=5;
010111 if you choose l=4 and r=6;
011111 if you choose l=2 and r=6;
011101 if you choose l=2 and r=4.
You have to determine if it's possible to make the given strings equal by applying this operation any number of times.

Input
The first line contains a single integer t (1≤t≤2000)  — the number of test cases.

Each test case consists of two lines:

the first line contains the string a (2≤|a|≤5000), consisting of only characters 0 and/or 1.
the second line contains the string b (2≤|b|≤5000), consisting of only characters 0 and/or 1.Additional constraints on the input:

in each test case, |a|=|b| (the strings have equal length);
in each test case, both strings start with 0 and end with 1;
the total length of all strings a in all test cases does not exceed 5000.

Output
For each test case, print YES if it is possible to make the strings equal. Otherwise, print NO. You can print each letter in any register.

Input:
7
01010001
01110101
01001
01001
000101
010111
00001
01111
011
001
001001
011011
010001
011011

Output:
YES
YES
YES
NO
NO
NO
YES
"""
cases = int(input())
for _ in range(cases):
    a = input()
    b = input()
    ok = False
    for i in range(len(a) - 1):
        if( (a[i] == '0' and a[i] == b[i]) and (a[i + 1] == '1' and a[i + 1] == b[i + 1])):
            ok = True
            break
    print("YES" if ok else "NO")
    print("------------------")