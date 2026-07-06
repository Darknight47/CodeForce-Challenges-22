"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/914/A --------------------------------

Given an array a1, a2, ..., an of n integers, find the largest number in the array that is not a perfect square.

A number x is said to be a perfect square if there exists an integer y such that x = y2.

Input
The first line contains a single integer n (1 ≤ n ≤ 1000) — the number of elements in the array.

The second line contains n integers a1, a2, ..., an ( - 106 ≤ ai ≤ 106) — the elements of the array.

It is guaranteed that at least one element of the array is not a perfect square.

Output
Print the largest number in the array which is not a perfect square. It is guaranteed that an answer always exists.

Input:
2
4 2

Output:
2
"""
import math
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
for i in range(len(nums) - 1, -1, -1):
    num = nums[i]
    
    if num < 0:
        ans = num
        break      

    sr = int(math.isqrt(num))
    if sr * sr != num:
        ans =  num
        break
            
print(ans)