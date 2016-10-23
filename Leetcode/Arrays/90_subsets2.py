def sets_helper(result, bitmap, pos, nums, hash, hash2):
    hash.add(bitmap)
    temp1 = [nums[i] for i in range(pos) if (bitmap & (1 << i) != 0)]
    temp1.sort()
    string = ''.join([str(i) for i in temp1])
    if string not in hash2:
        result.append([nums[i] for i in range(pos) if (bitmap & (1 << i) != 0)])
        hash2.add(string)

    if pos == len(nums):
        return;

    if ((bitmap << 1) | 0) not in hash:
        sets_helper(result, (bitmap << 1) | 0, pos + 1, nums, hash, hash2)
    if ((bitmap << 1) | 1) not in hash:
        sets_helper(result, (bitmap << 1) | 1, pos + 1, nums, hash, hash2)


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        hash = set()
        hash2 = set()
        bitmap = 0
        pos = 0
        sets_helper(result, bitmap, pos, nums, hash, hash2)
        return result


