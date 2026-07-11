"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/948/A -----------------------------------------

Bob is a farmer. He has a large pasture with many sheep. Recently, he has lost some of them due to wolf attacks. 
He thus decided to place some shepherd dogs in such a way that all his sheep are protected.

The pasture is a rectangle consisting of R × C cells. Each cell is either empty, contains a sheep, a wolf or a dog. 
Sheep and dogs always stay in place, but wolves can roam freely around the pasture, by repeatedly moving to the left, right, up or down to a neighboring cell. 
When a wolf enters a cell with a sheep, it consumes it. However, no wolf can enter a cell with a dog.

Initially there are no dogs. Place dogs onto the pasture in such a way that no wolf can reach any sheep, or determine that it is impossible. 
Note that since you have many dogs, you do not need to minimize their number.

Input
First line contains two integers R (1 ≤ R ≤ 500) and C (1 ≤ C ≤ 500), denoting the number of rows and the numbers of columns respectively.

Each of the following R lines is a string consisting of exactly C characters, representing one row of the pasture. Here, 'S' means a sheep, 'W' a wolf and '.' an empty cell.

Output
If it is impossible to protect all sheep, output a single line with the word "No".

Otherwise, output a line with the word "Yes". Then print R lines, representing the pasture after placing dogs. 
Again, 'S' means a sheep, 'W' a wolf, 'D' is a dog and '.' an empty space. You are not allowed to move, remove or add a sheep or a wolf.

If there are multiple solutions, you may print any of them. You don't have to minimize the number of dogs.

Input:
6 6
..S...
..S.W.
.S....
..W...
...W..
......

Output:
Yes
..SD..
..SDW.
.SD...
.DW...
DD.W..
......
"""
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

ok = True
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < r and 0 <= nj < c:
                    if arr[ni][nj] == 'W':
                        ok = False

# If safe, place dogs everywhere empty
if ok:
    print("YES")
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                arr[i][j] = 'D'
        print("".join(arr[i]))
else:
    print("NO")