class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ''.join(map(str, digits))
        result = int(result)+1;
        a = [];
        for i in str(result):
            a.append(int(i));
        return a;