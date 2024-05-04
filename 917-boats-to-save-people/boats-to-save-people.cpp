class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        int len=people.size();
        int ans=0;
        int p0=0;
        int p1=len-1;

        while(p0<=p1){
            
          if(people[p0]+people[p1]<=limit){
            ans++;
            p0++;
          }else{
            ans++;
          }
          p1--;

        }
        return ans;
    }
};