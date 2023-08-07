#include<bits/stdc++.h>
#include <iostream>
#include <climits>

using namespace std;

int maximum(int arr[], int n);
//N = 5
//Arr[] = {1,2,3,-2,5}
int main(){
    int n=5;
    int arr[n]={1,2,3,-2,5};
    int sum=0;
    int maxi=arr[0];
   
    for (int i = 0; i < 5; i++)
    {
        sum=sum+arr[i];
        maxi=max(maxi,sum);
        if(sum<0){
            sum=0;
        }
    }
    cout<<maxi<<endl;
    return 0;
}
