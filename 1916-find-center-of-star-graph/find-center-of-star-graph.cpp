class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        set<int> numbers;
        for(int i=0;i<=1;i++){
            for(int j=0;j<=1;j++){
                auto result=numbers.insert(edges[i][j]);
                if (!result.second){//if in the set
                    return edges[i][j];
                }
            }
        }
        


        return 0;
    }
};