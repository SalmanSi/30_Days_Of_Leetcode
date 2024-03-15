class Solution {
public:
    bool isPerfectSquare(int num) {
        int s=0;
        int e=num;
        long long int mid=s+(e-s)/2;
        while(s<=e){
            if((mid*mid)==num)
                {return true;}
            else if((mid*mid)<num)
                {s=mid+1;}
            else if((mid*mid)>num){
                e=mid-1;
            }
            mid=s+(e-s)/2;
        }
        return false;
    }
};