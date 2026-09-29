class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        right = k
        current_sum = 0
        max_sum = 0

        for i in range(k):
            current_sum += nums[i]
        
        max_sum = current_sum

        while right < len(nums):
            current_sum = current_sum - nums[left] + nums[right]

            max_sum = max(max_sum,current_sum)

            left += 1
            right += 1
        
        max_average = float(max_sum)/k

        return max_average
        