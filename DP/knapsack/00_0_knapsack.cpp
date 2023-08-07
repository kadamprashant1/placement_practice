#include<bits/stdc++.h>
using namespace std;

int knapsack(int val[], int wt[], int weight, int n){
    if( n ==0 || weight ==0) return 0;

    if( wt[n-1] <= weight){
        return max(val[n-1] + knapsack(val , wt, weight - wt[n-1],n-1), knapsack( val, wt, weight, n-1));

    }
    else{
        return knapsack(val,wt,weight, n-1);
    }


    return n;
}

int main(){
    int profit[] = { 60, 100, 120 };
    int weight[] = { 10, 20, 30 };
    int W = 50;
    int n = sizeof(profit) / sizeof(profit[0]);
    int ans = knapsack(profit, weight, W, n);
    cout<<"max profit is : "<< ans <<endl;
    return 0;
}