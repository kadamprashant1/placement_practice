#include <iostream>
#include <queue>
#include <vector>
#include <climits>
using namespace std;

const int MAX = 15; 

struct Block {
    int row, col, distance, num2Blocks;

    Block(int r, int c, int d, int n) : row(r), col(c), distance(d), num2Blocks(n) {}
};

bool isValid(int row, int col, vector<vector<int>>& maze, vector<vector<bool>>& visited) {
    return (row >= 0 && row < maze.size() && col >= 0 && col < maze[0].size() && maze[row][col] != 1 && !visited[row][col] && maze[row][col] != 3);
}

int findShortestPath(vector<vector<int>>& maze, pair<int, int>& start, pair<int, int>& target) {
    int rows = maze.size();
    int cols = maze[0].size();

    vector<vector<bool>> visited(rows, vector<bool>(cols, false));

    int moves[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    queue<Block> q;

    q.push(Block(start.first, start.second, 0, 0));
    visited[start.first][start.second] = true;

    while (!q.empty()) {
        Block current = q.front();
        q.pop();

        if (current.row == target.first && current.col == target.second) {
            return current.distance;
        }

        for (int i = 0; i < 4; i++) {
            int newRow = current.row + moves[i][0];
            int newCol = current.col + moves[i][1];

            if (isValid(newRow, newCol, maze, visited)) {
      
                int newNum2Blocks = current.num2Blocks + (maze[newRow][newCol] == 2);

                if (newNum2Blocks <= 2) {
    
                    visited[newRow][newCol] = true;


                    q.push(Block(newRow, newCol, current.distance + 1, newNum2Blocks));
                }
            }
        }
    }


    return -1;
}

int main() {
    int rows, cols;
    cin >> rows >> cols;

    vector<vector<int>> maze(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> maze[i][j];
        }
    }

    pair<int, int> start;
    cin >> start.first >> start.second;

    pair<int, int> target;
    cin >> target.first >> target.second;


    int shortestPath = findShortestPath(maze, start, target);

    if (shortestPath != -1) {
        cout << shortestPath << endl;
    } else {
        cout << "STUCK" << endl;
    }

    return 0;
}