class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        set<int> s ;
        vector<int> v ;
        int ind2=0;
        for (int i = 0; i < nums.size(); i++){
            if (s.count(target-nums[i])){
                ind2=i;
            }
            s.insert(nums[i]);
        }
        for (int i = 0; i < nums.size(); i++){
            if (nums[i]+nums[ind2] == target){
                
                return {i, ind2};
            }

        }
        return {0,0};
    }
};