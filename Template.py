"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2000/C ---------------------------------

Kristina has an array a, called a template, consisting of n integers. She also has m strings, each consisting only of lowercase Latin letters. The strings are numbered from 1 to m. 
She wants to check which strings match the template.

A string s is considered to match the template if all of the following conditions are simultaneously satisfied:

The length of the string s is equal to the number of elements in the array a.
The same numbers from a correspond to the same symbols from s. So, if ai=aj, then si=sj for (1≤i,j≤n).
The same symbols from s correspond to the same numbers from a. So, if si=sj, then ai=aj for (1≤i,j≤n).
In other words, there must be a one-to-one correspondence between the characters of the string and the elements of the array.
For example, if a = [3,5,2,1,3], then the string "abfda" matches the template, while the string "afbfa" does not, since the character "f" corresponds to both numbers 1 and 5.

Input
The first line of input contains a single integer t (1≤t≤10^4) — the number of test cases.

The following descriptions are for the test cases.

The first line of each test case contains a single integer n (1≤n≤2⋅10^5) — the number of elements in the array a.

The second line of each test case contains exactly n integers ai (−10^9≤ai≤10^9) — the elements of the array a.

The third line of each test case contains a single integer m (1≤m≤2⋅10^5) — the number of strings to check for template matching.

Following are m strings, each containing a non-empty string sj (1≤|sj|≤2⋅10^5), consisting of lowercase Latin letters.

It is guaranteed that the sum of n across all test cases does not exceed 2⋅105, and that the sum of the lengths of all strings does not exceed 2⋅10^5.

Output
For each test case, output m lines. On the i-th line (1≤i≤m) output:

"YES", if the string with index i matches the template;
"NO" otherwise.
You may output the answer in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer).

Input:
3
5
3 5 2 1 3
2
abfda
afbfa
2
1 2
3
ab
abc
aa
4
5 -3 5 -3
4
aaaa
bcbc
aba
cbcb

Output:
YES
NO
YES
NO
NO
NO
YES
NO
YES
"""
def pattern_equal(s, a):
    if len(s) != len(a):
        return False

    m1 = {}
    m2 = {}

    for x, y in zip(s, a):
        if x not in m1 and y not in m2:
            m1[x] = y
            m2[y] = x
        elif (x in m1 and m1[x] != y) or (y in m2 and m2[y] != x):
            return False

    return True

# def pattern(arr):
#     first_pos = {}
#     out = []
#     for i, v in enumerate(arr):
#         if v not in first_pos:
#             first_pos[v] = i
#         out.append(first_pos[v])
#     return out

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ss = int(input())
    for _ in range(ss):
        s = input()
        if(len(s) != len(arr)):
            print("NO")
            continue
        print("YES" if pattern_equal(arr, s) else "NO")
    print("----------------")