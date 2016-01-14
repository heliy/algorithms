struct edge{
  int v;
  bool type;
}

bool test_bipartite(vector<vector<edge> > &linklst){
  int n = lnklst.size();
  vector<bool> color(n);
  vector<bool> visited(n);
  queue<int> q;
  color[0] = 0;
  q.push(0);
  visited[0] = true;
  while(!q.empty()){
    int u = q.front();
    q.pop();
    for(int i = 0; i < lnklst[u].size(); i++){
      edge e = lnklst[u][i];
      int v = e.v;
      if(!visited[v]){
	color[v] = color[u]^e.type;
	q.push(v);
	visited[v] = true;
      }else{
	if(color[v] != color[u]^e.type){
	  return false;
	}
      }
    }
  }
  return true;
}
