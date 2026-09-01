#include <string>
#include <stack>

using namespace std;

bool solution(string s) {
    stack<char> st;
    
    for (auto ch = s.begin(); ch != s.end(); ch++) {
        if (st.empty()) {
            if (*ch == ')') return false;
            st.push(*ch);
        } else {
            if (*ch == '(') st.push(*ch);
            else if (st.top() == '(') st.pop();
            else return false;
        }
    }
    
    return st.size() == 0;
}