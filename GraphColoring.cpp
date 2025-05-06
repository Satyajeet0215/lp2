#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> adjList;

bool isSafe(int node, int colorToAssign, const vector<int>& colors) {
    for (int neighbor : adjList[node]) {
        if (colors[neighbor] == colorToAssign)
            return false;
    }
    return true;
}

bool solve(int node, int m, int n, vector<int>& colors) {
    if (node == n) return true;

    for (int color = 1; color <= m; color++) {
        if (isSafe(node, color, colors)) {
            colors[node] = color;
            if (solve(node + 1, m, n, colors)) return true;
            colors[node] = 0; // Backtrack
        }
    }
    return false;
}

int main() {
    int n, m_edges;
    cout << "Give inputs n and m: ";
    cin >> n >> m_edges;

    adjList.resize(n); // Use 0-based indexing

    cout << "Enter " << m_edges << " edges (v u):\n";
    for (int i = 0; i < m_edges; ++i) {
        int u, v;
        cin >> u >> v;
        adjList[u].push_back(v);
        adjList[v].push_back(u); // Undirected
    }

    int m_colors;
    cout << "Enter number of colors: ";
    cin >> m_colors;

    vector<int> colors(n, 0); // Initially all nodes uncolored

    if (solve(0, m_colors, n, colors)) {
        cout << "\nGraph can be colored with " << m_colors << " colors:\n";
        for (int i = 0; i < n; i++) {
            cout << "Node " << i << " ---> Color " << colors[i] << endl;
        }
    } else {
        cout << "\nGraph cannot be colored with " << m_colors << " colors.\n";
    }

    return 0;
}
