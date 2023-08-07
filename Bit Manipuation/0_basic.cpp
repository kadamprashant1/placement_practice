#include <iostream>
using namespace std;

void getBit(int n, int pos){//it checks given pos= 2 have which bit 0 or 1
    cout<<((n & (1<<pos))!=0 )<<endl;//so here i<<2 gives 0100 and 5 i.e. gives 0101
    //n & (1<<pos ) gives 0100 and it not equla to zero it return 1

}

 void setBit(int n, int pos){// it will set the bit at required position
 //here we will perform or and set the bit 
  cout<<( n | (1<<pos)) <<endl;

 }

 void clearBit(int n, int pos){ // it will clear the bit at given position
 //her we will perform shift operator and then take ~ of it
    int mask = ~(1<<pos);
    cout<<(n & mask)<<endl;


 }

  void updateBit(int n, int pos, int value){  // here we wil first clear the bit and then set opration on it
    int mask = ~(1<<pos);
    n =n & mask;
    cout<< (n | (value<<pos) )<<endl;


  } 

int main (){
// getBit(5,2);
// setBit(5,1);
// clearBit(5,2);
updateBit(5,1,1);

return 0;
}