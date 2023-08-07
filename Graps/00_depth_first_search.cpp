#include <bits/stdc++.h>
using namespace std;
const int N = 1e3 + 10;

vector<int> g[N];
bool visited[N];

void dfs(int vertex) {
    // action on vertex after entering vertex
    visited[vertex] = true;
    for (int child : g[vertex]) {
        cout<<" par " <<vertex<<", child "<<child<<endl;
        // take action on child before entering the child
        if (visited[child]) continue;
        dfs(child);
        // take action on child after exiting child node
    }
    // take action on vertex before exiting the vertex
}

// call + total complexity
// O(v times call + edges)
int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        int v1, v2;
        cin >> v1 >> v2;
        g[v1].push_back(v2);
        g[v2].push_back(v1);
    }
    dfs(1);
    return 0;
}
