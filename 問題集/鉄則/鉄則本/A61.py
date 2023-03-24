N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)  # 有向グラフなら消す
for i in range(N):
    
    print(str(i+1)+": ", end = "")
    if len(graph[i]) == 0:
        print("{"+"}")
        continue
    print(set(graph[i]))



