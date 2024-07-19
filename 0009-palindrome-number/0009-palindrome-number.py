class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0 or (x%10 == 0 and x != 0)):
            return False
        
        reversed = 0
        while(x > reversed):
            if(reversed > 0):
                reversed *= 10

            reversed += x%10

            x //= 10

        return reversed == x or reversed//10 == x

