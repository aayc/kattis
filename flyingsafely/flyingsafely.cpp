#include <iostream>
#include <cstring>
#include <unordered_set>
using namespace std;

bool A[10000][10000];
int dfs(int node, int N, unordered_set<int> &V) {
  int edges = 0;
  for(int i = 0; i < N; i++) {
    if (A[node][i] && V.find(i) == V.end()) {
      edges += 1;
      V.insert(i);
      edges += dfs(i, N, V);
    }
  }
  return edges;
}

int main() {
  int T;
  cin >> T;

  for(int t = 0; t < T; t++) {
    int N, M;
    cin >> N >> M;

    memset(A, 0, sizeof(A[0][0]) * N * N);

    for(int i = 0; i < M; i++) {
      int a, b;
      cin >> a >> b;
      A[a - 1][b - 1] = true;
      A[b - 1][a - 1] = true;
    }

    unordered_set<int> V = { 0 };
    cout << dfs(0, N, V) << endl;
  }

}
