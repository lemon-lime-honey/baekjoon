#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    vector<int> num;
    int idx = 0;
    
    while (n != 0) {
        num.emplace_back(n % 3);
        n /= 3;
    }
    
    while (!num.empty()) {
        n += num.back() * pow(3, idx);
        num.pop_back();
        idx++;
    }
    
    return n;
}