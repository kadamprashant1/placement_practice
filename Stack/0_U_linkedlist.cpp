#include <bits/stdc++.h>
using namespace std;

class Node{
    public:
        int data;
        Node* link;

        Node(int n){
            this->data=n;
            this->link=NULL;
        }
};
class Stack{
    Node* top;
    public:
    stack(){
        top=NULL;
    }

    void push(int data){
        Node* temp= new Node(data);

        if(!temp){
            cout<<"stack is overflow"<<endl;
            exit(1);
        }
        temp->data=data;
        temp->link = top;
        top= temp;
    }
    void pop(){
        Node* temp;
        if(isEmpty()){
            cout<<"stack is underflow "<<endl;
            exit(1);
        }
        else{
            temp =top;
            top=temp->link;
            free(temp);
        }
    }

    bool isEmpty(){
        return top==NULL;
    }
    int peek(){
        if( !isEmpty())
            return top->data;
        
        else
            exit(1);
        
    }

    void display(){
        Node* temp;
        if(top==NULL){
            cout<<"stack is underflow"<<endl;
            exit(1);
        }
        else{
            temp =top;
            while (temp!=NULL){
                cout<<temp->data;
                temp=temp->link;
                if(temp!= NULL){
                    cout<<"->";
                }
                cout<<endl;
            }
            
            
        }


    }
};
int main(){
    Stack s;
    s.push(11);
    s.push(22);
    s.push(33);
    s.push(44);
    s.push(55);
    //s.display();
    //cout<<"top of stack"<<endl;
    //cout<< s.peek() <<endl;
    //s.pop();
    s.display();

    return 0;
}