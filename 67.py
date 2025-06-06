class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        length = max(len(a), len(b))
        a = a.rjust(length, '0')
        b = b.rjust(length, '0')
               
        c=""
        indx=0
        i=length-1
        while(i>=0 or indx):
            if(i<0):
                num = indx
            else:
                num = int(a[i])+int(b[i])+indx
            if(num==2):
                indx=1
                c=c+'0'
            elif(num==3):
                indx=1
                c=c+'1'
            else:
                indx=0
                c=c+str(num)
            i-=1
        return c[::-1]