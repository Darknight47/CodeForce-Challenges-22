"""

-------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2244/B ----------------------------------------------

As is well known, Nikita loves reading. Today, he made a mess in his room and arranged his books into n stacks in a row, numbered from 1 to n from left to right. The i-th stack contains ai books. 
This arrangement is called neat if, in every stack except the rightmost one, the number of books is strictly less than in the stack to its right; that is, the array a is strictly increasing.

Yura wants to make the arrangement neat by performing the following operation any number of times:

Choose a stack i such that 1≤i<n and ai>1.
Take 1 book from the top of stack i, so ai decreases by 1.
Put this book on top of stack i+1, so ai+1 increases by 1.
Determine whether Yura can make the arrangement neat.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the number of stacks.

The second line of each test case contains n integers ai (1 ≤ ai ≤ 10^9) — the initial number of books in each stack.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output "YES" if Yura can make the arrangement neat, and "NO" otherwise.

You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted.

Input:
7
3
1 2 3
3
1 1 2
3
10 1 1
3
2 2 2
4
1 4 2 2
5
8 2 8 1 8
4
1 1 3 5

Output:
YES
NO
YES
YES
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ok = True
    for i in range(n - 1):
        cap = i + 1  
        leftover = 0
        if(arr[i] < cap):
            ok = False
            break       
        else:
            leftover = arr[i] - cap
        arr[i + 1] += leftover
    if(arr[-1] <= n - 1):
        ok = False
    print("YES" if ok else "NO")