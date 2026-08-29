#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    int idx = 0;
    int val = arr.at(0);
    
    for (int i = 0; i < arr.size(); i++) {
        if (arr.at(i) < val) {
            idx = i;
            val = arr.at(i);
        }
    }
    
    arr.erase(arr.begin() + idx);
    
    if (arr.empty()) {
        arr.emplace_back(-1);
    }

    return arr;
}