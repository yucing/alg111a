# [-2,1,-3,4,-1,2,1,-5,4]

nums = [-2,1,-3,4,-1,2,1,-5,4]
max = 0
for i in range(len(nums)):
    sum = 0
    for j in range(i,len(nums)):
        sum += nums[j]
        if sum > max:
            max_list = []
            max = sum
            max_list = nums[i:j+1]

print(max)
print(max_list)

'''
class Solution(object):
    def maxSubArray(self, nums):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        max = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum > max:
                    max = sum

        print(max)
'''