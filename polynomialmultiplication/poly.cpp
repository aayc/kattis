#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t < T; t++) {
    int l1;
    cin >> l1;
    int p1[l1 + 1];
    for(int i = 0; i <= l1; i++) {
      cin >> p1[i];
    }

    int l2;
    cin >> l2;
    int p2[l2 + 1];
    for(int i = 0; i <= l2; i++) {
      cin >> p2[i];
    }

    // Do multiplication
    int final_degree = l1 + l2 + 1;
    int result[final_degree];
    for(int i = 0; i < final_degree; i++) result[i] = 0;

    for(int i = 0; i <= l1; i++) {
      int i_degree = l1 - i - 1;
      for (int j = 0; j <= l2; j++) {
        int j_degree = l2 - j - 1;
        result[final_degree - (i_degree + j_degree) - 3] += p1[i] * p2[j];
      }
    }

    cout << final_degree - 1<< endl;
    for(int i = 0; i < final_degree; i++) {
      cout << result[i];
      if (i != final_degree - 1) {
        cout << " ";
      }
    }
    cout << endl;
  }
}
