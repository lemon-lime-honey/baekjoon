#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int l = 0;
    int s = 0;
    
    for (auto sz = sizes.begin(); sz != sizes.end(); sz++) {
        auto ll = max_element((*sz).begin(), (*sz).end());
        auto ss = min_element((*sz).begin(), (*sz).end());
        
        if (l < *ll) l = *ll;
        if (s < *ss) s = *ss;
    }
    
    return l * s;
}