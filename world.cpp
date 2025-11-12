#include<iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++) cin >> a[i];

    sort(a.begin(), a.end());

    long long ans = 0;
    for(int i = 0; i < n / 2; i++){
        ans += (a[n - 1 - i] - a[i]) * (a[n - 1 - i] - a[i]);
    }

    cout << ans << '\n';

    return 0;
}