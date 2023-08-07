#include <iostream>
#include <unordered_map>
using namespace std;


#wrong interpretation of code#


string countnsay(string s, int size) {
    unordered_map<char, int> unmap;
    string result;
    for (int i = 0; i < size; i++) {
        unmap[s[i]]++;
    }
    for (auto it : unmap) {
        result += to_string(it.second);
        result += it.first;
    }
    return result;
}

int main() {
    string s = "11222333";
    int size = s.size();
    cout << countnsay(s, size) << endl;
    return 0;
}
