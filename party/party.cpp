#include<bits/stdc++.h>

using namespace std;

void aloneAtParty(vector<int> people){
  map<int, int> age;
  for(int a: people){
    age[a] ^= 1;
  }
  for(auto it=age.begin(); it!=age.end(); it++){
    if(it->second == 1){
      cout << "The person alone is " << it->first <<" years old.\n";
      return;
    }
  }
  cout << "Everybody's got a pair.\n";
}

int main(){

  aloneAtParty(vector<int>{25, 19, 21, 25, 21});
  aloneAtParty(vector<int>{25, 19, 21, 25, 21, 19});

  return 0;
}
