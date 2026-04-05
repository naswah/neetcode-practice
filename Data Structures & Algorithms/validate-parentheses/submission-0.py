class Solution:
    def isValid(self, s: str) -> bool:
        list1 = list(s)
        st=[]
        for c in list1:
            if (c == '(' or c== '{' or c== '['):
                st.append(c)
            else:
                if not st:
                    return False
           
                top= st[-1]

                if((c== ')' and top=='(') or 
                (c== '}' and top == '{') or
                (c == ']' and top == '[')):
                    
                    st.pop()
                else:
                    return False
        return len(st) == 0
 





        