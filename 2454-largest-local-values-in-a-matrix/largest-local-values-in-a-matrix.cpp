class Solution {
public:

    int find_max(vector<vector<int>>&grid,int &a , int &b){
        int max=0;
        for(int r=a;r<=a+2;r++){
            for(int c=b;c<=b+2;c++){
                if(grid[r][c]>max){
                    max=grid[r][c];
                }
            }
        }
        return max;
    }
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int rows=grid.size();
        int cols=grid[0].size();
        vector<vector<int>> maxLocal(rows-2,vector<int>(cols-2));
        int max=0;

        for(int r=0;r<rows-2;r++){
            for(int c=0;c<cols-2;c++){
                maxLocal[r][c]=find_max(grid,r,c);
            }
        }
        return maxLocal;
    }

};