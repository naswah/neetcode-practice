class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k;
        self.nums= nums;

    def add(self, val: int) -> int:
        self.nums.append(val);
        self.nums.sort();
        b = [];
        for i in range(len(self.nums)-1,-1,-1):
            b.append(self.nums[i]);

        return b[self.k-1];
    