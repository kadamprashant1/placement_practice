#include <bits/stdc++.h>
using namespace std;
const int N = 1e3;
int graph1[N][N];

vector<int> graph2[N];

int main(){
    int n,m ;
    cin>>n>>m;
    for (int i=0; i<m; ++i){
        int v1, v2;
        cin>>v1>>v2;
        //adj matrix 
        // O(N^2) - space complexity
        
        graph1[v1][v2]=1;// for adj matrix
        graph1[v2][v1]=1;// for adj matrix

        //adj list
        //O( V + E) - space complexity
        graph2[v1].push_back(v2);// for adj list
        graph2[v2].push_back(v1);// for adj list

    }
}