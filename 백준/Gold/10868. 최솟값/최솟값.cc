#include <iostream>
#include <vector>

using namespace std;

long long nums[100001];
long long tree[400001];

long long init(int node, int start, int end) {
  if (start == end) {
    tree[node] = nums[start];
    return tree[node];
  }

  int mid = (start + end) / 2;
  tree[node] =
      min(init(node * 2, start, mid), init(node * 2 + 1, mid + 1, end));
  return tree[node];
}

long long query(int node, int start, int end, int left, int right) {
  if (end < left || start > right) {
    return 10000000000;
  }
  if (start >= left && end <= right) {
    return tree[node];
  }

  int mid = (start + end) / 2;
  return min(query(node * 2, start, mid, left, right),
             query(node * 2 + 1, mid + 1, end, left, right));
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, m;
  cin >> n >> m;

  for (int i = 0; i < n; i++) cin >> nums[i];
  for (int i = 0; i < 4 * n; i++) tree[i] = 10000000000;

  init(1, 0, n - 1);

  for (int i = 0; i < m; i++) {
    long long a, b;
    cin >> a >> b;
    cout << query(1, 0, n - 1, (int)a - 1, (int)b - 1) << "\n";
  }
  return 0;
}