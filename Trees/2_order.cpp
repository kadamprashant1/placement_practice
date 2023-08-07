#include<bits/stdc++.h>
using namespace std;

struct node{
    int data;
    struct node* left;
    struct node* right;

    node(int val){
        data=val;
        left=NULL;
        right=NULL;
    }  
};

void preorder(struct node* root){
    if(root==NULL) return;
    cout<<root->data<<" ";
    preorder(root->left);
    preorder(root->right);

}

void inorder(struct node* root){
    if(root==NULL) return;
    preorder(root->left);
    cout<<root->data<<" ";
    preorder(root->right);
}
void postorder(struct node* root){
    if(root==NULL) return;
    preorder(root->left);
    preorder(root->right);
    cout<<root->data<<" ";
}

int main(){
    struct node* root= new node(1);
    root->left=new node(2);
    root->right=new node(3);
    root->left->left=new node(4);
    root->right->right=new node(5);
    root->left->right=new node(6);
    root->right->left= new node(7);
    cout<<"preorder"<<endl;
    preorder(root);
    cout<<"\ninorder"<<endl;
    inorder(root);
    cout<<"postorder"<<endl;
    postorder(root);
    
    return 0;
}