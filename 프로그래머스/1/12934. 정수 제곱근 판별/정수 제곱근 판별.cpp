#include <cmath>

using namespace std;

long long solution(long long n) {
    long long chk = sqrt(n);
    
    if (pow(chk, 2) == n) {
        return (chk + 1) * (chk + 1);
    }
    
    return -1;
}