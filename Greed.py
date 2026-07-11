"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/892/A -------------------------------

Jafar has n cans of cola. Each can is described by two integers: remaining volume of cola ai and can's capacity bi (ai  ≤  bi).

Jafar has decided to pour all remaining cola into just 2 cans, determine if he can do this or not!

Input
The first line of the input contains one integer n (2 ≤ n ≤ 100 000) — number of cola cans.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 109) — volume of remaining cola in cans.

The third line contains n space-separated integers that b1, b2, ..., bn (ai ≤ bi ≤ 109) — capacities of the cans.

Output
Print "YES" (without quotes) if it is possible to pour all remaining cola in 2 cans. Otherwise print "NO" (without quotes).

You can print each letter in any case (upper or lower).

Input:
2
3 5
3 6

Output:
YES
"""
n = int(input())
arr = list(map(int, input().split()))
cans = sorted(list(map(int, input().split())))
temp_sum = sum(arr)
capacity = cans[-1] + cans[-2]
if(temp_sum > capacity):
    print("NO")
else:
    print("YES")