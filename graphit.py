import networkx as nx
import matplotlib.pyplot as plt

color = True
labels = True
target = "test"
graph = nx.Graph()
headnodes = {}
allnodes = {}
# filename = input("input filname")
f = open("sex.txt", 'r')
for x in f:
    subject, edges = x.strip().split(':')
    subject = subject.strip()
    edges = list(map(lambda x: x.strip(), edges.split(",")))
    subjectfirst, subjectlast = None, None
    if " " in subject:
        subjectfirst = subject.split(" ")[0]
        subjectlast = subject.split(" ")[1]
    elif subject in allnodes:
        subjectfirst, subjectlast = allnodes[subject].split(" ")
    if subjectfirst:
        subject = subjectfirst + " " + subjectlast
        headnodes[subjectfirst] = subjectfirst + " " + subjectlast
    graph.add_node(subject)
    for edge in edges:
        edgefirst, edgelast = None, None
        if " " in edge:
            edgefirst = edge.split(" ")[0]
            edgelast = edge.split(" ")[1]
        elif edge in allnodes:
            edgefirst, edgelast = allnodes[edge].split(" ")
        if edgefirst:
            edge = edgefirst + " " + edgelast
            allnodes[edgefirst] = edgefirst + " " + edgelast
        graph.add_node(edge)
        graph.add_edge(subject, edge)
dists = nx.single_source_shortest_path(graph, target)
colormap = {
    1:"#3458eb",
    2:"#9e34eb",
    3:"#eb34cf",
    4:"#6e0c31",
    5:"#eb1328"
}
colors = list(map(lambda x: len(dists[x]), list(graph)))
print(colors)
print(list(graph))
mf = open("masc.txt", 'r')
masc = list(map(lambda x: x.strip(),mf.readline().strip().split(",")))
if color == False:
    colors = list(map(lambda x: "#f024e6" if x not in masc else "#0c41f0", list(graph)))
nx.draw_kamada_kawai(graph, with_labels=labels, node_color=colors)
plt.show()
