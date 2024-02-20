class Solution {
    int binary_search(vector<int>& nums, int target, int left, int right) {
        if (left > right) return -1;

        int middle = left + (right - left) / 2;
        if (nums[middle] == target)
            return middle;
        else if (nums[middle] > target)
            return binary_search(nums, target, left, middle - 1);
        else
            return binary_search(nums, target, middle + 1, right);
    }

public:
    int search(vector<int>& nums, int target) {
        return binary_search(nums, target, 0, nums.size() - 1);
    }
};
