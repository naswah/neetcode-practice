class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l= len(nums);
        if (l<2 and l>1000):
            return 0;
        if (target< -10000000 and target> 10000000):
            return 0;
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j];
                
        