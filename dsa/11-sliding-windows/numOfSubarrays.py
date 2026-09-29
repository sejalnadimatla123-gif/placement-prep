class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        left = 0
        right = k
        current_sum = 0
        target_sum = threshold * k
        count = 0

        for i in range(k):
            current_sum += arr[i]
        
        if current_sum >= target_sum:
            count += 1
            
        while right < len(arr):
            current_sum = current_sum - arr[left] + arr[right]

            if current_sum >= target_sum:
                count += 1

            left += 1
            right += 1
        
        return count
        

        