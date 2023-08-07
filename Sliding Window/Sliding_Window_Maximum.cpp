#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int k;
    int size=nums.size();
    int i=0,j=0, sum=0;
    vector<int> ans;
    for(i=0; i<size-k+1; i++){
        int maxsum=INT_MIN;
        for(j=i; j<i+k;j++){
            maxsum=max(maxsum,nums[j]);
        }
        ans.push_back(maxsum);
    }
    cout<<ans.size()<<endl;
    return 0;
}