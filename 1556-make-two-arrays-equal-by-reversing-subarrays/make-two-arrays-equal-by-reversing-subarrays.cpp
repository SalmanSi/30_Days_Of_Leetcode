class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        map<int,int> freq_count;
        for(auto num : target){
            if(freq_count.find(num)==freq_count.end()){
                freq_count[num]=1;
            }else{
                freq_count[num]++;
            }
        }

        for (auto num:arr){
            if(freq_count.find(num)==freq_count.end()){
                return false;
            }
            else if (freq_count[num]>0){
                freq_count[num]--;
            }else{
                return false;
            }
        }

        for(const auto &pair:freq_count){
            if(pair.second>0 || pair.second<0){
                return false;
            }
        }
        return true;
    }
};