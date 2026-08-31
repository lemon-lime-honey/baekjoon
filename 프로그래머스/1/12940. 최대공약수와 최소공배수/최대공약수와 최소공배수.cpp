#include <vector>

using namespace std;

int get_gcd(int n, int m) {
    while (true) {
        if (n % m == 0) break;
        int temp = n % m;
        n = m;
        m = temp;
    }
    
    return m;
}

vector<int> solution(int n, int m) {
    vector<int> answer;
    int gcd = get_gcd(max(n, m), min(n, m));
    
    answer.emplace_back(gcd);
    answer.emplace_back(n * m / gcd);
    
    return answer;
}