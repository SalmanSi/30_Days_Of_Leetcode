class Solution {
public:
    static bool compare(const vector<int>&a,const vector<int>&b){
        return a[0]<b[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end(),compare);
        vector<vector<int>> merged;
        merged.push_back(intervals[0]);
        int len=intervals.size();
        cout<<len;
        for(int i=1;i<len;i++){
            if(merged.back()[1]>=intervals[i][0]){
                if(merged.back()[1]>=intervals[i][1]){
                    continue;
                }else{
                merged.back()[1]=intervals[i][1];}
            }else{
                merged.push_back(intervals[i]);
            }

        }

        return merged;
    }
};