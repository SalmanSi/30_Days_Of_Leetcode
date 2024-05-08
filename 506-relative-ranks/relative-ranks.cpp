class Solution {
public:
    static bool compare(const pair<int,int> &a, const pair<int,int> &b){
        return a.second>b.second;
    }
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<string> ans(score.size());
        vector<pair<int,int>> score_i(score.size());
        for(int i=0;i<score.size();i++){
            score_i[i].first=i;
            score_i[i].second=score[i];
        }
        sort(score_i.begin(),score_i.end(),compare);

        for(int i=0;i<score.size();i++){
            cout<<"{ "<<score_i[i].first<<" , "<<score_i[i].second<<" }"<<endl;
            if(i==0){
                ans[score_i[i].first]="Gold Medal";
            }else if(i==1){
                ans[score_i[i].first]="Silver Medal";
            }else if(i==2){
                ans[score_i[i].first]="Bronze Medal";
            }else if(i>2){
            ans[score_i[i].first]=to_string(i+1);}

        }

        return ans;




    }
};