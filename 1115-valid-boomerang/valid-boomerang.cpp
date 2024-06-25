class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
        float grad_2_3=101,grad_1_2=101,grad_1_3=101;
        if(points[2][0]-points[1][0]!=0)
            grad_2_3=(float)(points[2][1]-points[1][1])/(points[2][0]-points[1][0]);
        if(points[1][0]-points[0][0]!=0)
            grad_1_2=(float)(points[1][1]-points[0][1])/(points[1][0]-points[0][0]);
        if(points[2][0]-points[0][0]!=0)
            grad_1_3=(float)(points[2][1]-points[0][1])/(points[2][0]-points[0][0]);
        
          cout<<"1-2:"<<grad_1_2<<endl;
        cout<<"1-3:"<<grad_1_3<<endl;
        cout<<"2-3:"<<grad_2_3<<endl;
        if(grad_2_3!=grad_1_2&&grad_2_3!=grad_1_3&&grad_1_3!=grad_2_3&&grad_1_3!=grad_1_2){
            return true;
        }
      

        return false;
    }
};