
#0ms
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d  = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        
        su=0
        for i in range(len(s)-1):
            if(d[s[i+1]]>d[s[i]]):
                su-=d[s[i]]    
            else:
                su+= d[s[i]]  
        su+= d[s[i+1]]
        return su
    
#7ms
# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        
#         d  = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
#         ls =[]
#         for i in s:
#             ls.append(d[i])
#         su = ls[0]
#         for i in range(1,len(ls)):
#             if(ls[i-1]>=ls[i]):
#                 su+= ls[i]
#             else:
#                 su+= ls[i] - ls[i-1] -ls[i-1]
#         return su

        
def main():
    s = input()
    ret = Solution().romanToInt(s)
    print(ret) 
        
if __name__ == "__main__":
    main()