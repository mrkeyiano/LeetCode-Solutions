#9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        num=x
        last_num=0
        
        while num:
            last_num=last_num*10+num%10
            num=int(num/10)
        return x == last_num
