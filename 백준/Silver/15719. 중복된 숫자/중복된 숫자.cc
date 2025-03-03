#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  long long n, sum, num;

  sum = 0;
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> num;
    sum += num;
    sum -= i;
  }

  cout << sum;

  return 0;
}