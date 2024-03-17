class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        vector<int>row;

        for(int i=1;i<=numRows;i++){
            for(int j=0;j<i;j++){
                if(j==0||j==i-1){
                    row.push_back(1);
                }else{
                    row.push_back(result[i-2][j-1]+result[i-2][j]);
                }
               
            }
            result.push_back(row);
            row.clear();
        }
        return result;
    }
};