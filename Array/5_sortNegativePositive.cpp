#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v1={-12, 11, -13, -5, 6, -7, 5, -3, -6};
    for(int i=0; i<v1.size(); i++){
        if(v1[i]<0){
            cout<<v1[i]<<" ";
        }
    }
    for(int i=0; i<v1.size(); i++){
        if(v1[i]>=0){
            cout<<v1[i]<<" ";
        }
    }

    return 0;
}