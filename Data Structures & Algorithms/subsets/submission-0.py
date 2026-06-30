class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        result=[]

        def backtrack(start):
            ans.append(result[:])

            for i in range(start, len(nums)):
                result.append(nums[i])
                backtrack(i+1)
                result.pop()
        
        backtrack(0)
        return ans