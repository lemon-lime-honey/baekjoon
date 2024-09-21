#include <iostream>

using namespace std;

int main() {
  int n;
  cin >> n;

  int a = 1, b = 1, c;

  for (int i = 3; i <= n; i++) {
    c = b;
    b = (a + b) % 1000000007;
    a = c;
  }

  cout << b << " " << n - 2 << endl;
}