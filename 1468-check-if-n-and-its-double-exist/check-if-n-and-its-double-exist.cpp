class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        for (int i=0;i<arr.size();i++){
            for(int j=i+1;j<arr.size();j++){
                if (arr[i]==2*arr[j]||arr[j]==2*arr[i])
                    return 1;
            }
        }

        return 0;
    }
};