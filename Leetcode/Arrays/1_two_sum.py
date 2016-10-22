class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        has = dict()
        for i in range(0, len(nums)):
            has.update({nums[i]: i})

        for i in range(0, len(nums)):
            if has.has_key(target - nums[i]) and i != has[target - nums[i]]:
                return [i, has[target - nums[i]]]

        return False    