#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Recursive DFS utility function
void dfs_recursive(int node, vector<int> adj[], vector<int>& vis, vector<int>& dfs_result) {
    vis[node] = 1;
    dfs_result.push_back(node);

    for (int x : adj[node]) {
        if (vis[x] == 0) {
            dfs_recursive(x, adj, vis, dfs_result);
        }
    }
}

// DFS wrapper function
void dfs(vector<int> adj[], int n) {
    vector<int> vis(n + 1, 0);
    vector<int> dfs_result;

    dfs_recursive(1, adj, vis, dfs_result);  // Start from node 1

    cout << "DFS Traversal: ";
    for (int node : dfs_result) {
        cout << node << " ";
    }
    cout << endl;
}

// Recursive BFS utility function
void bfs_recursive(queue<int>& q, vector<int>& vis, vector<int>& bfs_result, vector<int> adj[]) {
    if (q.empty()) return;

    int node = q.front();
    q.pop();
    bfs_result.push_back(node);

    for (int x : adj[node]) {
        if (vis[x] == 0) {
            vis[x] = 1;
            q.push(x);
        }
    }

    bfs_recursive(q, vis, bfs_result, adj);
}

// BFS wrapper function
void bfs(vector<int> adj[], int n) {
    vector<int> vis(n + 1, 0);
    queue<int> q;
    vector<int> bfs_result;

    vis[1] = 1;
    q.push(1);

    bfs_recursive(q, vis, bfs_result, adj);

    cout << "BFS Traversal: ";
    for (int i = 0; i < bfs_result.size(); i++) {
        cout << bfs_result[i] << " ";
    }
    cout << endl;
}

int main() {
    int n, m;
    cout << "Give inputs nodes and edges: ";
    cin >> n >> m;

    vector<int> adj[n + 1];

    cout << "Enter " << m << " edges (v u):\n";
    for (int i = 1; i <= m; i++) {
        int v, u;
        cin >> v >> u;
        adj[v].push_back(u);
        adj[u].push_back(v); // undirected
    }

    bfs(adj, n);
    dfs(adj, n);

    return 0;
}
