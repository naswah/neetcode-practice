class Solution:
    def reverse(self, x: int) -> int:
        if (x > 0):
            sign = 1
        else:
            sign = -1
        
        x = abs(x)

        reversed_digit = 0
        while (x != 0):

            digit = x % 10
            reversed_digit = reversed_digit *10 + digit
            x //= 10

        result = sign* reversed_digit

        if(-2**31 <= result <= 2**31):
            return result
        else:
            return 0


        