"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/706/A -------------------------------------

Vasiliy lives at point (a, b) of the coordinate plane. He is hurrying up to work so he wants to get out of his house as soon as possible. 
New app suggested n available Beru-taxi nearby. The i-th taxi is located at point (xi, yi) and moves with a speed vi.

Consider that each of n drivers will move directly to Vasiliy and with a maximum possible speed. 
Compute the minimum time when Vasiliy will get in any of Beru-taxi cars.

Input
The first line of the input contains two integers a and b ( - 100 ≤ a, b ≤ 100) — coordinates of Vasiliy's home.

The second line contains a single integer n (1 ≤ n ≤ 1000) — the number of available Beru-taxi cars nearby.

The i-th of the following n lines contains three integers xi, yi and vi ( - 100 ≤ xi, yi ≤ 100, 1 ≤ vi ≤ 100) — the coordinates of the i-th car and its speed.

It's allowed that several cars are located at the same point. Also, cars may be located at exactly the same point where Vasiliy lives.

Output
Print a single real value — the minimum time Vasiliy needs to get in any of the Beru-taxi cars. You answer will be considered correct if its absolute or relative error does not exceed 10 - 6.

Namely: let's assume that your answer is a, and the answer of the jury is b. The checker program will consider your answer correct, if .

Input:
0 0
2
2 0 1
0 2 2

Output:
1.0
"""
import math
a, b = map(int, input().split())
n = int(input())
ans = float('inf')
for _ in range(n):
    x, y, v = map(int, input().split())
    dist = math.hypot(x - a, y - b) # sqrt((x - a)^2 + (y - b)^2)
    time = dist / v
    ans = min(ans, time)
print(ans)