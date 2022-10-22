
import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.stdin = open('venv/inp.txt', 'r')
print(type(sys.stdin))
lst=[]
l=[]
class Grraph:
    def minDistance(self, dist, queue):
        minimum = float("Inf")
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def printPath(self, parent, j):

        if parent[j] == -1:
            lst.append(j)
            print(j, end=" ")
            return
        self.printPath(parent, parent[j])
        lst.append(j)
        print(j, end=" ")


    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]), end=" ")
            # lst=[]
            self.printPath(parent, i)
            l.append(lst)
    def dijkstra(self, graph, src):

        row = len(graph)
        col = len(graph[0])

        dist = [float("Inf")] * row

        parent = [-1] * row

        dist[src] = 0

        queue = []
        for i in range(row):
            queue.append(i)

        while queue:


            u = self.minDistance(dist, queue)

            queue.remove(u)

            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

        self.printSolution(dist, parent)

g = Grraph()
# i=0
print("Entre number of vertices:")
v=int(input())
print("Entre number of edges:")
E=int(input())
print("are you using 0 based indexing[Y/N]")
xing=input()

graph = [ [0] * v for _ in range(v)]
# print(graph)
a=0
b=0
c=0
G=nx.DiGraph()
e=1
o=4
for i in range(v):
    if i%2 == 0:
        G.add_node(i,pos=(e,o))
        e=e+1
        o=o-1

    else:
        G.add_node(i, pos=(e, o))
        o=o+1
        e=e+6

for i in range(E):
    [a,b,c] =list(map(int, input().split()))
    # print(a,b,c)
    if(xing=='N'):
        a-=1;
        b-=1;
    graph[a][b]=c
    graph[b][a]=c
    G.add_edge(a,b,weight=c)

weight=nx.get_edge_attributes(G,'weight')
pos=nx.get_node_attributes(G,'pos')
plt.figure(1)
nx.draw_networkx(G,pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=weight)
plt.show()
fig, axes = plt.subplots(nrows=int(v/2), ncols=2)
ax = axes.flatten()
# print(graph)
# graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#          [4, 0, 8, 0, 0, 0, 0, 11, 0],
#          [0, 8, 0, 7, 0, 4, 0, 0, 2],
#          [0, 0, 7, 0, 9, 14, 0, 0, 0],
#          [0, 0, 0, 9, 0, 10, 0, 0, 0],
#          [0, 0, 4, 14, 10, 0, 2, 0, 0],
#          [0, 0, 0, 0, 0, 2, 0, 1, 6],
#          [8, 11, 0, 0, 0, 0, 1, 0, 7],
#          [0, 0, 2, 0, 0, 0, 6, 7, 0]
#          ]


g.dijkstra(graph, 0)
print("")
# print(lst)
last=0
j=1
tmp=[]
res=[]
i=0
for each in range(len(lst)):
    if i>=len(lst):
        break
    while lst[i]!=j:
        tmp.append(lst[i])
        i=i+1
    tmp.append(lst[i])
    i=i+1
    res.append(tmp)
    # print(tmp)
    tmp=[]
    j=j+1
# print(lst)
# print("\n\n")
# print(res)
grp=[None]*(v-1)
for j in range(len(res)):
    grp[j] = nx.DiGraph()
    for i in range(v):
        if i % 2 == 0:
            grp[j].add_node(i, pos=(e, o))
            e = e + 1
            o = o - 1
        else:
            grp[j].add_node(i, pos=(e, o))
            o = o + 1
            e = e + 6
for i in range(len(res)):

    for j in range(len(res[i])-1):
        if res[i][j+1]:
            grp[i].add_edge(res[i][j],res[i][j+1],weight=graph[res[i][j]][res[i][j+1]])
    weight = nx.get_edge_attributes(grp[i], 'weight')
    pos = nx.get_node_attributes(grp[i], 'pos')
    nx.draw_networkx(grp[i], pos, ax=ax[i],with_labels=True)
    nx.draw_networkx_edge_labels(grp[i],pos, edge_labels=weight)
    # nx.draw(grp[i])
    ax[i].set_axis_off()


plt.show()
