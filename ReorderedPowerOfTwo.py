Reordered Power of 2
Problem:
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
Return true if and only if we can do this so that the resulting number is a power of two.

Approach:
1.Turn the digit to a string and sort.Store it in 'target'
2.If the leading number is not zero:
    For each power of 2:
      Turn it to a string,sort the digit and checks if it matches with the target.
3.Return true if it matches,otherwise return false.

Solution:
class Solution(object):
    def reorderedPowerOf2(self, n):
        target = sorted(str(n))  
        if str(n)[0] != '0':     
            for i in range(31):  
                power = sorted(str(1 << i))
                if target == power:
                    return True
        return False

