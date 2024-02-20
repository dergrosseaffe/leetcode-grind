#include <unordered_map>

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        std::unordered_map<char, int> counter;

        for (auto c : magazine) {
            counter[c]++;
        }

        for (char c : ransomNote) {
            if (counter.find(c) == counter.end() || counter[c] == 0)
                return false;

            counter[c]--;
        }

        return true;
    }
};
