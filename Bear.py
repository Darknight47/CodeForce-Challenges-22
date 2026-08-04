"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/680/B ------------------------------------------

There are n cities in Bearland, numbered 1 through n. Cities are arranged in one long row. The distance between cities i and j is equal to |i - j|.

Limak is a police officer. He lives in a city a. His job is to catch criminals. It's hard because he doesn't know in which cities criminals are. 
Though, he knows that there is at most one criminal in each city.

Limak is going to use a BCD (Bear Criminal Detector). The BCD will tell Limak how many criminals there are for every distance from a city a. 
After that, Limak can catch a criminal in each city for which he is sure that there must be a criminal.

You know in which cities criminals are. Count the number of criminals Limak will catch, after he uses the BCD.

Input
The first line of the input contains two integers n and a (1 ≤ a ≤ n ≤ 100) — the number of cities and the index of city where Limak lives.

The second line contains n integers t1, t2, ..., tn (0 ≤ ti ≤ 1). There are ti criminals in the i-th city.

Output
Print the number of criminals Limak will catch.

Input:
6 3
1 1 1 0 1 0

Output:
3
"""
n, a = map(int, input().split())
arr = list(map(int, input().split()))
a -= 1  # convert to 0-index
counter = 0

if arr[a] == 1:
    counter += 1

# --- Distances d = 1, 2, 3, ... ---
d = 1
while True:
    L = a - d
    R = a + d

    L_valid = (0 <= L < n)
    R_valid = (0 <= R < n)

    # Case C: both sides invalid → check edges
    if not L_valid and not R_valid:
        break
    if (L_valid and R_valid) and (arr[L] == 1 and arr[R] == 1):
        counter += 2
        # if both sides are 0 → +0
    else:
        # Case B: exactly one side valid → certainty
        if L_valid and not R_valid:
            if arr[L] == 1:
                counter += 1

        elif R_valid and not L_valid:
            if arr[R] == 1:
                counter += 1
    d += 1
print(counter)