class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        map<string,int> freq_count;
        
        for (const auto& word:arr){
            freq_count[word]++;
        }
        int j=1;
        for (int i=0;i<arr.size();i++){
            if (freq_count[arr[i]]==1){
                if (k==j){
                    return arr[i];
                }
                j++;
            }
        }

        return "";
    }
};