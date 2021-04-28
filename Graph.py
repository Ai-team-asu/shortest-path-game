oo = 0x3f3f3f3f3f3f3f3f
def __run_dijkstra(self):
    dis = []
    par = []

    src = 0
    des = len(self.graph_nodes) - 1
    for i in self.graph_edges:
        dis.append(oo)
        par.append(-1)
    dis[src] = 0
    pq = PriorityQueue()
    pq.put((0, src))
    while (not pq.empty()):
        t = pq.get()
        u = t[1]
        c = -t[0]
        if (dis[u] != c):
            continue
        for neigh in self.graph_edges[u]:
            v = neigh[0]
            vc = neigh[1]
            if dis[u] + vc < dis[v]:
                dis[v] = dis[u] + vc
                par[v] = u
                pq.put((-dis[v], v))
    path = []
    path.append(des)
    parent = par[des]
    while parent != -1:
        path.append(parent)
        parent = par[parent]
    path.reverse()
    final = []
    for a in path:
        for b in self.graph_nodes:
            if self.graph_nodes.index(b) == a:
                final.append(b[0])
                break
    print(final)
    return final, self.maze