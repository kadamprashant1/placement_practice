#include<bits/stdc++.h>
using namespace std;

// vector {1,,4,3,6,7,5}// k=3

int main(){
    vector<int> v1={1,2,4,3,6,7,5};
    make_heap(v1.begin(),v1.end());//Time Complexity: O(N)
    cout<<v1.front()<<endl;//Auxiliary Space: O(1)
    return 0;
}