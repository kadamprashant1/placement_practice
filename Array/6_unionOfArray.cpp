#include<bits/stdc++.h>
using namespace std;
//85 25 1 32 54 6
//85 2 
int main(){
    vector<int> v1={85,25,1,32,54,6};
    vector<int> v2={85,2};
    map<int,int> mp;
    for (int i = 0; i < v1.size(); i++)
    {
        mp[v1[i]]++;
    }
    for (int i = 0; i <v2.size(); i++)
    {
        mp[v2[i]]++;
    }
    cout<<mp.size()<<endl;
    
    return 0;
}