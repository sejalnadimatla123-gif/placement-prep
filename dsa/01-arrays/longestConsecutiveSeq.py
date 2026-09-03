class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest_seq = 0

        for num in numSet:
            if num-1 not in numSet:
                current = num
                while current+1 in numSet:
                    current += 1
                
                seq_length = current - num + 1
                longest_seq = max(longest_seq,seq_length)

        return longest_seq 
                
        