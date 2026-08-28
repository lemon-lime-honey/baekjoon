#include <cmath>

using namespace std;

int solution(int n) {
    if (n < 8) {
        return 1;
    }
    
    return ceil((float)n / 7);
}