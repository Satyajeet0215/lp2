#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Recursive DFS utility function
void dfs_recursive(int node, vector<int> adj[], vector<int>& vis, vector<int>& dfs_result) {
    vis[node] = 1;
    dfs_result.push_back(node);

    for (int x : adj[node]) {
        if (vis[x]==0) {
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

// BFS function
void bfs(vector<int> adj[], int n) {
    vector<int> vis(n + 1, 0);
    vis[1] = 1;
    queue<int> q;
    q.push(1);
    vector<int> bfs;

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        bfs.push_back(node);

        for (int x : adj[node]) {
            if (vis[x] == 0) {
                vis[x] = 1;
                q.push(x);
            }
        }
    }

    cout << "BFS Traversal: ";
    for (int i = 0; i < bfs.size(); i++) {
        cout << bfs[i] << " ";
    }
    cout << endl;
}

int main() {
    int n, m;
    cout << "Give inputs n and m: ";
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
