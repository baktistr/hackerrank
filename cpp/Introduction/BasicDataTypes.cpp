// https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem

#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

int main() {
    // Complete the code.
    int a;
    long b;
    char c;
    float d;
    double e;
    cin >> a >> b >> c >> d >> e;
    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    
    std::cout << std::fixed << std::setprecision(3) << d << endl;
    std::cout << std::fixed << std::setprecision(9) << e << endl;
    return 0;
}
