numbers = [1,2,3,4,5,6,7,]

def uniques(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j: continue
            if nums[i] == nums[j] : return True
    return False

print(uniques(numbers))