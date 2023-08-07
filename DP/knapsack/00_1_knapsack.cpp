#include<bits/stdc++.h>
using namespace std;

int t[4][51]; //t[value +1][weight +1];
int knapsack(int val[], int wt[], int weight, int n){
    if( n ==0 || weight ==0) return 0;

    if (t[n][weight] != -1){ 
        return t[n][weight];
    }
     

    if( wt[n-1] <= weight){
        t[n][weight]=max(val[n-1] + knapsack(val , wt, weight - wt[n-1],n-1), knapsack( val, wt, weight, n-1));
        return t[n][weight] ;
    }
    else{
        t[n][weight]=knapsack(val,wt,weight, n-1);
        return t[n][weight] ;
    }


}

int main(){
    int profit[] = { 60, 100, 120 };
    int weight[] = { 10, 20, 30 };
    int W = 50;
    int n = sizeof(profit) / sizeof(profit[0]);
    memset(t,-1,sizeof(t)); // intialization

    int ans = knapsack(profit, weight, W, n);
    cout<<"max profit is : "<< ans <<endl;
    return 0;
}