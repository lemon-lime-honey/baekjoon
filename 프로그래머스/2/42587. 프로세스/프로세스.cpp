#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    priority_queue<pair<int, int>> pq;
    queue<pair<int, int>> que;
    int answer = 0;
    
    for (int i = 0; i < priorities.size(); i++) {
        pair<int, int> target = {priorities[i], i};
        que.push(target);
        pq.push(target);
    }
    
    while (!que.empty()) {
        pair<int, int> now = que.front();
        if (now.first < pq.top().first) {
            que.pop();
            que.push(now);
        } else {
            que.pop();
            pq.pop();
            answer++;
            if (now.second == location) return answer;
        }
    }
    
    return 0;
}