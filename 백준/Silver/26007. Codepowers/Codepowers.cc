#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  int n, m, k, x, a, l, r;

  ostringstream oss;

  scanf("%d %d %d %d", &n, &m, &k, &x);

  int cnt[n + 1];
  cnt[0] = 0;

  for (int i = 1; i < n + 1; i++) {
    scanf("%d", &a);
    x += a;
    cnt[i] = cnt[i - 1];
    if (x < k) cnt[i]++;
  }

  for (int i = 0; i < m; i++) {
    scanf("%d %d", &l, &r);
    oss << cnt[r - 1] - cnt[l - 1] << "\n";
  }

  printf("%s", oss.str().c_str());
}