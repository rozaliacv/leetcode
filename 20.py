class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [0]
        for i in s:
            if(i=='('or i=='['or i=='{'):
                stack.append(i)
            else:
                j = stack[-1]
                if(i==')' and j=='('):
                    stack.pop()
                elif( i==']' and j=='['):
                    stack.pop()
                elif(i=='}' and j=='{'):
                    stack.pop()
                else:
                    return False
        stack.remove(0)        
        return (len(stack)==0)
def main():
    s = input()
    ret = Solution().isValid(s)
    print(ret) 
        
if __name__ == "__main__":
    main()