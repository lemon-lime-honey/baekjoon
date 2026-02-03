#include <iostream>
#include <vector>

using namespace std;

long long nums[1000001];
long long tree[4000001];

long long init(int node, int start, int end) {
  if (start == end) return tree[node] = nums[start];
  int mid = (start + end) / 2;
  return tree[node] =
             init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end);
}

void update(int node, int start, int end, int index, long long val) {
  if (index < start || index > end) return;
  if (start == end) {
    tree[node] = val;
    return;
  }
  int mid = (start + end) / 2;
  update(node * 2, start, mid, index, val);
  update(node * 2 + 1, mid + 1, end, index, val);
  tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

long long query(int node, int start, int end, int left, int right) {
  if (left > end || right < start) return 0;
  if (left <= start && right >= end) return tree[node];
  int mid = (start + end) / 2;
  return query(node * 2, start, mid, left, right) +
         query(node * 2 + 1, mid + 1, end, left, right);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, m, k;
  cin >> n >> m >> k;

  for (int i = 0; i < n; i++) cin >> nums[i];

  init(1, 0, n - 1);

  for (int i = 0; i < m + k; i++) {
    long long a, b, c;
    cin >> a >> b >> c;
    if (a == 1) {
      update(1, 0, n - 1, (int)b - 1, c);
    } else {
      cout << query(1, 0, n - 1, (int)b - 1, (int)c - 1) << "\n";
    }
  }
  return 0;
}