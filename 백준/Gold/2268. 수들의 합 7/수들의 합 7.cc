#include <iostream>
#include <vector>

using namespace std;

long long tree[4000001];

void update(int node, int start, int end, int index, long long value) {
  if (start > index || end < index) {
    return;
  }
  if (start == end) {
    tree[node] = value;
    return;
  }

  int mid = (start + end) / 2;

  update(node * 2, start, mid, index, value);
  update(node * 2 + 1, mid + 1, end, index, value);

  tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

long long query(int node, int start, int end, int left, int right) {
  if (end < left || start > right) {
    return 0;
  }
  if (start >= left && end <= right) {
    return tree[node];
  }

  int mid = (start + end) / 2;
  return query(node * 2, start, mid, left, right) +
         query(node * 2 + 1, mid + 1, end, left, right);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, m;
  cin >> n >> m;

  for (int i = 0; i < m; i++) {
    long long a, b, c;
    cin >> a >> b >> c;

    if (a == 0) {
      int left = min((int)b - 1, (int)c - 1);
      int right = max((int)b - 1, (int)c - 1);
      cout << query(1, 0, n - 1, left, right) << '\n';
    } else {
      update(1, 0, n - 1, (int)b - 1, c);
    }
  }
  return 0;
}