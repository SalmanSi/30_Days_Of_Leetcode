class Solution {
public:
    int findMin(vector<int>& nums) {
        int s=0;
        int e=nums.size()-1;
        int mid;
        while(s<e-1){
            mid=s+(e-s)/2;
            if(nums[s]<nums[mid]&&nums[mid]<nums[e]){
                e=mid;
                continue;
            }
            if(nums[s]<nums[mid]&&nums[mid]>nums[e]){
                s=mid;
                continue;
            }
            if(nums[s]>nums[mid]&&nums[mid]<nums[e]){
                if(nums[s]>nums[e]){
                    e=mid;
                }else{
                    s=mid;
                }
            }
            if(nums[s]>nums[mid]&&nums[mid]>nums[e]){
                s=mid;
                continue;
            }

        }
        if(nums[s]<nums[e]){
            cout<<"e= "<<nums[e];
            return nums[s];
        }else{
            return nums[e];
        }
    }
};