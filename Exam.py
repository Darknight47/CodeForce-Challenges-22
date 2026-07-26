"""

-------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2051/C -----------------------------------------

Monocarp is preparing for his first exam at the university. There are n different questions which can be asked during the exam, numbered from 1 to n. 
There are m different lists of questions; each list consists of exactly n−1 different questions. 
Each list i is characterized by one integer ai, which is the index of the only question which is not present in the i-th list. 
For example, if n=4 and ai=3, the i-th list contains questions [1,2,4].

During the exam, Monocarp will receive one of these m lists of questions. 
Then, the professor will make Monocarp answer all questions from the list. So, Monocarp will pass only if he knows all questions from the list.

Monocarp knows the answers for k questions q1,q2,…,qk. For each list, determine if Monocarp will pass the exam if he receives that list.

Input
The first line contains one integer t (1≤t≤10^4) — the number of test cases.

Each test case consists of three lines:

the first line contains three integers n, m and k (2≤n≤3⋅10^5; 1≤m,k≤n);
the second line contains m distinct integers a1,a2,…,am (1≤ai≤n; ai<ai+1);
the third line contains k distinct integers q1,q2,…,qk (1≤qi≤n; qi<qi+1).
Additional constraints on the input:

the sum of n over all test cases does not exceed 3⋅10^5.
Output
For each test case, print a string of m characters. The i-th character should be 1 if Monocarp passes the exam if he receives the i-th question list, 0 if Monocarp won't pass.

Input:
4
4 4 3
1 2 3 4
1 3 4
5 4 3
1 2 3 4
1 3 4
4 4 4
1 2 3 4
1 2 3 4
2 2 1
1 2
2

Output:
0100
0000
1111
10
"""
cases = int(input())
for _ in range(cases):
    n, m, k = map(int, input().split())
    missing = list(map(int, input().split()))
    known = list(map(int, input().split()))
    diff = abs(n - k)
    if(diff > 1):
        print('0'*m)
        continue
    
    if k == n:
        print("1" * len(missing))
        continue

    # Otherwise he knows exactly n-1 questions → find the unknown one
    known_set = set(known)
    for q in range(1, n + 1):
        if q not in known_set:
            unknown = q
            break

    # He passes list i only if the missing question is the unknown one
    ans = []
    for a_i in missing:
        ans.append('1' if a_i == unknown else '0')

    print("".join(ans))