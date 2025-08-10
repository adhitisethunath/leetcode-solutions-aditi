Divide Array Into Equal Pairs
Problem:
You are given an integer array nums consisting of 2 * n integers.
You need to divide nums into n pairs such that:
  Each element belongs to exactly one pair.
  The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

Approach:
1.Sort the numbers so that identical numbers appear next to each other.
2.iterate in steps of 2 and verify if num[i] == num[i+1]
  Return true if nums can be divided into n pairs, otherwise return false.

Solution:
class Solution:
    def divideArray(self, nums):
        nums.sort()
        return all(nums[i] == nums[i + 1] for i in range(0, len(nums), 2)) 
