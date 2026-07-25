"""

----------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/165/A ----------------------------------------------

One day Vasya painted a Cartesian coordinate system on a piece of paper and marked some set of points (x1, y1), (x2, y2), ..., (xn, yn). Let's define neighbors for some fixed point from the given set (x, y):

point (x', y') is (x, y)'s right neighbor, if x' > x and y' = y
point (x', y') is (x, y)'s left neighbor, if x' < x and y' = y
point (x', y') is (x, y)'s lower neighbor, if x' = x and y' < y
point (x', y') is (x, y)'s upper neighbor, if x' = x and y' > y
We'll consider point (x, y) from the given set supercentral, if it has at least one upper, at least one lower, at least one left and at least one right neighbor among this set's points.

Vasya marked quite many points on the paper. Analyzing the picture manually is rather a challenge, so Vasya asked you to help him. Your task is to find the number of supercentral points in the given set.

Input
The first input line contains the only integer n (1 ≤ n ≤ 200) — the number of points in the given set. 
Next n lines contain the coordinates of the points written as "x y" (without the quotes) (|x|, |y| ≤ 1000), all coordinates are integers. 
The numbers in the line are separated by exactly one space. It is guaranteed that all points are different.

Output
Print the only number — the number of supercentral points of the given set.

Input:
8
1 1
4 2
3 1
1 2
0 2
0 1
1 0
1 3

Output:
2
"""
n = int(input())
points = set()
dict_x = {}
dict_y = {}

for _ in range(n):
    x, y = map(int, input().split())
    points.add((x, y))

    dict_x.setdefault(x, []).append(y)
    dict_y.setdefault(y, []).append(x)
ans = 0
for x, y in points:
    xs = dict_y[y]
    has_left = any(xi < x for xi in xs)
    has_right = any(xi > x for xi in xs)

    ys = dict_x[x]
    has_down = any(yi < y for yi in ys)
    has_up = any(yi > y for yi in ys)
    if(has_left and has_right and has_up and has_down):
        ans += 1
print(ans)