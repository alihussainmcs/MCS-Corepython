"""
Merge the Tools in python - HackerRank Solution

Problem :

Consider the following:
A string, s, of length n where s = c0c1.....cn-1.
An integer, k, where k is a factor of n.
We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s.
Then, use each ti to create string ui such that:
The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once.
In other words, if the character at some index j in ti occurs at a previous index<j in ti, then do not include the
character in string ui.


Given s and k, print n/k lines where each line i denotes string ui.


Input Format :
The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.

Constraints :
1 <= n <= 10^4, where n is the length of s.
1 <= k <= n
it is guaranteed that n is a multiple of k.

Output Format :
Print n/k lines where each line i contains string ui.


Sample Input :
AABCAAADA
3

Sample Output :
AB
CA
AD

Explanation :
String s is split into n/k = 9/3 = 3 equal parts of length k = 3. We convert each ti to ui by removing any subsequent
occurrences non-distinct characters in ti:
t0 = "AAB" -> u0 = "AB"
t1 = "CAA" -> u1 = "CA"
t2 = "ADA" -> u2 = "AD"
We then print each ui on a new line.
"""
from collections import OrderedDict


def merge_the_tools(string, k):
    # your code goes here
    strlen = len(string)
    for i in range(0, strlen, k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
