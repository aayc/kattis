#include <iostream>
#include <unordered_set>
using namespace std;

int N = 0;

int dfs(int node, bool** A, unordered_set<int> &V) {
  int edges = 0;
  for(int i = 0; i < N; i++) {
    if (A[node][i] && V.find(i) != V.end()) {
      edges += 1;
      V.insert(i);
      edges += dfs(i, A, V);
    }
  }
  return edges;
}

int main() {
  int T;
  cin >> T;

  for(int t = 0; t < T; t++) {
    int n, m;
    cin >> n >> m;

    bool** A = new bool[N][N];
    memset(A, 0, sizeof(A[0][0]) * N * N);

    for(int i = 0; i < M; i++) {
      int a, b;
      cin >> a >> b;
      A[a - 1][b - 1] = true;
      A[b - 1][a - 1] = true;
    }

    unordered_set<int> V = { 0 };
    cout << dfs(0, A, V);
  }

}
