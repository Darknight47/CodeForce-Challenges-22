"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/17/A ----------------------------------------

Nick is interested in prime numbers. Once he read about Goldbach problem. It states that every even integer greater than 2 can be expressed as the sum of two primes. 
That got Nick's attention and he decided to invent a problem of his own and call it Noldbach problem. 
Since Nick is interested only in prime numbers, Noldbach problem states that at least k prime numbers from 2 to n inclusively can be expressed as the sum of three integer numbers: 
two neighboring prime numbers and 1. For example, 19 = 7 + 11 + 1, or 13 = 5 + 7 + 1.

Two prime numbers are called neighboring if there are no other prime numbers between them.

You are to help Nick, and find out if he is right or wrong.

Input
The first line of the input contains two integers n (2 ≤ n ≤ 1000) and k (0 ≤ k ≤ 1000).

Output
Output YES if at least k prime numbers from 2 to n inclusively can be expressed as it was described above. Otherwise output NO.

Input:
27 2

Output:
YES
"""
n, k = map(int, input().split())
# Sieve of Eratosthenes (Create the quick lookup grid)
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, n + 1, i):
            is_prime[j] = False
            
# Extract the ordered list of primes
primes = [i for i, prime_flag in enumerate(is_prime) if prime_flag]

count = 0
for i in range(len(primes) - 1):
    result = primes[i] + primes[i+1] + 1
    
    if result > n:
        break
        
    if is_prime[result]:
        count += 1
print("YES" if count >= k else "NO")