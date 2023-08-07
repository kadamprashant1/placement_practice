
#include<bits/stdc++.h>
using namespace std;


int main(){
    vector<int> v1={0,2,1,2,0};
    map<int,int> m;
    for(int i=0;i<v1.size();i++){
        m[v1[i]]++;
    }   
    map<int,int> :: iterator it;
    for(it=m.begin();it!=m.end();it++){
        for(int i=0; i<(*it).second;i++){
        cout<<(*it).first<<" ";
        }
    }
    
    return 0;
}