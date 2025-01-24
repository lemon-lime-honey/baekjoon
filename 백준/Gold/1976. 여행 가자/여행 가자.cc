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

  scanf("%d\n%d", &n, &m);

  for (int i = 0; i < n + 1; i++) {
    parent.push_back(i);
  }

  for (int i = 1; i < n + 1; i++) {
    int target;

    for (int j = 1; j < n + 1; j++) {
      scanf("%d", &target);
      if (i != j && target == 1) _union(i, j);
    }
  }

  int city, ref;
  bool result = true;

  scanf("%d", &city);
  ref = find(city);

  for (int i = 0; i < m - 1; i++) {
    scanf(" %d", &city);
    if (find(city) != ref) {
      result = false;
    }
  }

  if (result) printf("YES\n");
  else printf("NO\n");

  return 0;
}
