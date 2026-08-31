#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int n;
    int m;
    cin >> n >> m;
    
    string target = string(n, '*');
    
    for (int i = 0; i < m; i++) {
        cout << target << endl;
    }
    
    return 0;
}