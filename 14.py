class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        out=""
        small = 200
        
        for i in strs:    
            if(len(i)<=small):
                small = len(i)
                ind = strs.index(i)
    
        for i in range(len(strs[ind])):
            flag =0
            for j in range(0,len(strs)):
                if(strs[ind][i]!=strs[j][i]):
                     flag=1
                     break 
            if(flag==0):
                out+=strs[ind][i]  
            else:
                break
        return out


def main():
    strs = input().split(",")
    ret = Solution().longestCommonPrefix(strs)
    print(ret) 
        
if __name__ == "__main__":
    main()       