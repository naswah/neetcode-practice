class Solution: # House robber jastai nut exlure 1 and last house turn wise to find max
    def rob1(self, nums:List[int])-> int:

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 0:
            return 0

        prev2= nums[0]
        prev1= max(nums[0], nums[1])

        for i in range(2, len(nums)):
            total =max(prev1, nums[i]+prev2)
            prev2 = prev1
            prev1 = total
        return prev1
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        return max(
            self.rob1(nums[:-1]),
            self.rob1(nums[1:])
        )
        