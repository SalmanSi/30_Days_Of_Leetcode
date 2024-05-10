class Solution {
public:
    static bool compare(const vector<int> &a, vector<int> &b){
        return ((double)a[0]/a[1])<((double)b[0]/b[1]);
    }
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int len=arr.size();
        vector<vector<int>> ratio;
        for(int i=0;i<len;i++){
            for(int j=i+1;j<len;j++){
                ratio.push_back({arr[i],arr[j]});
            }
        }
        sort(ratio.begin(),ratio.end(),compare);
        return ratio[k-1];
    }
};