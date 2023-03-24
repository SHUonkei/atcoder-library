#帰りがけ順->ラベル
#逆グラフにする
#ラベルの大きい順

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)

    N,M = map(int,input().split())
    def f(n):
        return int(n)-1
    AB = [list(map(f,input().split())) for  in range(M)]

    e = [[] for  in range(N)]
    ie = [[] for  in range(N)]

    for i in range(M):
        e[AB[i][0]].append(AB[i][1])
        ie[AB[i][1]].append(AB[i][0])

    visited = [0 for  in range(N)]
    scc = []
    num = [-1 for  in range(N)]
    l = []

    def dfs(n,l):
        visited[n] = 1
        for i in e[n]:
            if visited[i]:
                continue
            dfs(i,l)
        l.append(n)
        num[n] = len(l)
        return

    for i in range(N):
        if visited[i] == 0:
            dfs(i,l)

    visited = [0 for  in range(N)]
    l.reverse()

    def dfs2(n):
        visited[n] = 1
        scc[len(scc)-1].append(n)
        for i in ie[n]:
            if visited[i]:
                continue
            dfs2(i)

    for i in range(len(l)):
        if visited[l[i]]:
            continue
        scc.append([])
        dfs2(l[i])
    #-----------------------

    count = 0
    c = 0
    for i in range(len(scc)):
        n = len(scc[i])
        if n >= 2:
            count += n + c
            c = 0
        else:
            c += 1
    print(scc)
    print(count)

if name == 'main':
    main()
#帰りがけ順->ラベル
#逆グラフにする
#ラベルの大きい順

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)

    N,M = map(int,input().split())
    def f(n):
        return int(n)-1
    AB = [list(map(f,input().split())) for  in range(M)]

    e = [[] for  in range(N)]
    ie = [[] for  in range(N)]

    for i in range(M):
        e[AB[i][0]].append(AB[i][1])
        ie[AB[i][1]].append(AB[i][0])

    visited = [0 for  in range(N)]
    scc = []
    num = [-1 for  in range(N)]
    l = []

    def dfs(n,l):
        visited[n] = 1
        for i in e[n]:
            if visited[i]:
                continue
            dfs(i,l)
        l.append(n)
        num[n] = len(l)
        return

    for i in range(N):
        if visited[i] == 0:
            dfs(i,l)

    visited = [0 for  in range(N)]
    l.reverse()

    def dfs2(n):
        visited[n] = 1
        scc[len(scc)-1].append(n)
        for i in ie[n]:
            if visited[i]:
                continue
            dfs2(i)

    for i in range(len(l)):
        if visited[l[i]]:
            continue
        scc.append([])
        dfs2(l[i])
    #-----------------------

    count = 0
    c = 0
    for i in range(len(scc)):
        n = len(scc[i])
        if n >= 2:
            count += n + c
            c = 0
        else:
            c += 1
    print(scc)
    print(count)

if name == 'main':
    main()
#帰りがけ順->ラベル
#逆グラフにする
#ラベルの大きい順

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)

    N,M = map(int,input().split())
    def f(n):
        return int(n)-1
    AB = [list(map(f,input().split())) for  in range(M)]

    e = [[] for  in range(N)]
    ie = [[] for  in range(N)]

    for i in range(M):
        e[AB[i][0]].append(AB[i][1])
        ie[AB[i][1]].append(AB[i][0])

    visited = [0 for  in range(N)]
    scc = []
    num = [-1 for  in range(N)]
    l = []

    def dfs(n,l):
        visited[n] = 1
        for i in e[n]:
            if visited[i]:
                continue
            dfs(i,l)
        l.append(n)
        num[n] = len(l)
        return

    for i in range(N):
        if visited[i] == 0:
            dfs(i,l)

    visited = [0 for  in range(N)]
    l.reverse()

    def dfs2(n):
        visited[n] = 1
        scc[len(scc)-1].append(n)
        for i in ie[n]:
            if visited[i]:
                continue
            dfs2(i)

    for i in range(len(l)):
        if visited[l[i]]:
            continue
        scc.append([])
        dfs2(l[i])
    #-----------------------

    count = 0
    c = 0
    for i in range(len(scc)):
        n = len(scc[i])
        if n >= 2:
            count += n + c
            c = 0
        else:
            c += 1
    print(scc)
    print(count)

if name == 'main':
    main()
#帰りがけ順->ラベル
#逆グラフにする
#ラベルの大きい順

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)

    N,M = map(int,input().split())
    def f(n):
        return int(n)-1
    AB = [list(map(f,input().split())) for  in range(M)]

    e = [[] for  in range(N)]
    ie = [[] for  in range(N)]

    for i in range(M):
        e[AB[i][0]].append(AB[i][1])
        ie[AB[i][1]].append(AB[i][0])

    visited = [0 for  in range(N)]
    scc = []
    num = [-1 for  in range(N)]
    l = []

    def dfs(n,l):
        visited[n] = 1
        for i in e[n]:
            if visited[i]:
                continue
            dfs(i,l)
        l.append(n)
        num[n] = len(l)
        return

    for i in range(N):
        if visited[i] == 0:
            dfs(i,l)

    visited = [0 for  in range(N)]
    l.reverse()

    def dfs2(n):
        visited[n] = 1
        scc[len(scc)-1].append(n)
        for i in ie[n]:
            if visited[i]:
                continue
            dfs2(i)

    for i in range(len(l)):
        if visited[l[i]]:
            continue
        scc.append([])
        dfs2(l[i])
    #-----------------------

    count = 0
    c = 0
    for i in range(len(scc)):
        n = len(scc[i])
        if n >= 2:
            count += n + c
            c = 0
        else:
            c += 1
    print(scc)
    print(count)

if name == 'main':
    main()
わら
むず
#帰りがけ順->ラベル
#逆グラフにする
#ラベルの大きい順

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)

    N,M = map(int,input().split())
    def f(n):
        return int(n)-1
    AB = [list(map(f,input().split())) for  in range(M)]

    e = [[] for  in range(N)]
    ie = [[] for  in range(N)]

    for i in range(M):
        e[AB[i][0]].append(AB[i][1])
        ie[AB[i][1]].append(AB[i][0])

    visited = [0 for  in range(N)]
    scc = []
    num = [-1 for  in range(N)]
    l = []

    def dfs(n,l):
        visited[n] = 1
        for i in e[n]:
            if visited[i]:
                continue
            dfs(i,l)
        l.append(n)
        num[n] = len(l)
        return

    for i in range(N):
        if visited[i] == 0:
            dfs(i,l)

    visited = [0 for  in range(N)]
    l.reverse()

    def dfs2(n):
        visited[n] = 1
        scc[len(scc)-1].append(n)
        for i in ie[n]:
            if visited[i]:
                continue
            dfs2(i)

    for i in range(len(l)):
        if visited[l[i]]:
            continue
        scc.append([])
        dfs2(l[i])
    #-----------------------

    count = 0
    c = 0
    for i in range(len(scc)):
        n = len(scc[i])
        if n >= 2:
            count += n + c
            c = 0
        else:
            c += 1
    print(scc)
    print(count)

if name == 'main':
    main()