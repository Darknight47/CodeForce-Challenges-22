"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/610/A -----------------------------------------

Pasha has a wooden stick of some positive integer length n. He wants to perform exactly three cuts to get four parts of the stick. 
Each part must have some positive integer length and the sum of these lengths will obviously be n.

Pasha likes rectangles but hates squares, so he wonders, how many ways are there to split a stick into four parts so that 
it's possible to form a rectangle using these parts, but is impossible to form a square.

Your task is to help Pasha and count the number of such ways. Two ways to cut the stick are considered distinct if there exists some integer x, 
such that the number of parts of length x in the first way differ from the number of parts of length x in the second way.

Input
The first line of the input contains a positive integer n (1 ≤ n ≤ 2·10^9) — the length of Pasha's stick.

Output
The output should contain a single integer — the number of ways to split Pasha's stick into four parts of positive integer length so 
that it's possible to make a rectangle by connecting the ends of these parts, but is impossible to form a square.

Input:
6

Output:
1
"""
n = int(input())
if(n % 2 == 1):
    print(0)
else:
    if(n % 4 == 0):
        print(n//4 - 1)
    else:
        print(n//4)