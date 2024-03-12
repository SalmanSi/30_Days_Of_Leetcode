class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy_ptr,sell_ptr;
        int len=prices.size();
        if(len==1){
            return 0;//cant sell 
        }

        buy_ptr=0;
        sell_ptr=1;
        int min_ptr=0;
        for(int i=1;i<len;i++){
            if(prices[min_ptr]>prices[i]){
                min_ptr=i;
                continue;
            }
            if(prices[i]-prices[min_ptr]>prices[sell_ptr]-prices[buy_ptr]){
                buy_ptr=min_ptr;
                sell_ptr=i;
            }
        }
        int profit;
        profit=prices[sell_ptr]-prices[buy_ptr];
        if(profit<0){
            return 0;
        }
        return profit;
    }
};