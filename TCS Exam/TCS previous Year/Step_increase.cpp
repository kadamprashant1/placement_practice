// right +10
// up -20
// left -30
// down -40
// right 50

// continue

// code

#include <iostream>
using namespace std;

void fun_tion(int input){
    char c = 'a';
    int distance =10;
    int x=0, y=0;
    int i=0;
    while(input){
        switch(c){
            case 'a':
            x+=distance;
            
            c = 'b';
            break;
            
            case 'b':
            y += distance;
            
            c='c';
            break;
            
            case 'c':
            x -= distance;
            c ='d';
            break;
            
            case 'd':
            y-= distance;
            c = 'e';
            break;
            
            case 'e':
            x+= distance;
            c='a';
            break;
        }
        distance += 10;
        input--;
    }
    
    cout<<x<<" "<<y<<endl;
}
int main(){
    int input;
    cin>>input;
    fun_tion(input);
    return 0;
}