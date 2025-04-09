class Solution(object):
    def groupAnagrams(self, strs):
        dictn={}
        for s in strs:
            sorted_str=''.join(sorted(s))
            if(sorted_str  not in dictn):
                dictn[sorted_str]=[]
            dictn[sorted_str].append(s)
        l=[]
        for i in dictn:
            l.append(dictn[i])
        return l


        

        