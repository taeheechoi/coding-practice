def singleNumber(nums):
    count = {}
    for num in nums:
        if not num in count:
            count[num] = 1
        else:
            count[num] += 1
    

singleNumber([2, 2, 1])    
