from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
	"""
	Count shortest paths from starting node to all nodes of graph g
	:param g: Graph from NetworkX
	:param starting_node: starting node from g
	:return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
	"""
	print(g, starting_node)
	return dict()


def dfs_find(graph, src, dst, visited):
	visited[src] = True
	#print(visited)
	if src == dst:
		return True

	for node in graph.adj[src]:
		if not visited[node]:
			if dfs_find(graph, node, dst, visited):
				print(visited)
				return True

	return False


if __name__ == "__main__":
	graph = nx.Graph()
	graph.add_nodes_from("ABCDEFG")
	graph.add_edges_from(

		[
			("A", "B"),
			("A", "C"),
			("B", "D"),
			("B", "E"),
			("C", "F"),
			("E", "G"),
			("Q", "W"),
		]
	)

	graph.add_node('Z')
	src = "A"
	dst = "F"
	visited = {node: False for node in graph.nodes()}
	# for node in graph.adj:
	# 	print(node, graph.adj[node])

	print(dfs_find(graph, src, dst, visited))
