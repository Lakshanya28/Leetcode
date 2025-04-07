class Solution(object):
    def romanToInt(self, s):
        roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        tot=0
        i=len(s)-1
        if(len(s)<2):tot=roman[s[0]]
        else:
            while (i>0 and len(s)>1):
                if(roman[s[i-1]]<roman[s[i]]):
                    tot+=(roman[s[i]]-roman[s[i-1]])
                    i-=1
                else:
                    tot+=roman[s[i]]
                i-=1
            if(roman[s[0]]>=roman[s[1]]):tot+=roman[s[0]]
        return tot

            
        