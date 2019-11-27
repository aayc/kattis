#include <iostream>
#include <cmath>

using namespace std;

int pattern[3][3];
int main() {
  for(int r = 0; r < 3; r++) {
    for(int c = 0; c < 3; c++) {
      cin >> pattern[r][c];
    }
  }

  double prevr = -1;
  double prevc = -1;
  long double dist = 0;
  for (int i = 1; i <= 9; i++) {
    for(int r = 0; r < 3; r++) {
      for(int c = 0; c < 3; c++) {
        if (pattern[r][c] == i) {
          if (prevr >= 0) {
            dist += sqrtl((r - prevr)*(r - prevr) + (c - prevc)*(c - prevc));
          }
          prevr = r;
          prevc = c;
          break;
        }
      }
    }
  }
  cout.precision(10);
  cout << dist << endl;
}

