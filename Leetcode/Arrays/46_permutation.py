def sets_helper(result,bitmap,nums,hash,value):
    if bitmap == (1<<len(nums))-1:
        if tuple(value) not in hash:
            hash.add(tuple(value))
            temp = list(value)
            result.append(temp)
        return

    additions = [i for i in range(len(nums)) if (bitmap & (1 << i) == 0)]
    for i in additions:
        temp = list(value)
        temp.append(nums[i])
        sets_helper(result, bitmap | (1<<i), nums, hash,temp)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result =[]
        hash = set()
        bitmap = 0
        value = []
        permutation = []
        sets_helper(result,bitmap,nums,hash,value)
        return result