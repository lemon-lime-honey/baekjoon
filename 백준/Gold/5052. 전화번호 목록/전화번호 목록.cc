#include <iostream>
#include <string>

using namespace std;

class Node {
 public:
  Node* children[10];
  bool last;

  Node() {
    last = false;
    for (int i = 0; i < 10; i++) {
      children[i] = nullptr;
    }
  }
};

class Trie {
  Node* root;

 public:
  Trie() { root = new Node(); }

  bool insert(string target) {
    Node* node = root;
    bool result = true;

    for (int i = 0; i < target.length(); i++) {
      if (node->children[target[i] - '0']) {
        node = node->children[target[i] - '0'];
        if (node->last || i == target.length() - 1) result = false;
      } else {
        node->children[target[i] - '0'] = new Node();
        node = node->children[target[i] - '0'];
      }
    }

    node->last = true;
    return result;
  }
};

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    int n;
    bool result = true;
    Trie trie;

    cin >> n;

    for (int j = 0; j < n; j++) {
      string num;
      cin >> num;

      if (!trie.insert(num)) result = false;
    }

    if (result)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }

  return 0;
}