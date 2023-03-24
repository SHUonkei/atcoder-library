inf = float('INF')
def BellmanFord(G, s):
    """
    s:スタート地点
    G: 隣接グラフ [ [(v0,d0),...,(vj, dj)],..., [(v2,d2)]]
    返り値
    dist: 頂点sからの最小コストを管理しているリスト
    negative_cycle: True/False (負の閉路を持つか否か)
    """
    n = len(G) #頂点数
    costs = [inf]*n #頂点sからの到達コストを管理するリスト
    negative_cycle = False

    #スタート地点
    costs[s] = 0
    for i in range(n):
        update = False #更新の有無
        #各頂点
        for v in range(n):

            #頂点vから出る辺の重みをみる
            for to, c in G[v]:
                if costs[to] > costs[v] + c:
                    costs[to] = costs[v]+c
                    update = True
        if update == False:
            break
        if i==n-1 and update==True:
            negative_cycle = True
    
    
    return costs, negative_cycle