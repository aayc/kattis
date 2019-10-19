#include <iostream>
using namespace std;

int main() {
  oo = 100000000;
  int N, M, T, start_air;
  cin >> N >> M >> T >> start_air;

  vector<pair<int, int>>[N] neighbors;
  for (int i = 0; i < M; i++) {
    int f, t, d;
    scanf("%d %d %d", &f, &t, &d);

    neighbors[f - 1].push_back(pair<int, int>(t - 1, d));
    neighbors[t - 1].push_back(pair<int, int>(f - 1, d));

  }
}


