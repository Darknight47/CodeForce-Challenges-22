"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1900/B ------------------------------

Laura is a girl who does not like combinatorics. Nemanja will try to convince her otherwise.

Nemanja wrote some digits on the board. All of them are either 1, 2, or 3. The number of digits 1 is a. 
The number of digits 2 is b and the number of digits 3 is c. He told Laura that in one operation she can do the following:

Select two different digits and erase them from the board. After that, write the digit (1, 2, or 3) different from both erased digits.
For example, let the digits be 1, 1, 1, 2, 3, 3. 
She can choose digits 1 and 3and erase them. Then the board will look like this 1, 1, 2, 3. After that, she has to write another digit 2, so at the end of the operation, the board will look like 1, 1, 2, 3, 2.

Nemanja asked her whether it was possible for only digits of one type to remain written on the board after some operations. If so, which digits can they be?

Laura was unable to solve this problem and asked you for help. As an award for helping her, she will convince Nemanja to give you some points.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^5). The description of the test cases follows.

The first and only line of each test case contains three integers a, b, c (1≤a,b,c≤100) — the number of ones, number of twos, and number of threes, respectively.

Output
For each test case, output one line containing 3 integers.

The first one should be 1 if it is possible that after some operations only digits 1 remain on the board, and 0 otherwise.

Similarly, the second one should be 1 if it is possible that after some operations only digits 2 remain on the board, and 0 otherwise.

Similarly, the third one should be 1 if it is possible that after some operations only digits 3 remain on the board, and 0 otherwise.

Input:
3
1 1 1
2 3 2
82 47 59

Output:
1 1 1
0 1 0
1 0 0
"""
cases = int(input())
for _ in range(cases):
    a, b, c = map(int, input().split())

    only1 = (b + c) % 2 == 0
    only2 = (a + c) % 2 == 0
    only3 = (a + b) % 2 == 0

    print(int(only1), int(only2), int(only3))