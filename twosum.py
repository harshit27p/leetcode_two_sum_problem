mums = [2,7,11,15]
target = 9

def twosum(nums,target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num 
        if complement in num_map:
            return [num_map[complement],i]
         num_map[num]= i 
    return []
