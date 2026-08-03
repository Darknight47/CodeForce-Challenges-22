"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1300/B -----------------------------------------

Reminder: the median of the array [a1,a2,…,a2k+1] of odd number of elements is defined as follows: let [b1,b2,…,b2k+1] be the elements of the array in the sorted order. 
Then median of this array is equal to bk+1.

There are 2n students, the i-th student has skill level ai. It's not guaranteed that all skill levels are distinct.

Let's define skill level of a class as the median of skill levels of students of the class.

As a principal of the school, you would like to assign each student to one of the 2 classes such that each class has odd number of students (not divisible by 2).
The number of students in the classes may be equal or different, by your choice. Every student has to be assigned to exactly one class. 
Among such partitions, you want to choose one in which the absolute difference between skill levels of the classes is minimized.

What is the minimum possible absolute difference you can achieve?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the number of students halved.

The second line of each test case contains 2n integers a1,a2,…,a2n (1 ≤ ai ≤ 10^9) — skill levels of students.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output a single integer, the minimum possible absolute difference between skill levels of two classes of odd sizes.

Input:
3
1
1 1
3
6 5 4 1 2 3
5
13 4 20 13 2 5 8 3 17 16

Output:
0
1
5
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    half = len(arr) // 2
    ans = abs(arr[half - 1] - arr[half])
    print(ans)