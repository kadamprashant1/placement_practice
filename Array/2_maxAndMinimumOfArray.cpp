#include <bits/stdc++.h>
using namespace std;
 
 //3, 5, 4, 1, 9
 int main(){
    int max, min;
    int arr[5]={3,5,4,1,9};
    sort(arr,arr+5);
    max=arr[4];
    min=arr[0];
    cout<<min<<" "<<max<<endl;
 }