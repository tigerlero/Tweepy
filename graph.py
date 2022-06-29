import networkx as nx
import matplotlib.pyplot as plt
from utils import BuildDict, SortCentrality, WriteCentrality



users = BuildDict()

# Build graph
g = nx.DiGraph()
g.add_nodes_from(users.values())
for u_id, u_nm in users.items():
    f = open("ids/{}".format(u_id), 'r')
    followers = [l.strip() for l in f.readlines()]
    f.close()
    [g.add_edge(users[follower], u_nm) for follower in followers if follower in users.keys()]

nx.draw(g)
plt.savefig("graph.png")
nx.write_gml(g, "graph.gml")

report = open("graph_report.txt", "w")

report.write("---IN AND OUT EDGES---\n\n")

for n in g:
    report.write("{}, {}, {}\n".format(n, len(g.in_edges(n)), len(g.out_edges(n))))


report.write("\n\n--COMPONENTS---\n")

report.write("\nStrongly Connected Components:\n\n")

s_components = nx.strongly_connected_components(g)
for c in s_components:
    report.write("{}\n".format(c))


report.write("\n\n---CENTRALITIES---\n")

d_centrality = nx.degree_centrality(g)
i_centrality = nx.in_degree_centrality(g)
o_centrality = nx.out_degree_centrality(g)
c_centrality = nx.closeness_centrality(g)
b_centrality = nx.betweenness_centrality(g)
e_centrality = nx.eigenvector_centrality(g)

sorted_d = SortCentrality(d_centrality)
sorted_i = SortCentrality(i_centrality)
sorted_o = SortCentrality(o_centrality)
sorted_c = SortCentrality(c_centrality)
sorted_b = SortCentrality(b_centrality)
sorted_e = SortCentrality(e_centrality)

report.write("\nDegree Centrality\n\n")
WriteCentrality(report, sorted_d, d_centrality)

report.write("\n\nIn-Degree Centrality\n\n")
WriteCentrality(report, sorted_i, i_centrality)

report.write("\n\nOut-Degree Centrality\n\n")
WriteCentrality(report, sorted_o, o_centrality)

report.write("\n\nCloseness Degree Centrality\n\n")
WriteCentrality(report, sorted_c, c_centrality)

report.write("\n\nBetweenness Degree Centrality\n\n")
WriteCentrality(report, sorted_b, b_centrality)

report.write("\n\nEigenvector Degree Centrality\n\n")
WriteCentrality(report, sorted_e, e_centrality)
