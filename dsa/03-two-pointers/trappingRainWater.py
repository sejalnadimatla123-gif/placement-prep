class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left <= right:
            if left_max < right_max:
                if left_max > height[left]:
                    water += left_max - height[left]
                
                else:
                    left_max = height[left]
                
                left += 1
            
            else:
                if right_max > height[right]:
                    water += right_max - height[right]
                
                else:
                    right_max = height[right]
                
                right -= 1
        
        return water

        