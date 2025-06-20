class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        max_dist=0
        N_count=S_count=W_count=E_count=0
        for i,move in enumerate(s):
            if(move=='N'):N_count+=1
            elif move=='S':S_count+=1
            elif move=='W':W_count+=1
            else:E_count+=1

            l=i+1
            min_pairs=min(N_count,S_count)+min(E_count,W_count)

            curr_dist=0
            if(k>=min_pairs):
                curr_dist=l
            else:
                base_dist=l-2*min_pairs
                curr_dist=base_dist+2*k

            max_dist=max(curr_dist,max_dist)
        return max_dist

        

