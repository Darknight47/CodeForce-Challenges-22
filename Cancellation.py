"""


------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1405/B ------------------------------------

You're given an array a of n integers, such that a1+a2+⋯+an=0.

In one operation, you can choose two different indices i and j (1≤i,j≤n), decrement ai by one and increment aj by one. If i<j this operation is free, otherwise it costs one coin.

How many coins do you have to spend in order to make all elements equal to 0?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 5000). Description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 10^5)  — the number of elements.

The next line contains n integers a1,…,an (−10^9 ≤ ai ≤ 10^9). It is given that ∑ni=1ai=0.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, print the minimum number of coins we have to spend in order to make all elements equal to 0.

Input:
7
4
-3 5 -3 1
2
1 -1
4
-3 2 -3 4
4
-1 1 1 -1
7
-5 7 -6 -4 17 -13 4
6
-1000000000 -1000000000 -1000000000 1000000000 1000000000 1000000000
1
0

Output:
3
0
4
1
8
3000000000
0
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    current_debt = 0 
    
    
    for i in range(len(arr) - 1, -1, -1):
        val = arr[i]
        
        if val < 0:
            # Accumulate debt. We need positive numbers to the left to cancel this.
            current_debt += abs(val)
        elif val > 0:
            if current_debt > 0:
                if val >= current_debt:
                    # This positive number completely cancels the accumulated debt
                    remainder = val - current_debt
                    ans += remainder # Only the leftover goes to ans
                    current_debt = 0  # Debt is completely cleared
                else:
                    # This positive number helps pay the debt but isn't enough
                    current_debt -= val
            else:
                # No debt exists to the right
                ans += val
                
    print(ans)
    print("-----------")