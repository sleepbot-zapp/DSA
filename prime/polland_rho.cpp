#include <iostream>
#include <vector>
#include <chrono>
using namespace std;

vector<long long> polland(int n){
    vector<long long> t;
    if (n == 2)
        t.push_back(2);
    if (n == 3) 
        t.push_back(3);
    std::srand(std::time(0));
    long long random_num = std::rand() % (n - 1) + 1;
    
}


int main() {
    long long x;
    cout << "Type a number: ";
    cin >> x;
    vector<long long> t = polland(x);
    for (long long factor : t) {
        cout << factor << " ";
    }
    cout << endl;
    return 0;
}
