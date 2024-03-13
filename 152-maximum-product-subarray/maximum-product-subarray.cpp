class Solution {
public:
    int maxProduct(vector<int>& nums) {
       int res=nums[0];
       int len=nums.size();
       int max_prd;
       int cur_prd;
       for(int i=0;i<len;i++){
        max_prd=nums[i];
        cur_prd=nums[i];

        for(int j=i+1;j<len;j++){
            cur_prd*=nums[j];
            if(cur_prd>max_prd){
                max_prd=cur_prd;
            }
        }
        if(max_prd>res){
            res=max_prd;
        }

       }
      
       return   res;
    }
};