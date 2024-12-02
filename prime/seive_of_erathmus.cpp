#include <iostream>
#include <vector>
using namespace std;

vector<long long> seive(long long n) {
    vector<bool> s(n + 1, true);
    s[0] = s[1] = false;

    for (long long i = 2LL; i * i <= n; i++) {
        if (s[i]) {
            for (long long j = i * i; j <= n; j += i) {
                s[j] = false;
            }
        }
    }
    vector<long long> t;
    for (long long i = 2LL; i <= s.size(); i++) {
        if (s[i] && n % i == 0) {
            t.push_back(i);
        }
    }
    return t;
}

int main() {
    long long x;
    cout << "Type a number: ";
    cin >> x;
    vector<long long> t = seive(x);
    for (long long factor : t) {
        cout << factor << " ";
    }
    cout << endl;
    return 0;
}
