class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        num = [i for i in num]
        c = [0] * len(num)
        for i in range(0, len(num), 1):
            c[i] = nums.count(num[i])

        return num[c.index(max(c))]    