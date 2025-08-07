#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  int n, m;
  long long x, y, z, r;

  ostringstream oss;

  scanf("%d", &n);

  long long points[n][3];

  for (int i = 0; i < n; i++) {
    scanf("%lld %lld %lld", &points[i][0], &points[i][1], &points[i][2]);
  }

  scanf("%d", &m);

  for (int i = 0; i < m; i++) {
    scanf("%lld %lld %lld %lld", &x, &y, &z, &r);
    int result = 0;

    for (int j = 0; j < n; j++) {
      if ((points[j][0] - x) * (points[j][0] - x) +
              (points[j][1] - y) * (points[j][1] - y) +
              (points[j][2] - z) * (points[j][2] - z) <=
          r * r) {
        result++;
      }
    }

    oss << result << "\n";
  }

  printf("%s", oss.str().c_str());
}