"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        maximum = 0
        for i in s:
            if i in seen:
                maximum = max(maximum, len(seen))
                seen = seen[seen.index(i) + 1:]  # slice 'seen' after the repeated element
            seen.append(i)
        maximum = max(maximum, len(seen))
        return maximum
