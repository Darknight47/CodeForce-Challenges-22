"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/352/A --------------------------------------

Jeff's got n cards, each card contains either digit 0, or digit 5. Jeff can choose several cards and put them in a line so that he gets some number. 
What is the largest possible number divisible by 90 Jeff can make from the cards he's got?

Jeff must make the number without leading zero. At that, we assume that number 0 doesn't contain any leading zeroes. Jeff doesn't have to use all the cards.

Input
The first line contains integer n (1 ≤ n ≤ 10^3). The next line contains n integers a1, a2, ..., an (ai = 0 or ai = 5). Number ai represents the digit that is written on the i-th card.

Output
In a single line print the answer to the problem — the maximum number, divisible by 90. If you can't make any divisible by 90 number from the cards, print -1.

Input:
4
5 0 5 0

Output:
0
"""
n = int(input())
arr = list(map(int, input().split()))
fives = arr.count(5)
zeros = n - fives
if(fives < 9 and zeros == 0):
    print(-1)
elif(fives < 9 and zeros > 0):
    print(0)
elif(fives >= 9 and zeros > 0):
    temp_sum = 5 * fives
    temp = 0
    while temp_sum >= 45:
        if(temp_sum % 9 == 0):
            break
        temp_sum -= 5
        temp += 1
    fives -= temp
    print("5" * fives + "0" * zeros)
else:
    print(-1)