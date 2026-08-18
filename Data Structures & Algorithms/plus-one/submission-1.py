class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        my_string = ""

        for i in digits:
            my_string += str(i)

        my_number = int(my_string) + 1

        lst= [int(digit)for digit in str(my_number)]

        return lst