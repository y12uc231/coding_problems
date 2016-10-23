class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = [0]*(target+1)
        memo[0] = 1
        for i in range(1,target+1):
            for j in nums:
                k = i - j
                if k >=0:
                    memo[i]+=memo[k]
        return memo[target]