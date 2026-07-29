"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/94/A -----------------------------------------

Igor K. always used to trust his favorite Kashpirovsky Antivirus. That is why he didn't hesitate to download the link one of his groupmates sent him via QIP Infinium. 
The link was said to contain "some real funny stuff about swine influenza". The antivirus had no objections and Igor K. run the flash application he had downloaded. 
Immediately his QIP Infinium said: "invalid login/password".

Igor K. entered the ISQ from his additional account and looked at the info of his main one. 
His name and surname changed to "H1N1" and "Infected" correspondingly, and the "Additional Information" field contained a strange-looking binary code 80 characters in length, 
consisting of zeroes and ones. "I've been hacked" — thought Igor K. and run the Internet Exploiter browser to quickly type his favourite search engine's address.

Soon he learned that it really was a virus that changed ISQ users' passwords. 
Fortunately, he soon found out that the binary code was actually the encrypted password where each group of 10 characters stood for one decimal digit. 
Accordingly, the original password consisted of 8 decimal digits.

Help Igor K. restore his ISQ account by the encrypted password and encryption specification.

Input
The input data contains 11 lines. The first line represents the binary code 80 characters in length. 
That is the code written in Igor K.'s ISQ account's info. Next 10 lines contain pairwise distinct binary codes 10 characters in length, corresponding to numbers 0, 1, ..., 9.

Output
Print one line containing 8 characters — The password to Igor K.'s ISQ account. It is guaranteed that the solution exists.

Input:
01001100100101100000010110001001011001000101100110010110100001011010100101101100
0100110000
0100110010
0101100000
0101100010
0101100100
0101100110
0101101000
0101101010
0101101100
0101101110

Output:
12345678
"""
s = input()
nums = {}
for i in range(10):
    temp = input()
    nums[temp] = i
chunk_size = 10
chunks = [s[i : i + chunk_size] for i in range(0, len(s), chunk_size)]
ans = []
for chunk in chunks:
    if(chunk in nums):
        ans.append(nums[chunk])
print(*ans, sep="")