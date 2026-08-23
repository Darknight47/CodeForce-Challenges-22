"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2002/B ------------------------------------

Alice got a permutation a1,a2,…,an of [1,2,…,n], and Bob got another permutation b1,b2,…,bn of [1,2,…,n]. They are going to play a game with these arrays.

In each turn, the following events happen in order:

Alice chooses either the first or the last element of her array and removes it from the array;
Bob chooses either the first or the last element of his array and removes it from the array.
The game continues for n−1 turns, after which both arrays will have exactly one remaining element: x in the array a and y in the array b.

If x=y, Bob wins; otherwise, Alice wins. Find which player will win if both players play optimally.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1≤n≤3⋅10^5).

The next line contains n integers a1,a2,…,an (1≤ai≤n, all ai are distinct) — the permutation of Alice.

The next line contains n integers b1,b2,…,bn (1≤bi≤n, all bi are distinct) — the permutation of Bob.

It is guaranteed that the sum of all n does not exceed 3⋅10^5.

Output
For each test case, print a single line with the name of the winner, assuming both players play optimally. If Alice wins, print Alice; otherwise, print Bob.

Input:
2
2
1 2
1 2
3
1 2 3
2 3 1

Output:
Bob
Alice
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    if(arr == brr):
        print("Bob")
    else:
        arr.reverse()
        if(arr == brr):
            print("Bob")
        else:
            print("Alice")