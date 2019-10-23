#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define MP make_pair
#define fr(i,n) for (i = 0; i < n; ++i) 
#define rep(i,k,n) for (i = k; i <= n; ++i) 
#define repr(i,k,n) for (i = k; i >= n; --i) 
const ll MAX =1e9+7;

vector <int> adj[100001];
bool visited[100001];
ll ctr=0;
void dfs(int s) {
        visited[s] = true;
        for(int i = 0;i < adj[s].size();++i)    {
            if(visited[adj[s][i]] == false){
                ctr++;
                dfs(adj[s][i]);
            }
        }
}

void initialize() {
        for(int i = 1;i <= 100000;++i)
            visited[i] = false;
}

void fastscan(int &x)
    {
        bool neg=false;
        register int c;
        x =0;
        c=getchar();
        if(c=='-')
        {
            neg = true;
            c=getchar();
        }
        for(;(c>47 && c<58);c=getchar())
            x = (x<<1) + (x<<3) +c -48;
        if(neg)
            x *=-1;
    }

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
  
    ll n,m,x,y,i,k;
    cin>>n;
    fr(i,m){
        cin>>x>>y;
        adj[x].pb(y);
        adj[y].pb(x);
    }
   
    initialize();
    

      
    return 0;
}    