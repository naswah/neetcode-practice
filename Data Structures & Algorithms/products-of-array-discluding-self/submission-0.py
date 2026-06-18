class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        for i in range(len(nums)):
            product = 1
            for j in range (len(nums)):
                if (i==j):
                    j+=1
                else:
                    product = product *nums[j]
            res.append(product)
        
        return res
        