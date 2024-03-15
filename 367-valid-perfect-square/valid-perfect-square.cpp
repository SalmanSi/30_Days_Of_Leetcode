class Solution {
public:
    bool isPerfectSquare(int num) {
        long int root=num;
        while(root*root>num){
            root/=2;
        }
        
        long int upper_limit=root*root;
        if(root==num){
            return true;
        }
        while(root<upper_limit){
            if(root*root==num)
                return true;
            root+=1;
        }
        return false;

    }
};