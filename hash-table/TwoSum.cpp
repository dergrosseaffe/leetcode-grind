class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> complements;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (complements.find(complement) != complements.end()) {
                return {i, complements[complement]};
            }

            complements[nums[i]] = i;
        }

        return {};
    }
};
