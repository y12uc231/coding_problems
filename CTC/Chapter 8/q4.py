def sets_helper(result,bitmap,pos,nums,hash):
    hash.add(bitmap)
    result.append([nums[i] for i in range(pos) if (bitmap&(1<<i) != 0)])

    if pos == len(nums):
        return;

    if ((bitmap << 1) | 0) not in hash:
        sets_helper(result,(bitmap<<1) | 0,pos+1,nums,hash)
    if ((bitmap << 1) | 1) not in hash:
        sets_helper(result,(bitmap<<1) | 1,pos+1,nums,hash)



def power_set(nums):
    result =[]
    hash = set()
    bitmap = 0
    pos =0
    sets_helper(result,bitmap,pos,nums,hash)
    return result

print(power_set(range(3)))
#for i in result:
#    print(i)
