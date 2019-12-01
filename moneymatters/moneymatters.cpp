#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>
#include <map>
using namespace std;

int debts[10000];
bool V[10000] = {0};
int dfs(int node, map<int, vector<int>> &edges) {
  int ret = debts[node];
  if (edges.find(node) != edges.end()) {
    for(int i = 0; i < edges[node].size(); i++) {
      if (!V[edges[node][i]]) {
        V[edges[node][i]] = true;
        ret += dfs(edges[node][i], edges);
      }
    }
  }
  return ret;
}

int main() {
  int N, M;
  cin >> N >> M;

  for (int i = 0; i < N; i++) {
    cin >> debts[i];
  }

  map<int, vector<int>> edges;
  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    if (edges.find(a) == edges.end()) {
      vector<int> empty;
      edges.insert(pair<int, vector<int>>(a, empty));
    }
    if (edges.find(b) == edges.end()) {
      vector<int> empty;
      edges.insert(pair<int, vector<int>>(b, empty));
    }
    edges[a].push_back(b);
    edges[b].push_back(a);
  }

  for (int i = 0; i < N; i++) {
    if (!V[i]) {
      V[i] = true;
      int sum = dfs(i, edges);
      if (sum != 0) {
        cout << "IMPOSSIBLE";
        return 0;
      }
    }
  }
  cout << "POSSIBLE" << endl;
}
