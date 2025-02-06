#include <cmath>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector<int> parent;

int _find(int p) {
  if (parent[p] != p) parent[p] = _find(parent[p]);
  return parent[p];
}

bool _union(int p, int q) {
  p = _find(p);
  q = _find(q);

  if (p == q) return false;

  if (p < q)
    parent[q] = p;
  else
    parent[p] = q;

  return true;
}

int main() {
  int n, c;
  vector<pair<int, int>> fields;
  priority_queue<pair<int, pair<int, int>>> pipes;
  long result = 0;
  int cnt = 0;

  scanf("%d %d", &n, &c);

  for (int i = 0; i < n; i++) {
    int x, y;
    scanf("%d %d", &x, &y);
    fields.push_back(make_pair(x, y));
  }

  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      long dist = pow(fields[i].first - fields[j].first, 2) +
                  pow(fields[i].second - fields[j].second, 2);
      if (dist < c) continue;
      pipes.push(make_pair(dist * -1, make_pair(i, j)));
    }
  }

  for (int i = 0; i < n; i++) {
    parent.push_back(i);
  }

  while (!pipes.empty()) {
    int p, q;
    long dist = pipes.top().first;

    p = pipes.top().second.first;
    q = pipes.top().second.second;

    pipes.pop();

    if (_union(p, q)) {
      result -= dist;
      cnt++;

      if (cnt == n - 1) {
        printf("%ld\n", result);
        return 0;
      }
    }
  }

  printf("-1\n");

  return 0;
}