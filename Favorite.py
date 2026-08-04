"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2037/C ---------------------------------------------

Superultra, a little red panda, desperately wants primogems. In his dreams, a voice tells him that he must solve the following task to obtain a lifetime supply of primogems. Help Superultra!

Construct a permutation∗ p of length n such that pi+pi+1 is composite† over all 1≤i≤n−1. If it's not possible, output −1.

∗ A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

† An integer x is composite if it has at least one other divisor besides 1 and x. For example, 4 is composite because 2 is a divisor.

Input
The first line contains t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case contains an integer n (2 ≤ n ≤ 2⋅10^5) — the length of the permutation.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, if it's not possible to construct p, output −1 on a new line. Otherwise, output n integers p1,p2,…,pn on a new line.

Input:
2
3
8

Output:
-1
1 8 7 3 6 2 4 5
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n <= 4):
        print("-1")
        continue
    
    evens = [x for x in range(2, n + 1, 2) if x != 4]
    odds = [x for x in range(1, n + 1, 2) if x != 5]
    
    
    print(*evens, 4, 5, *odds)