"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1436/B ------------------------------------------

Sasha likes investigating different math objects, for example, magic squares. 
But Sasha understands that magic squares have already been studied by hundreds of people, so he sees no sense of studying them further. Instead, he invented his own type of square — a prime square.

A square of size n×n is called prime if the following three conditions are held simultaneously:

all numbers on the square are non-negative integers not exceeding 105;
there are no prime numbers in the square;
sums of integers in each row and each column are prime numbers.
Sasha has an integer n. He asks you to find any prime square of size n×n. 
Sasha is absolutely sure such squares exist, so just help him!

Input
The first line contains a single integer t (1 ≤ t ≤ 10) — the number of test cases.

Each of the next t lines contains a single integer n (2 ≤ n ≤ 100) — the required size of a square.

Output
For each test case print n lines, each containing n integers — the prime square you built. If there are multiple answers, print any.

Input:
2
4
2

Output:
4 6 8 1
4 9 9 9
4 10 10 65
1 4 4 4
1 1
1 1
"""
import math

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.sqrt(x))
    for i in range(3, r+1, 2):
        if x % i == 0:
            return False
    return True

cases = int(input())
for _ in range(cases):
    n = int(input())

    if(is_prime(n)):
        for _ in range(n):
            print("1 " * n)
    else:
        target = n - 1
        x = None

        for cand in range(1, 100001):
            if not is_prime(cand):
                if(is_prime(target + cand)):
                    x = cand
                    break
        
        for i in range(n):
            row = []
            for j in range(n):
                if(i == j):
                    row.append(x)
                else:
                    row.append(1)
            print(*row)