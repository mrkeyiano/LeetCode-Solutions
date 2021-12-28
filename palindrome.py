#9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        reverse_num=0
        
        while num:
            reverse_num=reverse_num*10+num%10
            num=int(num/10)
        return num == reverse_num
