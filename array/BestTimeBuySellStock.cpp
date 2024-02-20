#include <limits>

class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int minPrice  = std::numeric_limits<int>::max();
        int maxPrice  = 0;
        int maxProfit = 0;

        for (int i = 0; i < prices.size(); i++) {
            minPrice = std::min(minPrice, prices[i]);
            maxProfit = std::max(maxProfit, prices[i] - minPrice);
        }

        return maxProfit;
    }
};
