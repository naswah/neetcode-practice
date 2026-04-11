class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = Counter(nums);
        for key, val in a.items():
            if val == 1:
                return key;
        return 0;
        