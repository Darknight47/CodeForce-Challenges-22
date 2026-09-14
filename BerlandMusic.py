"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1622/B ------------------------------------------

Berland Music is a music streaming service built specifically to support Berland local artist. Its developers are currently working on a song recommendation module.

So imagine Monocarp got recommended n songs, numbered from 1 to n. 
The i-th song had its predicted rating equal to pi, where 1≤pi≤n and every integer from 1 to n appears exactly once. In other words, p is a permutation.

After listening to each of them, Monocarp pressed either a like or a dislike button. 
Let his vote sequence be represented with a string s, such that si=0 means that he disliked the i-th song, and si=1 means that he liked it.

Now the service has to re-evaluate the song ratings in such a way that:

the new ratings q1,q2,…,qn still form a permutation (1≤qi≤n; each integer from 1 to n appears exactly once);
every song that Monocarp liked should have a greater rating than every song that Monocarp disliked (formally, for all i,j such that si=1 and sj=0, qi>qj should hold).
Among all valid permutations q find the one that has the smallest value of ∑i=1n|pi−qi|, where |x| is an absolute value of x.

Print the permutation q1,q2,…,qn. If there are multiple answers, you can print any of them.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The first line of each testcase contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the number of songs.

The second line of each testcase contains n integers p1,p2,…,pn (1≤pi≤n) — the permutation of the predicted ratings.

The third line contains a single string s, consisting of n characters. Each character is either a 0 or a 1. 
0 means that Monocarp disliked the song, and 1 means that he liked it.

The sum of n over all testcases doesn't exceed 2⋅10^5.

Output
For each testcase, print a permutation q — the re-evaluated ratings of the songs. If there are multiple answers such that ∑i=1n|pi−qi| is minimum possible, you can print any of them.

Input:
3
2
1 2
10
3
3 1 2
111
8
2 3 1 8 5 4 7 6
01110001

Output:
2 1
3 1 2
1 6 5 8 3 2 4 7
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    s = input()
    
    zeros_indices = []
    ones_indices = []
    
    for i in range(n):
        if s[i] == '0':
            zeros_indices.append(i)
        else:
            ones_indices.append(i)
            
    # Sort indices by their initial array values to maintain relative order
    zeros_indices.sort(key=lambda i: arr[i])
    ones_indices.sort(key=lambda i: arr[i])
    
    res = [0] * n
    
    val = 1
    for idx in zeros_indices:
        res[idx] = val
        val += 1
        
    for idx in ones_indices:
        res[idx] = val
        val += 1
        
    print(*res)