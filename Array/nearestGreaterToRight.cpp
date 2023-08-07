#include <bits/stdc++.h>
using namespace std;
void solution(int a[5], int n){
    stack<int> s;
    cout<<a[n]<<endl;
    s.push(a[n]);
    //O(n) time complexity wala code for it using stack
    for(int i=n; i<=4;i++){
            if(s.top()<a[i]){
                s.pop();
                s.push(a[i]);
            }
    }
    cout<<"Greater To RIght "<<s.top()<<endl;
}


int main(){
    int n=1;
    int array[5]={1,5,6,2,7};//array
   solution(array,n);
}