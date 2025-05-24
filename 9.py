class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        m = str(x)
        n = m[: :-1]
        if(m==n):
            return True
        else:
            return False
def main():
    x = input()
    ret = Solution().isPalindrome(x)
    print(ret) 
        
if __name__ == "__main__":
    main()