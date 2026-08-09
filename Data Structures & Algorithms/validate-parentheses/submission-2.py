class Solution:
    def isValid(self, s: str) -> bool:
        result=[]

        for i in s:
            if i in "({[":
                result.append(i)

            elif i in ')}]':
                if not result: 
                    return False

                if (i==']' and result[-1]!='[') or (i=='}' and result[-1]!= '{') or (i==')' and result[-1]!='('):
                    return False
                result.pop()

            else:
                return False
                
        return len(result) == 0