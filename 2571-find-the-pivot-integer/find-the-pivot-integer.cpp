class Solution {
public:
    int pivotInteger(int n) {
        int sum_start=1;
        int sum_end=n;
        int s=1,e=n;
        while(s<e){
            if(sum_end>sum_start){
                s++;
                sum_start+=s;
                continue;
            }
            if(sum_start>sum_end){
                e--;
                sum_end+=e;
                continue;
            }
        }

        if(sum_start==sum_end){
            return s;
        }
        cout<<"start: "<<sum_start<<endl;
        cout<<"end: "<<sum_end<<endl;
        return -1;
    }
};