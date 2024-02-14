class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Boyer-Moore Voting Algorithm
   
        int current = 0;
        int currentCount = 0;
        for (int candidate : nums) {
            if (currentCount <= 0)
                current = candidate;
            currentCount += (candidate == current) ? 1 : -1;
        }

        return current;
    }
};