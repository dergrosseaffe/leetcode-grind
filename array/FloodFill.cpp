class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int rows = image.size();
        int cols = image[0].size();
        const vector<pair<int, int>> moves = {{-1,0}, {0, -1}, {0, 1}, {1, 0}};

        std::function<void(int, int, int)> dfs;
        dfs = [&dfs, &image, &moves, rows, cols, color] (int row, int col, int scolor) -> void {
            if (row < 0 || row >= rows || col < 0 || col >= cols) return;
            if (image[row][col] == scolor) {
                image[row][col] = color;
                for (const auto& [dx, dy] : moves) {
                    dfs(row + dx, col + dy, scolor);
                }
            }
        };

        auto scolor = image[sr][sc];
        if (scolor != color)
            dfs(sr, sc, scolor);

        return image;
    }
};
