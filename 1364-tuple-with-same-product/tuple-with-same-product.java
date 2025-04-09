import java.util.*;
class Solution {
    public int tupleSameProduct(int[] nums) {
        Map<Integer, List<int[]>> product = new HashMap<>();
        int n=nums.length;

        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int pro=nums[i] * nums[j];
                product.putIfAbsent(pro,new ArrayList<>());
                product.get(pro).add(new int[]{nums[i],nums[j]});
            }
        }
        int count=0;
        for (List<int[]> pairs : product.values()) {
            int k = pairs.size();
            if (k > 1) {
                count += k * (k - 1) * 4;  // Each pair combination gives 8 valid tuples
            }
        }

        return count;
        
    }
}