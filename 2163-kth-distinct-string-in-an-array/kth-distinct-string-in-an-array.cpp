class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        map<string,int> freq_count;
        
        for (const auto& word:arr){
            freq_count[word]++;
        }
        int j=1;
        for (const auto& word:arr){
            if (freq_count[word]==1){
                if (k==j){
                    return word;
                }
                j++;
            }
        }

        return "";
    }
};