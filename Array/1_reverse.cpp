#include <bits/stdc++.h>
using namespace std;

void revstr(string& str){
    int s=str.length();
    for(int i=0; i<s/2; i++){
        swap(str[i],str[s-i-1]);
    }
}

 int main(){
    string str ="Prashant";
    revstr(str);
    cout<< str;
    return 0;
 }