"""


--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1927/C ----------------------------------

Given an array a of n integers, an array b of m integers, and an even number k.

Your task is to determine whether it is possible to choose exactly k2 elements from both arrays in such a way that among the chosen elements, every integer from 1 to k is included.

For example:

If a=[2,3,8,5,6,5], b=[1,3,4,10,5], k=6, then it is possible to choose elements with values 2,3,6 from array a and elements with values 1,4,5 from array b. 
In this case, all numbers from 1 to k=6 will be included among the chosen elements.
If a=[2,3,4,5,6,5], b=[1,3,8,10,3], k=6, then it is not possible to choose elements in the required way.
Note that you are not required to find a way to choose the elements — your program should only check whether it is possible to choose the elements in the required way.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains three integers n, m, and k (1≤n,m≤2⋅10^5, 2≤k≤2⋅min(n,m), k is even) — the length of array a, the length of array b, and the number of elements to be chosen, respectively.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^6) — the elements of array a.

The third line of each test case contains m integers b1,b2,…,bm (1 ≤ bj ≤ 10^6) — the elements of array b.

It is guaranteed that the sum of values n and m over all test cases in a test does not exceed 4⋅10^5.

Output
Output t lines, each of which is the answer to the corresponding test case. 
As the answer, output "YES" if it is possible to choose k2 numbers from each array in such a way that among the chosen elements, every integer from 1 to k is included. Otherwise, output "NO".

You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

Input:
6
6 5 6
2 3 8 5 6 5
1 3 4 10 5
6 5 6
2 3 4 5 6 5
1 3 8 10 3
3 3 4
1 3 5
2 4 6
2 5 4
1 4
7 3 4 4 2
1 4 2
2
6 4 4 2
1 5 2
3
2 2 1 4 3


Output:
YES
NO
YES
YES
NO
NO
"""
cases = int(input())
for _ in range(cases):
    n, m, k = map(int, input().split())
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    only_a = 0
    only_b = 0
    both = 0
    ok = True

    for v in range(1, k + 1):
        in_a = v in set_a
        in_b = v in set_b

        if(not in_a and not in_b):
            ok = False
            break

        if(in_a and not in_b):
            only_a += 1
        elif(in_b and not in_a):
            only_b += 1
        else:
            both += 1

    if(only_a > (k//2) or only_b > (k // 2)):
        ok = False
        #break

    need_a = (k//2) - only_a
    need_b = (k//2) - only_b

    if(need_a + need_b > both):
        ok = False
        #break

    print("YES" if ok else "NO")
    print("----------------------")
