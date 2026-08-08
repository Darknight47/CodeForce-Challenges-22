"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1468/N ----------------------------------------------------


The progress is not standing still in Berland. Recently all garbage containers in Bertown, the capital of Berland, were replaced by differentiated recycling bins, 
each accepting some category of waste. While this will definitely improve the ecological situation, for some citizens it's difficult to get used to the habit of sorting waste.

Monocarp is one of those citizens who tries to get used to waste sorting. Today he has to take out the trash from his house. There are three containers near the Monocarp's house, the first one accepts paper waste, 
the second one accepts plastic waste, and the third one — all other types of waste. It is possible to fit c1 items into the first container, c2 items into the second container and c3 items into the third container.

Monocarp has a lot of items to throw into containers. Some are made of paper, so Monocarp has to put them into the first container (he has a1 such items), 
some are made of plastic, so he has to put them into the second container (he has a2 such items), and some are neither paper nor plastic — 
so Monocarp has to put them into the third container (he has a3 such items).

Unfortunately, there are also two categories of items that Monocarp is unsure of: he has a4 items which are partially made of paper, 
so he will put each of these items either into the first container or into the third container. Similarly, he has a5 items partially made of plastic, 
so he has to put each of them either into the second container or into the third container. 
Obviously, this choice is made separately for each item — for example, Monocarp can throw several partially-plastic items into the second container, and all other partially-plastic items — into the third one.

Now Monocarp wonders: is it possible to put each item into some container so that the first container will hold no more than c1 items, 
the second one — no more than c2 items, and the third one — no more than c3 items?

Input
The first line contains one integer t (1 ≤ t ≤ 3⋅10^4) — the number of test cases.

Each test case consists of two lines. The first line of each test case contains three integers c1, c2, c3 (0 ≤ c1, c2, c3 ≤ 10^8) — the capacities of the containers.

The second line of each test case contains five integers a1, a2, a3, a4, a5 (0 ≤ ai ≤ 10^8), where ai is the number of items of the i-th category Monocarp 
has to throw out (i=1 is paper waste, i=2 is plastic waste, i=3 is general waste, i=4 is partially-paper waste, i=5 is partially-plastic waste).

Output
For each test case, print either YES if it is possible to fit all items into containers, or NO otherwise. You may print each letter in any case
(for example, YES, Yes, yes, yEs will all be recognized as positive answer).

Input:
7
1 2 3
1 2 3 0 0
2 2 3
1 2 3 1 0
2 2 3
1 2 3 0 1
1 2 5
1 2 3 1 1
0 0 0
0 0 0 0 0
0 0 4
1 0 0 0 0
13 37 42
0 0 0 40 47

Output:
YES
YES
NO
YES
YES
NO
YES
"""
cases = int(input())
for _ in range(cases):
    cap_a, cap_b, cap_c = map(int, input().split())
    a, b, c, ac, bc = map(int, input().split())
    if(cap_c < c or cap_b < b or cap_a < a):
        print("NO")
        continue

    r1 = cap_a - a
    r2 = cap_b - b
    cap_c = cap_c - c

    need = max(0, ac - r1) + max(0, bc - r2)
    if(need <= cap_c):
        print("YES")
    else:
        print("NO")