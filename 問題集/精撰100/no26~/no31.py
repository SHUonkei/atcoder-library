def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    W,H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]

    data = [[0]*W] + data
    data.append([0]*W)

    for i in range(H+2):
        data[i].append(0)
        data[i] = [0]+ data[i]

    #print(data)

    even_dy = [1,0,-1,0,-1,1]
    even_dx = [0,1,0,-1,-1,-1]

    odd_dy = [1,0,-1,0,1,-1]
    odd_dx = [0,1,0,-1,1,1]


    def bfs(y,z):
        count = 0
        Q = deque()
        Q.append((y,z))
        dist = [[-1]*(W+2) for _ in range(H+2)]
        dist[y][z] = 1
    #    j = 0
        while len(Q)>0:
    #        print(Q)
    #        j +=1
    #        if j == 10:
    #            exit()
    #        print(dist)
    #        print(count)
            x = Q.popleft()
            #ここにdist = 1をいれると、すでにQにいれたのに探索して死まくことがあるのでダメ
    #        print(x)
    #        if data[x[0]][x[1]]:
    #            continue
            for i in range(6):

                if x[0]%2 == 0:
                    u = x[0]+even_dy[i]
                    v = x[1]+even_dx[i]
                else:
                    u = x[0]+odd_dy[i]
                    v = x[1]+odd_dx[i]
    #            print(u,v)
                if 0 <= u < H+2 and 0 <= v < W+2:
                    if dist[u][v] == -1:
                        if data[u][v]:
                            count += 1
    #                        print((x[1],x[0]),(v,u))
                            continue
                        dist[u][v] = 1
                        Q.append((u,v))
    #    for i in range(H+2):
    #        print(*dist[i])
        return count



    ans = bfs(0,0)
    print(ans)

if __name__ == "__main__":
	main()