class Solution {
public:
    bool isPalindrome(int x) {
        int temp=x;
        long long int reverse=0;
        if(x<0){
            return 0;
        }
        long long int i=1;
        while(temp>=10){
            i*=10;
            temp/=10;
        }
        cout<<"digs: "<<i<<endl;
        for(temp=x;temp>0;i/=10){
            reverse=reverse+(temp%10)*i;
            cout<<reverse<<endl;
            temp=temp/10;
        }
        
        if(reverse==x)
        {

            return 1;
        }
    return 0;
    }
};