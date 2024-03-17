class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        int len = nums.size();
        int conjugate;
        int s, e;
        vector<int> res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < len; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            // now i is not repeated
            conjugate = -nums[i];
            // now two sum
            s = i + 1;
            e = len - 1;

            while (s < e) {

                if (nums[s] + nums[e] < conjugate) {
                    s++;
                } else if (nums[s] + nums[e] > conjugate) {
                    e--;
                } else {

                    res.push_back(-conjugate);
                    res.push_back(nums[s]);
                    res.push_back(nums[e]);
                    result.push_back(res);
                    res.clear();

                    // Avoid duplicates
                    while (s < e && nums[s] == nums[s + 1]) {
                        s++;
                    }
                    while (s < e && nums[e] == nums[e - 1]) {
                        e--;
                    }

                    s++;
                    e--;
                }
            }
        }

        return result;
    }
};