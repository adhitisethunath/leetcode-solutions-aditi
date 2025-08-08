Problem:
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order

Example 1:
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Approach:
- Use list comprehension with `enumerate()`
- Check if `x` is in each word
- Collect the index if it matches

class Solution(object):
    def findWordsContaining(self, words, x):
        return [i for i,w in enumerate(words) if x in w]
