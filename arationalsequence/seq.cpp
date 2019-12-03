#include <iostream>
#include <cmath>
#include <queue>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int main() {
  int N;
  cin >> N;
  for (int t = 0; t < N; t++) {
    long long m, p, q;
    char c;
    cin >> m >> p >> c >> q;

    queue<pair<int, int>> pq;
    pq.push(pair<int, int>(1, 1));
    long long n = 1;
    while (true) {
      pair<int, int> node = pq.front();
      pq.pop();
      //cout << node.first << "/" << node.second << endl;
      if (node.first == p && node.second == q) {
        break;
      }
      else {
        pq.push(pair<int, int>(node.first, node.second + node.first));
        pq.push(pair<int, int>(node.first + node.second, node.second));
      }
      n += 1;
    }
    cout << n << endl;
  }

}
