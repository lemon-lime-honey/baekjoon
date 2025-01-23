#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool cmp(vector<int>& v1, vector<int>& v2);
int find(int p);
bool _union(int p, int q);

vector<int> parent;

int main() {
  int n;
  cin >> n;

  vector<vector<int>> graph;

  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - 1 - i; j++) {
      int w;
      cin >> w;
      graph.push_back(vector<int>{w, i + 1, i + j + 2});
    }
  }

  sort(graph.begin(), graph.end(), cmp);
  vector<vector<int>> result;

  for (int i = 0; i < n + 1; i++) {
    result.push_back(vector<int>{});
  }

  for (int i = 0; i < n + 1; i++) {
    parent.push_back(i);
  }

  for (int i = 0; i < (int)graph.size(); i++) {
    if (_union(graph[i][1], graph[i][2])) {
      result[graph[i][1]].push_back(graph[i][2]);
      result[graph[i][2]].push_back(graph[i][1]);
    }
  }

  for (int i = 1; i < n + 1; i++) {
    cout << result[i].size() << " ";
    sort(result[i].begin(), result[i].end());
    for (int j = 0; j < (int)result[i].size(); j++) {
      cout << result[i][j];
      if (j != (int)result[i].size() - 1)
        cout << " ";
      else
        cout << endl;
    }
  }

  return 0;
}

bool cmp(vector<int>& v1, vector<int>& v2) {
  if (v1[0] == v2[0] && v1[1] != v2[1]) return v1[1] < v2[1];
  if (v1[0] == v2[0] && v1[1] == v2[1]) return v1[2] < v2[2];
  return v1[0] < v2[0];
}

int find(int p) {
  if (parent[p] != p) parent[p] = find(parent[p]);
  return parent[p];
}

bool _union(int p, int q) {
  p = find(p);
  q = find(q);

  if (p == q) return false;
  if (p < q)
    parent[q] = p;
  else
    parent[p] = q;
  return true;
}