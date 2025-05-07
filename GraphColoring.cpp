#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> adjList;
int totalSolutions = 0;
bool foundFirstSolution = false;
vector<int> firstSolution;

bool isSafe(int node, int colorToAssign, const vector<int>& colors) {
    for (int neighbor : adjList[node]) {
        if (colors[neighbor] == colorToAssign)
            return false;
    }
    return true;
}

void solve(int node, int m, int n, vector<int>& colors) {
    if (node == n) {
        totalSolutions++;
        if (!foundFirstSolution) {
            firstSolution = colors;
            foundFirstSolution = true;
        }
        return;
    }

    for (int color = 1; color <= m; color++) {
        if (isSafe(node, color, colors)) {
            colors[node] = color;        // Assign color
            solve(node + 1, m, n, colors);
            colors[node] = 0;            // Backtrack
        }
    }
}

int main() {
    int n, m_edges;
    cout << "Enter number of nodes and number of edges: ";
    cin >> n >> m_edges;

    adjList.assign(n, vector<int>());

    cout << "Enter " << m_edges << " edges (0-based index: u v):\n";
    for (int i = 0; i < m_edges; ++i) {
        int u, v;
        cin >> u >> v;
        if (u >= 0 && u < n && v >= 0 && v < n) {
            adjList[u].push_back(v);
            adjList[v].push_back(u);
        } else {
            cout << "Invalid edge: (" << u << ", " << v << "). Skipping.\n";
        }
    }

    int m_colors;
    cout << "Enter number of colors: ";
    cin >> m_colors;

    vector<int> colors(n, 0);

    solve(0, m_colors, n, colors);

    if (totalSolutions == 0) {
        cout << "\nGraph cannot be colored with " << m_colors << " colors.\n";
    } else {
        cout << "\nTotal number of valid colorings: " << totalSolutions << endl;
        cout << "One valid coloring:\n";
        for (int i = 0; i < n; i++) {
            cout << "Node " << i << " -> Color " << firstSolution[i] << endl;
        }
    }

    return 0;
}
