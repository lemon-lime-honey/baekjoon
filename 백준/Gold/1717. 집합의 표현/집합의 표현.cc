#include <iostream>
#include <vector>

using namespace std;

vector<int> parent;

int find(int p) {
  if (parent[p] != p) parent[p] = find(parent[p]);
  return parent[p];
}

void _union(int p, int q) {
  p = find(p);
  q = find(q);
  if (p == q) return;
  if (p < q)
    parent[q] = p;
  else
    parent[p] = q;
  return;
}

int main() {
  int n, m;
  scanf("%d %d", &n, &m);

  for (int i = 0; i < n + 1; i++) {
    parent.push_back(i);
  }

  for (int i = 0; i < m; i++) {
    int command, a, b;
    scanf("%d %d %d", &command, &a, &b);

    switch (command) {
      case 0:
        _union(a, b);
        break;
      case 1:
        if (find(a) == find(b))
          printf("YES\n");
        else
          printf("NO\n");
        break;
    }
  }

  return 0;
}
