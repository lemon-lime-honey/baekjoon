#include <string>
#include <queue>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    priority_queue<int> pq;
    int target = 0;

    while (n != 0) {
        pq.push(n % 10);
        n /= 10;
    }
    
    while (!pq.empty()) {
        target = pq.top();
        answer *= 10;
        answer += target;
        pq.pop();
    }
    
    return answer;
}