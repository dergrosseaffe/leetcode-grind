#include <functional>

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int rows = board.size();
        int cols = board[0].size();
        const vector<pair<int, int>> moves = {{-1,0}, {0, -1}, {0, 1}, {1, 0}};

        std::function<bool(int, int, int)> dfs;
        dfs = [&dfs, &board, &moves, &word, rows, cols] (int row, int col, int index) -> bool {
            if (word.size() == index)
                return true;
            if (row < 0 || row >= rows || col < 0 || col >= cols)
                return false;
            if (board[row][col] != word[index])
                return false;

            auto temp = board[row][col];
            board.at(row).at(col) = '#';

            bool found = false;
            for (const auto& [dx, dy] : moves) {
                found = found || dfs(row + dx, col + dy, index+1);
            }

            board.at(row).at(col) = temp;
            return found;
        };

        for (int row  = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (dfs(row, col, 0))
                    return true;
            }
        }

        return false;
    }
};
