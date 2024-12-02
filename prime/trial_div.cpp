#include <iostream>
#include <vector>
using namespace std;

vector<long long> trial(long long n) {
    vector<long long> s;

    while (n % 2LL == 0) {
        n = n / 2;
        s.push_back(2);
    }

    for (long long i = 3LL; i * i <= n; i += 2LL) {
        while (n % i == 0) {
            n = n / i;
            s.push_back(i);
        }
    }
    if (n > 2) {
        s.push_back(n);
    }
    return s;
}

int main() {
    long long x;
    cout << "Type a number: ";
    cin >> x;
    vector<long long> b = trial(x);
    for (long long factor : b) {
        cout << factor << " ";
    }
    cout << endl;

    return 0;
}
