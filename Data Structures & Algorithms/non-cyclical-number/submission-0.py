class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_square(n: int)-> int:
            total = 0;
            while (n>0):
                a = n % 10
                total += a*a
                n //= 10
            return total
        
        happy_number = set()
        while (n != 1):
            if n in happy_number:
                return False
            happy_number.add(n)
            n = calculate_square(n)
        return True
