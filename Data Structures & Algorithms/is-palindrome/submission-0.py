class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.lower();
        cleaned = ""
        for ch in a:
            if ch.isalnum():
                cleaned += ch
        my_list=list(cleaned);
        list2=[];
        for i in range(len(my_list)-1,-1,-1):
            list2.append(my_list[i]);

        if my_list == list2:
            return True;
        else:
            return False;
