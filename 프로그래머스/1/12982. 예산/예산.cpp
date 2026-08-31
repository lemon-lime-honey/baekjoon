#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> d, int budget) {
    sort(d.begin(), d.end());
    int answer = 0;
    
    for (auto i = d.begin(); i != d.end(); i++) {
        if (*i > budget) break;
        budget -= *i;
        answer++;
    }
    
    return answer;
}