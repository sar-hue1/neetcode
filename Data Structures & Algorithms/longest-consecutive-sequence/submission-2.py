class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        nums_set = set(nums)
        for i in range(0,len(nums)):  
                if nums[i]-1 not in nums_set:
                    start = nums[i]
                    curr_count=1

                    while start+1 in nums_set:
                         start+=1
                         curr_count+=1
                    count = max(count,curr_count)
        return count                 








                
        