"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2106/C -----------------------------

Two integer arrays a and b of size n are complementary if there exists an integer x such that ai+bi=x over all 1≤i≤n. 
For example, the arrays a=[2,1,4] and b=[3,4,1] are complementary, since ai+bi=5 over all 1≤i≤3. However, the arrays a=[1,3] and b=[2,1] are not complementary.

Cow the Nerd thinks everybody is interested in math, so he gave Cherry Bomb two integer arrays a and b. 
It is known that a and b both contain n non-negative integers not greater than k.

Unfortunately, Cherry Bomb has lost some elements in b. Lost elements in b are denoted with −1. 
Help Cherry Bomb count the number of possible arrays b such that:

a and b are complementary.
All lost elements are replaced with non-negative integers no more than k.
Input
The first line of the input contains a single integer t (1≤t≤10^4) — the number of test cases.

The first line of each test case contains two integers n and k (1≤n≤2⋅10^5, 0≤k≤10^9) — the size of the arrays and the maximum possible value of their elements.

The second line contains n integers a1,a2,...,an (0≤ai≤k).

The third line contains n integers b1,b2,...,bn (−1≤bi≤k). If bi=−1, then this element is missing.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
Output exactly one integer, the number of ways Cherry Bomb can fill in the missing elements from b such that a and b are complementary.

Input:
7
3 10
1 3 2
-1 -1 1
5 1
0 1 0 0 1
-1 0 1 0 -1
5 1
0 1 0 0 1
-1 1 -1 1 -1
5 10
1 3 2 5 4
-1 -1 -1 -1 -1
5 4
1 3 2 1 3
1 -1 -1 1 -1
5 4
1 3 2 1 3
2 -1 -1 2 0
5 5
5 0 5 4 3
5 -1 -1 -1 -1

Output:
1
0
0
7
0
1
0
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    temp_sum = -1   
    ans = 1
    # First pass: find fixed sum s if any b[i] is known
    for i in range(n):
        if brr[i] != -1:
            if temp_sum == -1:
                temp_sum = arr[i] + brr[i]
            else:
                if temp_sum != arr[i] + brr[i]:
                    ans = 0
                    break
    if(ans == 0):
        print(ans)
        continue
    #  temp_sum is still -1 → no known b[i]
    if temp_sum == -1:
        mx = max(arr) - min(arr)
        ans = k - mx + 1
        print(ans)
        continue
    
    # temp_sum is known → validate all positions
    for i in range(n):
        if arr[i] > temp_sum or temp_sum - arr[i] > k:
            ans = 0
            break

    print(ans)