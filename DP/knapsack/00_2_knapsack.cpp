#include<bits/stdc++.h>
using namespace std;

int t[4][51];

int main(){
    int profit[] = { 60, 100, 120 };
    int weight[] = { 10, 20, 30 };
    int W = 50;
    int n = sizeof(profit) / sizeof(profit[0]);

    // Initialize
    for(int i=0; i<=n; i++){
        for(int j=0; j<=W; j++){
            if(i==0 || j==0){
                t[i][j] = 0;
            }
        }
    }
  
    for(int i=1; i<=n; i++){
        for(int j=1; j<=W; j++){
            if(weight[i-1] <= j){
                t[i][j] = max(profit[i-1] + t[i-1][j-weight[i-1]], t[i-1][j]);
            }
            else{
                t[i][j] = t[i-1][j];
            }
        }
    }
    cout << "Max profit is: " << t[n][W] << endl;
    return 0;
}
