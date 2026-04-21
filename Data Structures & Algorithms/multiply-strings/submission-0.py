class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def convert_to_int(nums:str) -> int:
            num =0
            for i in range(len(nums)):
                num= (num*10 + ord(nums[i])-48)
            return num;

        num1= convert_to_int(num1)
        num2=convert_to_int(num2)

        result= num1* num2

        return str(result)
        