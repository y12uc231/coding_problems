def sets_helper(result,bitmap,nums,hash,value):
    if bitmap == (1<<len(nums))-1:
        if value not in hash:
            hash.add(value)
            result.append(value)
        return

    additions = [i for i in range(len(nums)) if (bitmap & (1 << i) == 0)]
    for i in additions:
        sets_helper(result, bitmap | (1<<i), nums, hash,value+nums[i])




def permutations(string):
    nums = list(string)
    result =[]
    hash = set()
    bitmap = 0
    value = ''
    sets_helper(result,bitmap,nums,hash,value)
    return result


print(permutations('aaaa'))
#for i in result:
#    print(i)
