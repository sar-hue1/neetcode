class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        mini= float('inf')
        for left in range(0,len(nums)):
            if nums[left]<mini:
                mini = nums[left]
                left-=1
        return int(mini)        

        