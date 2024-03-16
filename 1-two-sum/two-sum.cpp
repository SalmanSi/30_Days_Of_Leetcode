class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indices;
        map<int,int> complements;//complemnt:index
        for(int i=0;i<nums.size();i++){
            if(complements.find(nums[i])!=complements.end())//it exists
            {
                indices.push_back(complements[nums[i]]);
                indices.push_back(i);
                return indices;
            }
            else{//not found
                complements[target-nums[i]]=i;
            }
            }
       
        
        return indices; 
        }
    };
