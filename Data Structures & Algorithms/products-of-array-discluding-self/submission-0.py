class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod_left = 1
        prod_right = 1

        res = [1]*n
        for i in range(n):
            res[i]=prod_left
            prod_left *= nums[i]


        for i in range(n-1,-1,-1):
            res[i]*=prod_right           
            prod_right *= nums[i]

        return res
        