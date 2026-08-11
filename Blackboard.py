"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2256/A -------------------------------------

Rain is falling outside the Fairy Warehouse, so Chtholly, Nephren, and Ithea spend the afternoon playing a game in the common room.

Ithea writes three non-negative integers a, b, and c on the blackboard.

Chtholly may perform the following operation an arbitrary number of times (possibly zero):

Choose one of the three current integers and replace it with the sum of the other two current integers. The other two integers remain unchanged.
For example, starting from (3,5,11), she can replace 11 with 3+5, obtaining (3,5,8).

Nephren wants to know the minimum range∗ of the three integers that Chtholly can obtain. Help her find it!

∗ The range of a non-empty finite collection of numbers is defined as its maximum value minus its minimum value. In particular, the range of three numbers x, y, and z is max(x,y,z)−min(x,y,z).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The only line of each test case contains three integers a, b, and c (0 ≤ a, b, c ≤10^9) — the integers initially written on the blackboard.

Output
For each test case, output a single integer — the minimum possible range of the three integers.

Input:
6
5 5 5
4 6 9
2 3 10
0 0 7
2 3 5
20 4 5

Output:
0
5
3
0
3
5
"""
cases = int(input())
for _ in range(cases):
    arr = sorted(list(map(int, input().split())))
    if(arr[0] + arr[1] < arr[2]):
        print((arr[0] + arr[1]) - arr[0])
    else:
        print(arr[2] - arr[0])